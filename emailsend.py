import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import statusicon

sender_email = "mrstoni78@gmail.com"
receiver_email = "theju.mrss123@gmail.com"
password = input('Enter Password')

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

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
<html>
<head>
<title>Bootstrap Icons</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
</head>
<body class="container">
<div style="width:97%;display: inline-flex;border-style:  groove;box-shadow: inset 0 0 3px 1px black;background-color: white;"> 
    <div style="width:70%;background-image: linear-gradient(smoke, white);/* border-style: double; */display:block;padding:1%;">
    
    <center><h1>TODAYS WORK STATUS</h1></center>
    <br>
   
    <div style=" display: inline-block;
      width: 96%;
      border-style: double;  
      background-image: linear-gradient(whit, white); ">
      <center>
        <div style="margin: 3px;">
        <div style="
        display: inline-block;
        width: 24%;
        padding-top:10px;
        background-image: linear-gradient(gray, white);
        "><center>Total Work<br/> Order<br><h1>"""+totalworkorder+"""</h1></center></div>
        <div style="
        display: inline-block;
        width: 24%;
        padding-top:10px;
        background-image: linear-gradient(gray, white);
        "><center>Escalated <br/>Sites<br><h1>"""+escalatedsites+"""</h1></center></div>
        <div style="
        display: inline-block;
        width: 24%;
        padding-top:10px;
        background-image: linear-gradient(gray, white);
        "><center>Flagged <br/>Sites<br><h1>"""+flaggedsites+"""</h1></center></div>
        <div style="
        display: inline-block;
        width: 24%;
        padding-top:10px;
        background-image: linear-gradient(gray, white);
        "><center>Calls in<br/> Que<br><h1>"""+callsinque+"""</h1></center></div>
</div>
</center>
<br/>
<center>
    <div style="margin: 3px;">
    <div style="
    display: inline-block;
    width: 24%;
    padding-top:10px;
    background-image: linear-gradient(gray, white);
    "><center>Calls<br/> Active<br><h1>"""+callsactive+"""</h1></center></div>
    <div style="
    display: inline-block;
    width: 24%;
    padding-top:10px;
    background-image: linear-gradient(gray, white);
    "><center>Calls<br/> Completed<br><h1>"""+callscomplted+"""</h1></center></div>
    <div style="
    display: inline-block;
    width: 24%;
    padding-top:10px;
    background-image: linear-gradient(gray, white);
    "><center>Notifications <br/>Sent<br><h1>"""+notificationssent+"""</h1></center></div>
    <div style="
    display: inline-block;
    width: 24%;
    padding-top:10px;
    background-image: linear-gradient(gray, white);
    "><center>Notifications<br/> Failed<br><h1>"""+notificationsfailed+"""</h1></center></div>
    </div>
</center>
      </div>
    </div>
     <div style="border-style: double;margin: 14px;width:30%;display:block;padding:1%;/* border: 1px solid; */box-shadow: 0 0 4px black;background-color: white;">
     <center>
            <p style="margin-top:50%;">
            <img src="""+Status__ICON+""" width="150px" height="150px" alt="Good">
            </p>
            </center>
     <span>Today's progress determined by yesterday's choices </span>
    </div>
    </div>
    </body>
    </html>
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
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )