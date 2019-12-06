import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class DisplayMatrixMax7219:

    def __init__(self, latch = 15, clock = 13, data_in = 11, intensity = 2):
        self.latch = latch, 
        self.clock = clock, 
        self.data_in = data_in

        GPIO.setup(self.latch, GPIO.OUT)
        GPIO.setup(self.clock, GPIO.OUT)
        GPIO.setup(self.data_in, GPIO.OUT)

        GPIO.output(self.latch, GPIO.LOW)
        GPIO.output(self.clock, GPIO.LOW)
        self._initMAX7219(intensity)
    
    def _tick(self):
        GPIO.output(self.clock, GPIO.HIGH)
        GPIO.output(self.clock, GPIO.LOW)
        return

    def _pulseLatch(self):
        GPIO.output(self.latch, GPIO.HIGH)
        GPIO.output(self.latch, GPIO.LOW)
        return

    def _pushData(self, value):
        for x in range(0,8):
            temp = value & 0x80
            if temp == 0x80:
                GPIO.output(self.data_in, 1) # data bit HIGH
            else:
                GPIO.output(self.data_in, 0) # data bit LOW
            self._tick()
            value = value << 0x01 # shift left       
        return

    def _initMAX7219(self, intensity):
        # no decode
        self._pushData(0x09)
        self._pushData(0x00)
        self._pulseLatch();

        # set intensity
        self._pushData(0x0A)
        self._pushData(intensity) 
        self._pulseLatch()

        # set scan limit 0-7
        self._pushData(0x0B)
        self._pushData(0x07)
        self._pulseLatch()

        for i in range(0, 9):
            self.writeMAX7219(0, i)
        self.displayOn()

    def writeMAX7219(self, data, location):
        self._pushData(location)
        self._pushData(data)
        self._pulseLatch()
        return


    def displayOff(self):
        self._pushData(0x0C)
        self._pushData(0x00)
        self._pulseLatch()


    def displayOn(self):
        self._pushData(0x0C)
        self._pushData(0x01)
        self._pulseLatch()

    def display(self, out):
        for i in range(0, len(out)):
            self.writeMAX7219(int(out[i], 2), (i % 8) + 1)
            
    def line(self, index):
        return ((7 - index) * '0') + '1' + (index * '0')
     
    def __del__(self):
        self.displayOff()
        GPIO.cleanup()
