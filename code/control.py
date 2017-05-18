#!/usr/bin/env python3
from config import fl_motor, fr_motor, bl_motor, br_motor
import motion
import time
import curses


def main():
    
    leftmotors = [fl_motor, bl_motor]
    rightmotors = [fr_motor, br_motor]
    dirselect = None
    tspeed = float(input("Running speed (0 - 100): "))
    #movetime = float(input("Running time (sec): "))
    movetime = 0.03

    stdscr = curses.initscr()
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(1)
    stdscr.addstr(0,10, "Enter w, a, s, d, to move")
    stdscr.addstr(1,10, "Enter 'q' to quit\n\n")
    stdscr.refresh()
    
    while (dirselect != ord('q')):
        motion.stopdrive(motors = leftmotors + rightmotors)
        dirselect = stdscr.getch()
        stdscr.refresh()

        if dirselect == ord('w'):
            motion.drive(leftmotors, rightmotors, tspeed)
        if dirselect == ord('a'):
            motion.drive(leftmotors, rightmotors, tspeed, -tspeed)
        if dirselect == ord('s'):
            motion.drive(leftmotors, rightmotors, -tspeed)
        if dirselect == ord('d'):
            motion.drive(leftmotors, rightmotors, tspeed, tspeed)
        
        time.sleep(movetime)

    curses.endwin()


if __name__ == "__main__":
    main()