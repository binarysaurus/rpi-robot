#!/usr/bin/env python3
import motion

# front Left motor GPIO pins
fl_fp = 2
fl_bp = 3
fl_sp = 4

# front Right motor GPIO pins
fr_fp = 5
fr_bp = 6
fr_sp = 13

# Back Left motor GPIO pins
bl_fp = 10
bl_bp = 9
bl_sp = 11

# Back Right motor GPIO pins
br_fp = 17
br_bp = 27
br_sp = 22

# Motor pins set
fl_motor = motion.Motor(fl_fp, fl_bp, fl_sp, False)
fr_motor = motion.Motor(fr_fp, fr_bp, fr_sp, True)
bl_motor = motion.Motor(bl_fp, bl_bp, bl_sp, False)
br_motor = motion.Motor(br_fp, br_bp, br_sp, True)


dirselect = None