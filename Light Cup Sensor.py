import RPi.GPIO as GPIO

LedPin = 18
lc_sensor = 25

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(LedPin, GPIO.OUT) 
GPIO.setup(lc_sensor, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(lc_sensor, GPIO.IN)

try:
    while True:
        val = GPIO.input(lc_sensor)
        print("Piezo Sensor Value : ", val)
        if val == False:
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

