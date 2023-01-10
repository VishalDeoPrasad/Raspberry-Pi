import RPi.GPIO as GPIO

buzzerPin = 17
lb_sensor = 18

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(buzzerPin, GPIO.OUT) 
#GPIO.setup(piezo, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(lb_sensor, GPIO.IN)

try:
    while True:
        val = GPIO.input(lb_sensor)
        print("Light Blocking Sensor Value : ", val)
        if val == False:
            GPIO.output(buzzerPin, GPIO.HIGH)
             
        else :
            GPIO.output(buzzerPin, GPIO.LOW)
    
except KeyboardInterrupt: 
   print("Keyboard interrupt")

except:
   print("some error") 

finally:
   print("clean up") 
   GPIO.cleanup()


