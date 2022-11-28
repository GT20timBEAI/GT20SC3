import smtplib
import ssl
from services.template import templateHTML
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

def sendOrderEmail(username, price, emailuser):
    email_sender = 'gt20sc3@gmail.com'
    email_password = 'vmrhsyyzuznzeqxh'
    email_receiver = emailuser

    date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

    subject = f'Your Fashion Campuss Order {date_str}'
    body = templateHTML(username, price)

    em = MIMEMultipart()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject

    # Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
    em.attach(MIMEText(body, "html"))

    contect = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contect) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

