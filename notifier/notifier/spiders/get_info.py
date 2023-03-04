from scrapy import FormRequest, Spider, Request
from scrapy.utils.response import open_in_browser
from scrapy.utils.project import get_project_settings
from sqlalchemy import create_engine, Column, Integer, String
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
            print(enc, key, iv)
            enc = base64.b64decode(enc)
            cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
            return unpad(cipher.decrypt(enc), 16)

    decrypted = decrypt(password,key,iv)
    return decrypted.decode("utf-8", "ignore")  


class ScrapeSpider(Spider):
    # Define the database connection URL
    # settings = get_project_settings()
    # print(settings.get('DB_URL'))

    name = 'get_info'
    allowed_domains = ['ucalgary.sona-systems.com']
    urls = ['https://ucalgary.sona-systems.com/']
    
    # Fetch data from the database using a session
    def start_requests(self):
        db_url = self.settings.get('DB_URL')
        print("dburl",db_url)
        # initialize the database connection
        # Create a SQLAlchemy engine object to connect to the database
        engine = create_engine(db_url)
        # Create a session factory to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()
        users = session.query(Table).all()
        session.close()
        print(users[0].username, users[0].password)
        
        # for user in users:
        for user in users:
            yield Request(self.urls[0], callback=self.parse, meta={'username': user.username, 'password': user.password})
    

    def parse(self, response, username=None, password=None):
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
                                        callback=self.after_login
                                        )

    def after_login(self, response):
        # Check if the login was successful
        if "VIEW AVAILABLE STUDIES" in response.text:
            # If the login was successful, redirect to the page that lists all the studies
            yield response.follow('https://ucalgary.sona-systems.com/all_exp_participant.aspx', callback=self.get_links)

        else:
            # If the login was unsuccessful, print an error message
            self.logger.error("Login failed")

    def get_links(self, response):
        # open_in_browser(response)
        links = set()
        # a tag is located in td tag
        scraped_links = response.css('td a::attr(href)')
        for link in scraped_links:
            # get the id of the study from the link
            id = link.split('=')[1]
            links.add(
                f'https://ucalgary.sona-systems.com/exp_info_participant.aspx?experiment_id={id}')
        # run another function to get the details of each study
        return links
        # yield from response.follow_all(links, callback=self.get_details)

    def get_details(self, response):
        data = {}
        # open_in_browser(response)
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
            data[key] = value
        return data

if __name__ == '__main__':
    spider = ScrapeSpider()
    spider.start_requests()
