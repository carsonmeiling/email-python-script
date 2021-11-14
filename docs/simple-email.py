import smtplib, ssl

smtp_server = 'smtp.gmail.com'
port = 465 
password = input('Enter email password and press enter: ')

sender_email = 'mcar8131@gmail.com'
receiver_email = 'carmc93@gmail.com'

for i in range(2):
    
  message = """ Time to blow up your email. 
  The list goes on."""

  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

