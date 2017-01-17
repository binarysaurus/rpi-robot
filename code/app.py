from distutils import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setwarnings(False)



def main():
    val = input('arg: ')
    while (val != 'q'):
        GPIO.output(21, bool(distutils.util.strtobool(val)))
        GPIO.output(20, not bool(distutils.util.strtobool(val)))
        val = input('arg: ')
    #GPIO.output(20, 1)


if __name__ == "__main__":
    main()
