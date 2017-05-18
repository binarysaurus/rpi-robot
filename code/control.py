#!/usr/bin/env python3
from config import fl_motor, fr_motor, bl_motor, br_motor, urf1
import motion
import time
import curses


def main():
    
    motors = [fl_motor, fr_motor, bl_motor, br_motor]
    dirselect = None
    tspeed = float(input("Running speed (0 - 100): "))
    tradius = float(input("Turn (0 to 1): "))
    movetime = 0.03

    stdscr = curses.initscr()
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(1)
    stdscr.addstr(0,10, "Enter w, a, s, d, to move")
    stdscr.addstr(1,10, "Enter 'q' to quit\n\n")

    stdscr.refresh()
    
    while (dirselect != ord('q')):
        
        stdscr.addstr(2,10, "Current distance: %d\n\n" % urf1.getdistance())
        motion.stopdrive(motors = motors)

        dirselect = stdscr.getch()
        stdscr.refresh()

        if dirselect == ord('w'):
            motion.drive(motors, tspeed)
        if dirselect == ord('a'):
            motion.drive(motors, tspeed, -tradius)
        if dirselect == ord('s'):
            motion.drive(motors, -tspeed)
        if dirselect == ord('d'):
            motion.drive(motors, tspeed, tradius)
        
        time.sleep(movetime)

    curses.endwin()


if __name__ == "__main__":
    main()