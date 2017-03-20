#!/usr/bin/env python3
from config import fl_motor, fr_motor, bl_motor, br_motor, dirselect
import motion
import time

def main():
	dirselect = None
	tspeed = input("Running speed (0 - 100): ")
	movetime = input("Running time (sec): ")
	while (dirselect != 'q'):
		motion.stopdrive(fl_motor, fr_motor, bl_motor, br_motor)
		dirselect = input("Direction (w,a,s,d): ")
		if dirselect == 'w':
			motion.drive(fl_motor, fr_motor, bl_motor, br_motor, tspeed, 1)
		if dirselect == 'a':
			motion.drive(fl_motor, fr_motor, bl_motor, br_motor, tspeed, 1, -tspeed)
		if dirselect == 's':
			motion.drive(fl_motor, fr_motor, bl_motor, br_motor, tspeed, -1)
		if dirselect == 'd':
			motion.drive(fl_motor, fr_motor, bl_motor, br_motor, tspeed, 1, tspeed)
		time.sleep(movetime)


if __name__ == "__main__":
	main()