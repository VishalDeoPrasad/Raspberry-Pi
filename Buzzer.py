import RPi.GPIO as GPIO
import time

led = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

try: 
	while True:
		GPIO.output(led, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(led, GPIO.LOW)
		time.sleep(0.5)
		
except KeyboardInterrupt: 
	print("KeyBoard Interrupt:")
	
except:
	print("Some Error")

finally:
	print("Cleaning UP:")
	GPIO.cleanup()
