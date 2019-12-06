import RPi.GPIO as GPIO

class Shifter:
    
    def __init__(self, data_in = 11, latch = 12, clock = 13):
        self.data_in = data_in
        self.latch = latch
        self.clock = clock
        
        GPIO.setmode(GPIO.BOARD)
        
        GPIO.setup(self.data_in, GPIO.OUT)
        GPIO.setup(self.latch, GPIO.OUT)
        GPIO.setup(self.clock, GPIO.OUT)
    
    def display(self, str):
        for c in str:
            if c is '1':
                GPIO.output(self.data_in,GPIO.LOW)
            else:
                GPIO.output(self.data_in,GPIO.HIGH)
            self._tick()    
            
        GPIO.output(self.data_in, GPIO.LOW)
        self._display()
    
    def _tick(self):
        GPIO.output(self.clock, GPIO.HIGH)
        GPIO.output(self.clock, GPIO.LOW)
    
    def _display(self):
        GPIO.output(self.latch,GPIO.HIGH)
        GPIO.output(self.latch,GPIO.LOW)
    
    def __del__(self):
        GPIO.cleanup()