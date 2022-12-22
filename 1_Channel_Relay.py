import RPi.GPIO as GPIO
import time

ln1= 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(ln1, GPIO.OUT)


try: 
	while True:
		GPIO.output(ln1, GPIO.LOW)
		time.sleep(2)
		GPIO.output(ln1, GPIO.HIGH)
		time.sleep(2)
		
		
except KeyboardInterrupt: 
	print("KeyBoard Interrupt:")
	
except:
	print("Some Error")

finally:
	print("Cleaning UP:")
	GPIO.cleanup()

