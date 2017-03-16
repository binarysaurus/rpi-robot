import move as mv
import time

FL = mv.motor(2, 3, 4, 1)
FR = mv.motor(5, 6, 13, -1)
BL = mv.motor(10, 9, 11, 1)
BR = mv.motor(17, 27, 22, -1)


def moveall(FL, FR, BL, BR, speed, dir):
	FL.move(speed, 1)
	BL.move(speed, 1)
	FR.move(speed, 1)
	BR.move(speed, 1)

for i in range(100):
	moveall(FL, FR, BL, BR, i, 1)
	print("Motors operating at %d%%\n", i)
	time.sleep(0.7)

FL.halt(exitstop=True)
FR.halt(exitstop=True)
BL.halt(exitstop=True)
BR.halt(exitstop=True)