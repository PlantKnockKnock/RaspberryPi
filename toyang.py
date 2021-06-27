import RPi.GPIO as GPIO
import time, datetime

Moisture_Pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Moisture_Pin, GPIO.IN)

def Sense(Moisture_Pin):
	timedate = datetime.datetime.now().strftime("%H:%M %Y-%m-%d ")
	if GPIO.input(Moisture_Pin):
		print("Dry - turn water on", timedate)
	else:
		print ("Wet-trun water off", timedate)
	return()

while True:
	Sense(Moisture_Pin)
	time.sleep(1)
