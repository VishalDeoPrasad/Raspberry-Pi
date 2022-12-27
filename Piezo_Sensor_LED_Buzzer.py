import RPi.GPIO as GPIO

LedPin = 20
piezo = 26
buzzerPin = 21

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(LedPin, GPIO.OUT)
GPIO.setup(buzzerPin, GPIO.OUT) 
#GPIO.setup(piezo, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(piezo, GPIO.IN)

try:
    while True:
        val = GPIO.input(piezo)
        print("Piezo Sensor Value : ", val)
        if val == False:
            GPIO.output(LedPin, GPIO.HIGH)
            GPIO.output(buzzerPin, GPIO.HIGH)
             
        else :
            GPIO.output(LedPin, GPIO.LOW)
            GPIO.output(buzzerPin, GPIO.LOW)
    
except KeyboardInterrupt: 
   print("Keyboard interrupt")

except:
   print("some error") 

finally:
   print("clean up") 
   GPIO.cleanup()


