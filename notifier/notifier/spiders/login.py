from scrapy import FormRequest, Spider, Request


class LoginSpider(Spider):
    # Define the database connection URL
    # settings = get_project_settings()
    # print(settings.get('DB_URL'))

    name = 'login'
    allowed_domains = ['ucalgary.sona-systems.com']
    urls = ['https://ucalgary.sona-systems.com/']
    
    def __init__(self, *args, **kwargs):
        super(LoginSpider, self).__init__(*args, **kwargs)
        # username and password are passed as arguments to the spider
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')

    def parse(self, response):
        # Get the CSRF token from the login form
        csrf_token = response.css(
            'input[name="csrf_token"]::attr(value)').get()

        # Login to the website
        yield FormRequest.from_response(response,
                                        formdata={
                                            'csrf_token': csrf_token,
                                            'ctl00$ContentPlaceHolder1$userid': self.username,
                                            'ctl00$ContentPlaceHolder1$pw': self.password,
                                            'ctl00$ContentPlaceHolder1$_default_auth_button': 'Log In'
                                        },
                                        callback=self.after_login
                                        )

    def after_login(self, response):
        # Check if the login was successful
        if "VIEW AVAILABLE STUDIES" in response.text:
            # If the login was successful, respond with true
            yield { 'success': True }
        else:
            # If the login was unsuccessful, respond with false
            yield { 'success': False }
        

if __name__ == '__main__':
    spider = LoginSpider()
    spider.logger.log("Starting Spider")
    spider.start_requests()
