from gpiozero import Servo
from time import sleep
import RPi.GPIO as GPIO
 
servo1Pin=26
GPIO.setmode(GPIO.BCM)

servo1 = Servo(servo1Pin)
print("Rassberry Pi Servo"); 
try: 
    while True:
        print("max")
        servo1.max()
        sleep(0.5)
        
        print("mid")
        servo1.mid()
        sleep(0.5)
        
        print("min")
        servo1.min()
        sleep(0.5)
        
        print("mid")
        servo1.mid()
        sleep(0.5)
        
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt")

except:
   print("some error") 

finally:
   print("clean up") 
   GPIO.cleanup()

