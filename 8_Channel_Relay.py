import RPi.GPIO as GPIO
import time

ln1, ln2, ln3, ln4, ln5, ln6, ln7, ln8 = 6, 13, 19, 26, 12, 16, 20, 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ln1, GPIO.OUT)
GPIO.setup(ln2, GPIO.OUT)
GPIO.setup(ln3, GPIO.OUT)
GPIO.setup(ln4, GPIO.OUT)
GPIO.setup(ln5, GPIO.OUT)
GPIO.setup(ln6, GPIO.OUT)
GPIO.setup(ln7, GPIO.OUT)
GPIO.setup(ln8, GPIO.OUT)


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
		
		GPIO.output(ln5, GPIO.LOW)
		time.sleep(2)
		GPIO.output(ln5, GPIO.HIGH)
		
		GPIO.output(ln6, GPIO.LOW)
		time.sleep(2)
		GPIO.output(ln6, GPIO.HIGH)
		
		GPIO.output(ln7, GPIO.LOW)
		time.sleep(2)
		GPIO.output(ln7, GPIO.HIGH)
		
		GPIO.output(ln8, GPIO.LOW)
		time.sleep(2)
		GPIO.output(ln8, GPIO.HIGH)
		
		
except KeyboardInterrupt: 
	print("KeyBoard Interrupt:")
	
except:
	print("Some Error")

finally:
	print("Cleaning UP:")
	GPIO.cleanup()


