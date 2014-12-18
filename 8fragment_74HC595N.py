import RPi.GPIO as GPIO
import time


class Display8egment:
    
    options = {
        0 : '01111110',
        1 : '01001000',
        2 : '00111101',
        3 : '01101101',
        4 : '01001011',
        5 : '01100111',
        6 : '01110111',
        7 : '01001100',
        8 : '01111111',
        9 : '01001111',
        'r': '00000000'
    }
    
    def __init__(self, data_in = 11, latch = 12, clock = 13):
        self.data_in = data_in
        self.latch = latch
        self.clock = clock
        
        GPIO.setmode(GPIO.BOARD)
        
        GPIO.setup(self.data_in, GPIO.OUT)
        GPIO.setup(self.latch, GPIO.OUT)
        GPIO.setup(self.clock, GPIO.OUT)
    
    def display(self, char):
        for c in self.__class__.options[char]:
            if c is '1':
                GPIO.output(self.data_in,GPIO.HIGH)
            else:
                GPIO.output(self.data_in,GPIO.LOW)
                
            self._tick()    
            
        GPIO.output(self.data_in, GPIO.LOW)
        self._display()
    
    def _tick(self):
        GPIO.output(self.clock, GPIO.HIGH)
        GPIO.output(self.clock, GPIO.LOW)
    
    def _display(self):
        GPIO.output(self.latch,GPIO.HIGH)
        GPIO.output(self.latch,GPIO.LOW)
    
    def clean(self):
        GPIO.cleanup()
        

display = Display8egment()
for i in range(0, 10):
    display.display(i)
    time.sleep(1)

display.display('r')
display.clean()
