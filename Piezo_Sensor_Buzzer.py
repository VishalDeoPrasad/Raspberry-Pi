import RPi.GPIO as GPIO

buzzerPin = 21
piezo = 26

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(buzzerPin, GPIO.OUT) 
#GPIO.setup(piezo, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(piezo, GPIO.IN)

try:
    while True:
        val = GPIO.input(piezo)
        print("Piezo Sensor Value : ", val)
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


