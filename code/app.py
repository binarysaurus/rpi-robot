from ast import literal_eval
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

motor1f = 21
motor1b = 20

GPIO.setup(motor1f, GPIO.OUT)
GPIO.setup(motor1b, GPIO.OUT)




def main():
    val = input('arg: ')
    while (val != 'q'):
        GPIO.output(motor1f, bool(literal_eval(val)))
        GPIO.output(motor1b, not bool(literal_eval(val)))
        val = input('arg: ')
    #GPIO.output(20, 1)

GPIO.output(motor1f, 0)
GPIO.output(motor1b, 0)
GPIO.cleanup()


if __name__ == "__main__":
    main()
