import RPi.GPIO as GPIO
import time

ln1, ln2= 6, 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(ln1, GPIO.OUT)
GPIO.setup(ln2, GPIO.OUT)


try: 
	while True:
		GPIO.output(ln1, GPIO.LOW)
		time.sleep(2)
		GPIO.output(ln1, GPIO.HIGH)
		
		GPIO.output(ln2, GPIO.LOW)
		time.sleep(2)
		GPIO.output(ln2, GPIO.HIGH)
		
		
except KeyboardInterrupt: 
	print("KeyBoard Interrupt:")
	
except:
	print("Some Error")

finally:
	print("Cleaning UP:")
	GPIO.cleanup()

