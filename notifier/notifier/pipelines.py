# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import smtplib
import ssl
from email.message import EmailMessage


from sqlalchemy import text

class NotifierPipeline:
    # with the items we get from the spider, I want to send an email with the data
    def __init__(self):
        self.email_sender = 'open.seat.finder@gmail.com'
        self.email_password = 'dwlrbisufxnnneju'

    def send_email(self, email_receiver, subject, body):
        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        # em.set_content(body)
        em.add_alternative(body, subtype='html')
        
        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, email_receiver, em.as_string())
        
    def send_sub_email(self, email_to, data):
        subject = 'New Research Participation Opportunities!'
        studies = ""
        body_template = """
<html>
  <head>
    <style>
        h2,
        dt {
            font-weight: bold;
        }

        dl,
        dd {
            font-size: 0.9rem;
        }

        dd {
            margin-bottom: 1em;
        }
        button {
            border-radius: 0.375rem;
            padding-top: 0.625rem;
            padding-bottom: 0.625rem;
            padding-left: 0.875rem;
            padding-right: 0.875rem;
            font-size: 0.875rem;
            line-height: 1.25rem;
            font-weight: 600;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            background-color: #f14;
            color: #fff;
        }
        button:hover {
            background-color: #e00;
        }
        button:active {
            background-color: #c00;
        }
    </style>
  </head>
  <body>
    <h1>
    Good news! there %s %s new research %s!
    </h1>
    %s
    <p>
    You will be automatically unsubscribed and your credentials will be erased from our database when the course ends. Nevertheless, <a href="https://open-seat-notifier.vercel.app/api/delete/%s">click here
    </a> if you would like to unsubscribe now </p>
  </body>
</html>
"""
        
        # for each study, make a description list
        for study in data:
            for index, (key, value) in enumerate(study.items()):
                if index == 1:
                    studies += f"<h2>{value}</h2><dl>"
                elif index > 1:
                    if key == 'link':
                        studies += f"<a href='{value}'><button>Check it out</button></a>"
                    else:
                        # description list element
                        studies += f"""
<dt>{key}</dt>
<dd>{value}</dd>
"""

            studies += "</dl><hr>"
            # add the study id to the notified list
            query = text("UPDATE main SET notified_studies = array_append(notified_studies, :new_id)")
            self.session.execute(query, {'new_id': study['id']})
        # commit the changes to the database
        self.session.commit()

        email_receiver = email_to
        len_links = len(data)
        is_or_are = 'is' if len_links == 1 else 'are'
        opportunity = 'opportunity' if len_links == 1 else 'opportunities'
        body = body_template % (is_or_are, len_links, opportunity, studies, email_receiver)
        
        self.send_email(email_receiver, subject, body)
        
    def send_unsub_email(self, email_to):
        email_receiver = email_to
        subject = 'Incorrect Credentials for Sona Research Participation'
        body = """
<html>
  <body>
    <p>
    The credentials you provided for the Sona Research Participation website are incorrect. Your data has been erased from our database. If you would like to subscribe again, please visit <a href="https://open-seat-notifier.vercel.app/">Open Seat Notifier</a> and enter your correct credentials.
    </p>
    <p>
    We apologize for the inconvenience.
    </p>
  </body>
</html>
"""
        # delete the user from the database
        # query = text("DELETE FROM main WHERE email = :email")
        row_to_delete = self.session.query('main').filter_by(email=email_receiver).first()
        self.session.delete(row_to_delete)
        
        self.send_email(email_receiver, subject, body)
        

    
    def process_item(self, item, spider):
        if spider.name == 'login': 
            self.end(item)
        data = item['data']
        if len(data) == 0: # if there are no new studies, don't send an email
            self.end(item)
        self.session = item['session']
        # if there are new studies, send an email
        self.send_sub_email(item['email'], data) if not (item['error'] == 'Login failed') else self.send_unsub_email(item['email'])

        self.end(item)

    def end(self,item):
        self.session.close() if self.session else None
        return item
