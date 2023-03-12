from scrapy import FormRequest, Spider, Request
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad



# Define a SQLAlchemy model to represent the table
Base = declarative_base()
class Table(Base):
    __tablename__ = 'main'
    
    email = Column(String, primary_key=True)
    id = Column(Integer)
    # this is a string because it's a list of strings
    notified_studies = Column(String)
    username = Column(String)
    password = Column(String)
    

# https://medium.com/@sachadehe/encrypt-decrypt-data-between-python-3-and-javascript-true-aes-algorithm-7c4e2fa3a9ff
def decrypt(password, key):
    """ Decrypt username and password """

    # CBC with Fix IV
    #FIX IV
    iv =  'UWPMBFUOMDOADSJX'.encode('utf-8') #16 char for AES128

    def decrypt(enc,key,iv):
            enc = base64.b64decode(enc)
            cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
            return unpad(cipher.decrypt(enc), 16)

    decrypted = decrypt(password,key,iv)
    return decrypted.decode("utf-8", "ignore")  


class ScrapeSpider(Spider):
    name = 'get_info'
    allowed_domains = ['ucalgary.sona-systems.com']
    urls = ['https://ucalgary.sona-systems.com/']
    already_signed_up = 'You have already signed up for this study (and received credit or have a pending credit), so you may not sign up for it again.'
    prohibited = 'Sign-Up prohibited because of Sign-Up Restrictions. There are study pre-requisite or disqualifier requirements which you do not meet.'
    # Fetch data from the database using a session
    def start_requests(self):
        db_url = self.settings.get('DB_URL')
        # initialize the database connection
        # Create a SQLAlchemy engine object to connect to the database
        engine = create_engine(db_url)
        # Create a session factory to interact with the database
        Session = sessionmaker(bind=engine)
        self.session = Session()
        users = self.session.query(Table).all()
        
        # for user in users:
        for user in users:
            self.num_of_skipped = 0
            self.logger.info('Scraping user: %s', user.email)
            user_data = {
                'email': user.email,
                'notified': user.notified_studies,
                'data': []
            }
            # store coockiejar for the user
            yield Request(self.urls[0], callback=self.parse, cb_kwargs=dict(username=user.username, password=user.password, cookiejar=user.id, user_data=user_data), meta={'cookiejar': user.id}, dont_filter=True)

    def parse(self, response, username, password, cookiejar, user_data):
        
        # Get the CSRF token from the login form
        csrf_token = response.css(
            'input[name="csrf_token"]::attr(value)').get()

        # Login to the website
        yield FormRequest.from_response(response,
                                        formdata={
                                            'csrf_token': csrf_token,
                                            'ctl00$ContentPlaceHolder1$userid': username,
                                            'ctl00$ContentPlaceHolder1$pw': decrypt(password, self.settings.get('DECRYPT_KEY')),
                                            'ctl00$ContentPlaceHolder1$_default_auth_button': 'Log In'
                                        },
                                        callback=self.after_login,
                                        cb_kwargs=dict(cookiejar=cookiejar, user_data=user_data),
                                        meta={'cookiejar': cookiejar},
                                        dont_filter=True
                                        )

    def after_login(self, response, cookiejar, user_data):
        # open_in_browser(response)
        # Check if the login was successful
        if "VIEW AVAILABLE STUDIES" in response.text:
            # If the login was successful
            # redirect to the page that lists all the studies
            yield response.follow('https://ucalgary.sona-systems.com/all_exp_participant.aspx', callback=self.get_links, cb_kwargs=dict(cookiejar=cookiejar, user_data=user_data), meta={'cookiejar': cookiejar}, dont_filter=True)
        else:
            # If the login was unsuccessful, delete the user from the database and send an email to the user
            yield {'data': 'Login failed', 'email': user_data['email']}

    def get_links(self, response, cookiejar, user_data):
        # open_in_browser(response)
        links = set()
        # a tag is located in td tag
        scraped_links = response.css('td a::attr(href)').getall()
        for link in scraped_links:
            # get the id of the study from the link
            id = link.split('=')[1]
            # if the id has already been notified, don't add it to the data
            links.add(f'https://ucalgary.sona-systems.com/exp_info_participant.aspx?experiment_id={id}') if id not in user_data['notified'] else None
        num_of_links = len(links)
        link = links.pop()
        
        yield response.follow(link, callback=self.get_details, cb_kwargs=dict(user_data=user_data, links = links), meta={'cookiejar': cookiejar}, dont_filter=True)


    def get_details(self, response, user_data, links):
        add_to_data = True
        exp_id = response.url.split('=')[1]
        # user_data['data']
        
        scraped_data = {}
        # add experiment id to the data
        scraped_data['id'] = exp_id
        # for each tr tag in tbody tag, get the th text inside a span sometimes and make it the key and
        # the first text inside a span from the first td tag the value
        for tr in response.css('tbody tr'):
            # sometimes the key is inside a span tag and sometimes it's not
            key = tr.css('th span::text').get() or tr.css('th::text').get()
            key = str(key).strip()
            # if key == 'Study Type':
            #     value = str(tr.css('td strong::text').get()).strip()
            # else:
            #     value = str(tr.css('td span::text').get()).strip()
            # # inline if statement
            value = str(tr.css('td strong::text').get()).strip(
            ) if key == 'Study Type' else str(tr.css('td span::text').get()).strip()
            
            # if the value is already signed up or prohibited, don't add it to the data
            if self.already_signed_up in value or self.prohibited in value:
                add_to_data = False
                self.num_of_skipped += 1
                continue
            elif value == 'None':
                key = 'link'
                value = f'https://ucalgary.sona-systems.com/exp_view_slots.aspx?experiment_id={exp_id}'
            scraped_data[key] = value
        # add the data to the user_data if the user is not already signed up or prohibited
        user_data['data'].append(scraped_data) if add_to_data else None
        
        if len(links) > 0:
            link = links.pop() # get the next link
            yield response.follow(link, callback=self.get_details, cb_kwargs=dict(user_data=user_data, links = links), meta={'cookiejar': response.meta['cookiejar']}, dont_filter=True)
        else: # return the data to the pipeline to be processed and sent to the user as an email and update the database
            yield user_data


if __name__ == '__main__':
    spider = ScrapeSpider()
    spider.logger.log("Starting Spider")
    spider.start_requests()
