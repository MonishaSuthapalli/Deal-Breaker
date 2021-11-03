import smtplib

from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('Email sending example using Python. It\'s Simple Text Message')

fromEmail = 'hollandislou@gmail.com'
toEmail = 'monishasuthapalli688@gmail.com'

msg['Subject'] = 'Simple Text Message'
msg['From'] = fromEmail
msg['To'] = toEmail

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login('hollandislou@gmail.com', 'bhashyam')
s.send_message(msg)
s.quit()
