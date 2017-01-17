from ast import literal_eval
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

motor1f = 8
motor1b = 7

GPIO.setup(motor1f, GPIO.OUT)
GPIO.setup(motor1b, GPIO.OUT)




def main():
    val = input('arg: ')
    while (True):
        GPIO.output(motor1f, bool(literal_eval(val)))
        GPIO.output(motor1b, not bool(literal_eval(val)))
        val = input('arg: ')
    GPIO.output(motor1f, 0)
    GPIO.output(motor1f, 0)
    GPIO.cleanup()




if __name__ == "__main__":
    main()
