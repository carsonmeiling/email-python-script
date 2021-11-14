import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from get_random_pic import get_image

sender_email = "sender@gmail.com"
receiver_email = "receive@gmail.com"
password = input("Type your password and press enter:")
# returns image URL from get_random_pic
image = get_image()

message = MIMEMultipart("alternative")
message["Subject"] = "Calling all Notre Damians"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
I hope you like puppies
"""
html = """\
<html>
  <body>
    <p>What's up Bry?<br>
       This was meant to send you a bunch of random pictures, but the img won't render. So now, it will just blow up your email.<br>
    </p>
    <p>Email ??? of ??? </p>
    <br>
    <br>
    <br>
    <br>
    <p>Carson </p>

  </body>
</html>
""" 
      #  <a href='{image}'> Click Here<a>
      #  <img href="{image}" alt='whatever pic'</img> 
# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
for i in range(101):
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(
          sender_email, receiver_email, message.as_string()
      )