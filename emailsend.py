import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import statusicon
import csv

sender_email = "mrstoni78@gmail.com"
password = input('Enter Password')

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email


totalworkorder = "6"
escalatedsites = "10"
flaggedsites = "12"
callsinque = "45"
callsactive = "67"
callscomplted = "78"
notificationssent = "90"
notificationsfailed = "100"
# Create the plain-text and HTML version of your message
Status__ICON =''
if False:
    Status__ICON = statusicon.thumbsup
else:
    Status__ICON = statusicon.thumbsdown

text = """
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """<!DOCTYPE html>
<div style="width:97%;display:flex;border-style:  groove;box-shadow: inset 0 0 3px 1px black;background-color: white;">
  <div class="" style="width:70%;background-image: linear-gradient(smoke, white);display:block;padding:1%;">
    <center>
      <h1>TODAYS WORK STATUS</h1>
    </center>
    <br>

   <div style=" display: inline-block;width: 100%;border-style: double; background-image: linear-gradient(whit, white); ">
        <div style="margin: 3px;">
          <div style="display: inline-block;width: 40%;padding-top:10px;background-image: linear-gradient(gray, white);">
            <center>Total Work<br /> Order<br><h1>10</h1></center>
          </div>
          <div style="display: inline-block;width: 40%;padding-top:10px;background-image: linear-gradient(gray, white);">
            <center>Escalated <br />Sites<br><h1>10</h1></center>
          </div>
          <div style="display: inline-block;width: 40%;padding-top:10px;background-image: linear-gradient(gray, white);">
            <center>Flagged <br />Sites<br><h1>10</h1></center>
          </div>
          <div style="display: inline-block;width: 40%;padding-top:10px;background-image: linear-gradient(gray, white);">
            <center>Calls in<br /> Que<br><h1>100</h1></center>
          </div>
        </div>
      <br/>
    
        <div style="margin: 3px;">
          <div style="display: inline-block;width: 40%;padding-top:10px;background-image: linear-gradient(gray, white);">
            <center>Calls<br /> Active<br><h1>100</h1></center>
          </div>
          <div style="display: inline-block;width: 40%;padding-top:10px;background-image: linear-gradient(gray, white);">
            <center>Calls<br /> Completed<br><h1>100</h1></center>
          </div>
          <div style="display: inline-block;width: 40%;padding-top:10px;background-image: linear-gradient(gray, white);">
            <center>Notifications <br />Sent<br><h1>100</h1></center>
          </div>
          <div style="display: inline-block;width: 40%;padding-top:10px;background-image: linear-gradient(gray, white);">
            <center>Notifications<br /> Failed<br><h1>100</h1></center>
          </div>
        </div>
      
    </div>
  </div>
  <div 	class="" style="border-style: double;margin: 14px;width:30%;display:block;padding:1%;box-shadow: 0 0 4px black;background-color: white;">
    <center>
      <p style="margin-top:50%;">
        <img src="""+Status__ICON+""" width="150px" height="150px" alt="Good">
      </p>
    </center>
    <span>Today's progress determined by yesterday's choices </span>
  </div>
</div>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with open("contacts_file.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for name, email in reader:
        print(f"Sending email to {name}")
        receiver_email = email
        message["To"] = receiver_email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
