#!/usr/bin/env python
from time import sleep
from subprocess import call
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import os

def TakeStills(n):
	if (lowCount > n):  # 6000 milliseconds in 30 mins
		call("raspistill -o /home/pi/Sensor/stills/img%01d.jpg -t 10000 -tl 1000 -q 50 -w 800 -h 600", shell=True)
		call("zip -j thumbsZip /home/pi/Sensor/stills/thumbnails/*",shell=True)

def ConvertThumbs(n):
	sleep(5)
	call("convert -define jpeg:size=500x180 stills/*.jpg -auto-orient -thumbnail 300x -unsharp 0x.5 stills/thumbnails/thumbs0%d.jpg", shell=True)

USERNAME = "ivyleavedtoadflax@gmail.com"
PASSWORD = "cdunxqfmuysysrls"
	
def sendMail(to, subject, text, files=[]):

#	assert type(to)==list
#	assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    
    msg.attach( MIMEText(text) )

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'
                       % os.path.basename(file))
        msg.attach(part)

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo_or_helo_if_needed()
	server.starttls()
	server.ehlo_or_helo_if_needed()
	server.login(USERNAME,PASSWORD)
	server.sendmail(USERNAME, to, msg.as_string())
	server.quit()

# sendMail(["matt.upson@btinternet.com"],
# sendMail(["m.perezortola@gmail.com"],
	# "Camera Triggered",
	# "Bla",
	# ["/home/pi/Sensor/stills/thumbnails/thumbs00.jpg",
	# "/home/pi/Sensor/stills/thumbnails/thumbs01.jpg",
	# "/home/pi/Sensor/stills/thumbnails/thumbs02.jpg",
	# "/home/pi/Sensor/stills/thumbnails/thumbs03.jpg",
	# "/home/pi/Sensor/stills/thumbnails/thumbs04.jpg",
	# "/home/pi/Sensor/stills/thumbnails/thumbs05.jpg",
	# "/home/pi/Sensor/stills/thumbnails/thumbs06.jpg",
	# "/home/pi/Sensor/stills/thumbnails/thumbs07.jpg",
	# "/home/pi/Sensor/stills/thumbnails/thumbs08.jpg",
	# "/home/pi/Sensor/stills/thumbnails/thumbs09.jpg",
	# "/home/pi/Sensor/stills/thumbnails/thumbs10.jpg"])