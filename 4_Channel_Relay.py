import RPi.GPIO as GPIO
import time

ln1, ln2, ln3, ln4 = 6, 13, 19, 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(ln1, GPIO.OUT)
GPIO.setup(ln2, GPIO.OUT)
GPIO.setup(ln3, GPIO.OUT)
GPIO.setup(ln4, GPIO.OUT)


try: 
	while True:
		GPIO.output(ln1, GPIO.LOW)
		time.sleep(2)
		GPIO.output(ln1, GPIO.HIGH)
		
		GPIO.output(ln2, GPIO.LOW)
		time.sleep(2)
		GPIO.output(ln2, GPIO.HIGH)
		
		GPIO.output(ln3, GPIO.LOW)
		time.sleep(2)
		GPIO.output(ln3, GPIO.HIGH)
		
		GPIO.output(ln4, GPIO.LOW)
		time.sleep(2)
		GPIO.output(ln4, GPIO.HIGH)
		
		
except KeyboardInterrupt: 
	print("KeyBoard Interrupt:")
	
except:
	print("Some Error")

finally:
	print("Cleaning UP:")
	GPIO.cleanup()

