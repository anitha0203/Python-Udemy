import smtplib
from email.message import EmailMessage

email = EmailMessage()

email_content = '''Dear madam,
 How are you?
'''

email['Subject'] = 'Test email'
email['From'] = 'anithaboppidi@gmail.com'
email['To'] = 'anithaboppidi@gmail.com'

email.set_content(email_content)

smtp_connector = smtplib.SMTP(host="smtp.gmail.com", port=587)
smtp_connector.starttls()
smtp_connector.login('anithaboppidi@gmail.com', 'password')

smtp_connector.send_message(email)
smtp_connector.quit()
