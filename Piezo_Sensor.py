import RPi.GPIO as GPIO

piezo = 26

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
#GPIO.setup(piezo, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(piezo, GPIO.IN)

try:
    while True:
        val = GPIO.input(piezo)
        print("Piezo Sensor Value : ", val)
    
except KeyboardInterrupt: 
   print("Keyboard interrupt")

except:
   print("some error") 

finally:
   print("clean up") 
   GPIO.cleanup()

