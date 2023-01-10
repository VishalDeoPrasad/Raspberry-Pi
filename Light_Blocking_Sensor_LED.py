import RPi.GPIO as GPIO

LedPin = 22
lb_sensor = 18

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(LedPin, GPIO.OUT) 
#GPIO.setup(piezo, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(lb_sensor, GPIO.IN)

try:
    while True:
        val = GPIO.input(lb_sensor)
        print("Light Blocking Sensor Value : ", val)
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

