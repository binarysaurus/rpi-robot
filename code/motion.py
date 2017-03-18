#!/usr/bin/env python3
import RPi.GPIO as GPIO

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
    	self.halt(self)

    def move(self, speed, direction):
    	if direction * self.invertdir >= 0:
    		GPIO.output(self.forwardpin, GPIO.HIGH)
    		GPIO.output(self.backwardpin, GPIO.LOW)
    	else:
    		GPIO.output(self.forwardpin, GPIO.LOW)
    		GPIO.output(self.backwardpin, GPIO.HIGH)
    	self.pwm.ChangeDutyCycle(speed)

    def halt(self):
    	GPIO.output(self.forwardpin, GPIO.LOW)
    	GPIO.output(self.backwardpin, GPIO.LOW)

def drive(fl_motor, fr_motor, bl_motor, br_motor, speed, dir, turn = 0):
    assert(abs(speed - turn) <= 100, "Duty cycle cannot exceed 100%!")
    assert(abs(speed + turn) <= 100, "Duty cycle cannot exceed 100%!")
    fl_motor.move(abs(speed + turn), dir)
    fr_motor.move(abs(speed + turn), dir)
    bl_motor.move(abs(speed - turn), dir)
    br_motor.move(abs(speed - turn), dir)

def stopdrive(fl_motor, fr_motor, bl_motor, br_motor):
    fl_motor.halt()
    fr_motor.halt()
    bl_motor.halt()
    br_motor.halt()