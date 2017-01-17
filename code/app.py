import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setwarnings(False)



def main():
    val = input('arg: ')
    while (val != 'q'):
        GPIO.output(21, 1 if str2bool(val) else 0)
        GPIO.output(20, 0 if str2bool(val) else 1)
        val = input('arg: ')
    #GPIO.output(20, 1)


def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")


if __name__ == "__main__":
    main()
