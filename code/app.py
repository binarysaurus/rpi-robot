import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

GPIO.output(21, 1)
#GPIO.output(20, 1)
