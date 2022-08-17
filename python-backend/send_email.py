import smtplib
import ssl
from email.message import EmailMessage

def send(email_to, links):
    studies = ""
    for data in links:
        studies+=f"""
<h3>{data['title']}</h3>
<h5>{data['description']}
<h5>Worth: {data['credits']}
<br/>
Duration: {data['duration']}
<br/>
Location: {data['location']}</h5>
<a href="{data['link']}"><button>Check it out</button></a>
<hr>
"""


    # Define email sender and receiver
    email_sender = 'open.seat.finder@gmail.com'
    email_password = 'dwlrbisufxnnneju'

    email_receiver = email_to
    
    # Set the subject and body of the email
    subject = 'New Research Participation Opportunities!'
    len_links = len(links)
    is_or_are = 'is' if len_links == 1 else 'are'
    opportunity = 'opportunity' if len_links == 1 else 'opportunities'
    body = f"""
<html>
    <body>
    <p>
    Good news! there {is_or_are} {len_links} new research {opportunity}!
    </p>
    {studies}
  </body>
</html>
"""

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    # em.set_content(body)
    em.add_alternative(body, subtype='html')

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
