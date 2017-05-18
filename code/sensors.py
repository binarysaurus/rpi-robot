import RPi.GPIO as GPIO
import time
import threading

class RangeFinder(object):
    def __init__(self, trigpin, echopin, orientation = None):

        print("Initializing Ultrasonic Range Finder... \n\tTRIGGER: %d, ECHO:  %d" % 
            (trigpin, echopin))

        self.trigpin = trigpin
        self.echopin = echopin
        self.orientation = orientation
        self.distance = 0
        GPIO.setup(self.trigpin, GPIO.OUT)
        GPIO.setup(self.echopin, GPIO.IN)
        time.sleep(2)

    def _getdistance(self):
        GPIO.output(self.trigpin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigpin, False)
        
        while GPIO.input(self.echopin)==0:
          pstart = time.time()
        
        while GPIO.input(self.echopin)==1:
          pend = time.time()

        self.distance = (pend - pstart) * 17150
    
    def getdistance(self):
        gd = threading.Thread(target=self._getdistance)
        gd.start()
        gd.join()
        return self.distance