import time
from Shifter import Shifter

class Display8egment:
    
    options = {
        '0' : '01111110',
        '1' : '01001000',
        '2' : '00111101',
        '3' : '01101101',
        '4' : '01001011',
        '5' : '01100111',
        '6' : '01110111',
        '7' : '01001100',
        '8' : '01111111',
        '9' : '01001111',
        'r': '00000000'
    }
    
    def __init__(self):
        self.shifter = Shifter()
    
    def display(self, string):
        out = ''
        for c in str(string)[::-1]:
            out += self.__class__.options[c]
            
        self.shifter.display(out)
        

display = Display8egment()
for i in range(10, 30)[::-1]:
    display.display(i)
    time.sleep(1)

display.display('rr')
# display.clean()
