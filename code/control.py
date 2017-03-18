import move as mv
import time
import tkinter as tk

FL = mv.motor(2, 3, 4, 1)
FR = mv.motor(5, 6, 13, -1)
BL = mv.motor(10, 9, 11, 1)
BR = mv.motor(17, 27, 22, -1)


def moveall(FL, FR, BL, BR, speed, dir, turn = 0):
	
	FL.move(speed + turn, dir)
	BL.move(speed + turn, dir)
	FR.move(speed - turn, dir)
	BR.move(speed - turn, dir)

#inputpwm = int(input("Input PWM: "))
#direction = int(input("Input dir: "))

 
#moveall(FL, FR, BL, BR, inputpwm, direction)
#time.sleep(5)
x = 2
tm = 1
spd = 30
while (x != 'q'):
	x = input("direction?")
	if x == 'w':
		moveall(FL, FR, BL, BR, spd, 1, 0)
	if x == 'a':
		moveall(FL, FR, BL, BR, spd, 1, -spd)
	if x == 's':
		moveall(FL, FR, BL, BR, spd, -1, 0)
	if x == 'd':
		moveall(FL, FR, BL, BR, spd, 1, spd)
	time.sleep(tm)

#for i in range(100):
#	moveall(FL, FR, BL, BR, i, 1)
#	print("Motors operating at ", i, "%", sep="")
#	time.sleep(0.7)

FL.halt(exitstop=True)
FR.halt(exitstop=True)
BL.halt(exitstop=True)
BR.halt(exitstop=True)
