#!/usr/bin/env python3
from config import fl_motor, fr_motor, bl_motor, br_motor
import motion
import time

def main():
	leftmotors = [fl_motor, bl_motor]
	rightmotors = [fr_motor, br_motor]
	dirselect = None
	tspeed = int(input("Running speed (0 - 100): "))
	movetime = int(input("Running time (sec): "))
	while (dirselect != 'q'):
		motion.stopdrive(motors = leftmotors + rightmotors)
		dirselect = input("Direction (w,a,s,d): ")
		if dirselect == 'w':
			motion.drive(leftmotors, rightmotors, tspeed)
		if dirselect == 'a':
			motion.drive(leftmotors, rightmotors, tspeed, -tspeed)
		if dirselect == 's':
			motion.drive(leftmotors, rightmotors, -tspeed)
		if dirselect == 'd':
			motion.drive(leftmotors, rightmotors, tspeed, tspeed)
		time.sleep(movetime)


if __name__ == "__main__":
	main()