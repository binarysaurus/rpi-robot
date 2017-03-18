#!/usr/bin/env python3
from config import fl_motor, fr_motor, bl_motor, br_motor
import motion
import time

tspeed = 30
dirselect = None
movetime = 1.0

while (dirselect != 'q'):
	dirselect = input("Direction (w,a,s,d): ")
	motion.halt(fl_motor, fr_motor, bl_motor, br_motor)
	if dirselect == 'w':
		moveall(fl_motor, fr_motor, bl_motor, br_motor, tspeed, 1)
	if dirselect == 'a':
		moveall(fl_motor, fr_motor, bl_motor, br_motor, tspeed, 1, -tspeed)
	if dirselect == 's':
		moveall(fl_motor, fr_motor, bl_motor, br_motor, tspeed, -1)
	if dirselect == 'd':
		moveall(fl_motor, fr_motor, bl_motor, br_motor, tspeed, 1, tspeed)
	time.sleep(movetime)
