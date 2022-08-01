import smtplib
import ssl
from email.message import EmailMessage

def send(email_to, links):

    # Define email sender and receiver
    email_sender = 'open.seat.finder@gmail.com'
    email_password = 'dwlrbisufxnnneju'

    email_receiver = email_to

    # Set the subject and body of the email
    subject = 'New Research Participation Opportunities!'
    body = f"""
    Here are the links to the participation opportunities:
    {links.__str__()}
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
