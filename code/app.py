from ast import literal_eval
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)




def main():
    val = input('arg: ')
    while (val != 'q'):
        GPIO.output(21, bool(literal_eval(val)))
        GPIO.output(20, not bool(literal_eval(val)))
        val = input('arg: ')
    #GPIO.output(20, 1)

GPIO.output(21, 0)
GPIO.output(20, 0)
GPIO.cleanup()


if __name__ == "__main__":
    main()
