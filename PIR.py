##!/usr/bin/python

########### 

import RPi.GPIO as GPIO
from time import sleep
from time import strftime
from LEDinit import LEDinit

# Use Broadcom chip reference for GPIO
GPIO.setmode(GPIO.BCM)

# Suppress channel already in use warning
GPIO.setwarnings(False)

# name pins

pin5 = 21

# Setup outputs
GPIO.setup(pin5, GPIO.IN)

highCount = 0
lowCount = 0

print("Initialising PIR")

print("45 seconds...")
sleep(25)
print("20 seconds...")
sleep(20)

print("5 seconds...")
print("PIR initialised")


while True: 
	if (GPIO.input(pin5) == GPIO.HIGH):
		if lowCount > 0:
			timestamp = strftime("%Y-%m-%d,%H:%M:%S")
			PIRlog = open("/home/pi/Sensor/PIRLog.csv", "a")
			PIRlog.write("\n" + timestamp + "," + "LOW" + "," + str(lowCount))
			PIRlog.close()
		if (lowCount > 50):  # 18000 milliseconds in 30 mins
			call("raspistill -o /home/pi/Sensor/stills/timestamp.jpg -t 0", shell=True)
		lowCount = 0
		PIRState = open("/home/pi/Sensor/PIRState", "w")
		PIRState.write("1")
		PIRState.close()
		highCount += 0.1
		sleep(0.1)	
	else:
		if highCount > 0:
			timestamp = strftime("%Y-%m-%d,%H:%M:%S")
			PIRlog = open("/home/pi/Sensor/PIRLog.csv", "a")
			PIRlog.write("\n" + timestamp + "," + "HIGH" + "," + str(highCount))
			PIRlog.close()
		highCount = 0
		#Commented out below so that sensor.py returns writes to PIRState instead.
		#PIRState = open("/home/pi/Sensor/PIRState", "w")
		#PIRState.write("0")
		#PIRState.close()
		lowCount += 0.1
		sleep(0.1)
		
