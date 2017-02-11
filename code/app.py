from ast import literal_eval
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class motor(object):
    def __init__(self, iopin, LR):
    	self.iopin = iopin
    	self.LR = LR
    	

    def setdrive(self):





motor1f = 21
motor1b = 20

GPIO.setup(motor1f, GPIO.OUT)
GPIO.setup(motor1b, GPIO.OUT)

motor front_left



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
