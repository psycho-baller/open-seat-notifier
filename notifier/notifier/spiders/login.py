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
        self.start_requests()

    def parse(self, response, username, password):
        # Get the CSRF token from the login form
        csrf_token = response.css(
            'input[name="csrf_token"]::attr(value)').get()

        # Login to the website
        yield FormRequest.from_response(response,
                                        formdata={
                                            'csrf_token': csrf_token,
                                            'ctl00$ContentPlaceHolder1$userid': username,
                                            'ctl00$ContentPlaceHolder1$pw': password,
                                            'ctl00$ContentPlaceHolder1$_default_auth_button': 'Log In'
                                        },
                                        callback=self.after_login
                                        )

   
        

if __name__ == '__main__':
    spider = LoginSpider()
    spider.logger.log("Starting Spider")
    spider.start_requests()
