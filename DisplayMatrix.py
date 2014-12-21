import time
from Shifter import Shifter

class DisplayMatrix:

    def __init__(self, timeout = .002):
        self.timeout = timeout
        self.shifter = Shifter()
    
    def display(self, out):
        for i in range(0, len(out)):
            self.shifter.display(out[i][::-1] + self.line(i))
            
            # take some load off the CPU
            time.sleep(self.timeout)
        
    def line(self, index):
        return ((7 - index) * '0') + '1' + (index * '0')
        
    def clear(self):
        self.shifter.display('0000000000000000')
        
    def __del__(self):
        self.clear()
