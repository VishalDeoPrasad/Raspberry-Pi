import RPi.GPIO as GPIO

LedPin = 21
switchPin = 26

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(LedPin, GPIO.OUT) 
GPIO.setup(switchPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(switchPin) == False:
            GPIO.output(LedPin, GPIO.HIGH)
             
        else :
            GPIO.output(LedPin, GPIO.LOW)
    
except KeyboardInterrupt: 
   print("Keyboard interrupt")

except:
   print("some error") 

finally:
   print("clean up") 
   GPIO.cleanup()

