import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class motor(object):
    def __init__(self, for_pin, bac_pin, speed_pin, reversed):
    	self.for_pin = for_pin
    	self.bac_pin = bac_pin
    	self.speed_pin = speed_pin
    	self.reversed = reversed
    	GPIO.setup(self.for_pin, GPIO.OUT)
    	GPIO.setup(self.bac_pin, GPIO.OUT)
    	GPIO.setup(self.speed_pin, GPIO.OUT)

    def move(self, speed, direction):
    	if reversed:
    		direction = -direction
    	GPIO.output(self.for_pin,)

    def halt(self):
    	GPIO.output(self.for_pin, 0)
    	GPIO.output(self.bac_pin, 0)
    	GPIO.output(self.speed_pin, 0)


"""
left1 = motor(1, 2, 3, False)
left2 = motor(4, 5, 6, False)
right1 = motor(7, 8, 9, False)
right2 = motor(10, 11, 12, False)

def movemotors(l1, l2, r1, r2, speed, dir):
	l1.move(speed, dir)
	l2.move(speed, dir)
	r1.move(speed, dir)
	r2.move(speed, dir)

def main:
	while i in range(100):
		movemotors(l1, l2, r1, r2, i, i)

"""