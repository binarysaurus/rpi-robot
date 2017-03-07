from ast import literal_eval
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class motors(object):
    def __init__(self, FL_pin, FR_pin, BL_pin, BR_pin):
    	self.FL_pin = FL_pin
    	self.FR_pin = FR_pin
    	self.BL_pin = BL_pin
    	self.BR_pin = BR_pin
    	GPIO.setup(self.FL_pin, GPIO.OUT)
    	GPIO.setup(self.FR_pin, GPIO.OUT)
    	GPIO.setup(self.BL_pin, GPIO.OUT)
    	GPIO.setup(self.BR_pin, GPIO.OUT)

    def move(self, speed, direction):


    def halt(self):
    	







motor1f = 21
motor1b = 20

GPIO.setup(motor1f, GPIO.OUT)
GPIO.setup(motor1b, GPIO.OUT)

locomotion = motors(1,2,3,4)

locomotion.move(speed, turnangle)




def main():
    val = input('arg: ')
    while (val != 'q'):
        GPIO.output(motor1f, bool(literal_eval(val)))
        GPIO.output(motor1b, not bool(literal_eval(val)))
        val = input('arg: ')
    GPIO.output(motor1f, 0)
    GPIO.output(motor1f, 0)
    GPIO.cleanup()




if __name__ == "__main__":
    main()
