import move as mv
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


FL = mv.motor(2, 3, 4, 1)
#FR = 
#BL = 
#BR = 

FL.move(60, 1)
time.sleep(10)
FL.halt(exitstop=True)