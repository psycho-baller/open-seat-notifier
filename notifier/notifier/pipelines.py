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
        self.subject = 'New Research Participation Opportunities!'
        self.body_template = """
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
        
    def process_item(self, item, spider):
        if spider.name == 'login':
            return item
        data = item['data']
        if len(data) == 0: # if there are no new studies, don't send an email
            return item
        # if there are new studies, send an email
        session = item['session']
        studies = ""
        
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
            session.execute(query, {'new_id': study['id']})
        # commit the changes to the database
        session.commit()
        session.close()

        email_receiver = item['email']
        len_links = len(data)
        is_or_are = 'is' if len_links == 1 else 'are'
        opportunity = 'opportunity' if len_links == 1 else 'opportunities'
        body = self.body_template % (is_or_are, len_links, opportunity, studies, email_receiver)
        
        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = email_receiver
        em['Subject'] = self.subject
        # em.set_content(body)
        em.add_alternative(body, subtype='html')
        
        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, email_receiver, em.as_string())

        return item
