import RPi.GPIO as GPIO

LedPin = 21
buttonPin = 17

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(LedPin, GPIO.OUT) 
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(buttonPin) == False:
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
