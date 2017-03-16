import move as mv
import time

FL = mv.motor(2, 3, 4, 1)
#FR = 
#BL = 
#BR = 
for i in range(100):
	FL.move(i, 1)
	time.sleep(0.7)
	
FL.halt(exitstop=True)