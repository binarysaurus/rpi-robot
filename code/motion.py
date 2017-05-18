import RPi.GPIO as GPIO
from math import sqrt

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor(object):
    def __init__(self, forwardpin, backwardpin, speedpin, invertdir = False):
    	self.forwardpin = forwardpin
    	self.backwardpin = backwardpin
    	self.speedpin = speedpin
    	self.invertdir = -1 if invertdir else 1
    	GPIO.setup(self.forwardpin, GPIO.OUT)
    	GPIO.setup(self.backwardpin, GPIO.OUT)
    	GPIO.setup(self.speedpin, GPIO.OUT)
    	self.pwm = GPIO.PWM(speedpin, 50)
    	self.pwm.start(50)
    	self.halt()

    def move(self, speed, turn):
    	assert abs(speed) <= 100, "Duty cycle cannot exceed 100%!"
    	assert abs(turn) <= 1, "Turning range -1 to 1!"

    	if turn == 0:
    		turn = 1
    	
    	if turn * speed * self.invertdir >= 0:
    		GPIO.output(self.forwardpin, GPIO.HIGH)
    		GPIO.output(self.backwardpin, GPIO.LOW)
    	else:
    		GPIO.output(self.forwardpin, GPIO.LOW)
    		GPIO.output(self.backwardpin, GPIO.HIGH)
    	self.pwm.ChangeDutyCycle(abs(int(speed*turn)))

    def halt(self):
    	GPIO.output(self.forwardpin, GPIO.LOW)
    	GPIO.output(self.backwardpin, GPIO.LOW)

def drive(leftmotors, rightmotors, speed, turn = 0):
    # Assert based on simplification of |A-B| <= C, |A+B|<=C, 
    # bug: Assert will pass if A||B = 0 since B||A may exceed 100 independently
    #assert sqrt(abs(4*speed*turn)) <= 100, "Duty cycle cannot exceed 100%!"

    for left in leftmotors: 
    	left.move(speed, turn) 
    
    for right in rightmotors: 
    	right.move(speed, -turn) 

def stopdrive(motors):
    for motor in motors:
    	motor.halt()
