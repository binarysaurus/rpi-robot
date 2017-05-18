import motion
import sensors

### DRIVE PINS ### 

# front Left motor GPIO pins
fl_fp = 5
fl_bp = 6
fl_sp = 13

# front Right motor GPIO pins
fr_fp = 10
fr_bp = 9
fr_sp = 11

# Back Left motor GPIO pins
bl_fp = 2
bl_bp = 3
bl_sp = 4

# Back Right motor GPIO pins
br_fp = 17
br_bp = 27
br_sp = 22

# Motor pins set
fl_motor = motion.Motor(fl_fp, fl_bp, fl_sp, False)
fr_motor = motion.Motor(fr_fp, fr_bp, fr_sp, True)
bl_motor = motion.Motor(bl_fp, bl_bp, bl_sp, False)
br_motor = motion.Motor(br_fp, br_bp, br_sp, True)

### SENSOR PINS ###

# Range Finder 1
trig1 = 26 
echo1 = 19

# URange Finder pins set
urf1 = sensors.RangeFinder(trig1, echo1)