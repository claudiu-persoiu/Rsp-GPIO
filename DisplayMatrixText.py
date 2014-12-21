import time
from DisplayMatrix import DisplayMatrix

class DisplayMatrixText:

    aphabet = {
        'a': [
            '11111',
            '10011',
            '01101',
            '01101',
            '00001',
            '01101',
            '01101',
            '11111'
        ],
        'b': [
            '11111',
            '00011',
            '01101',
            '00011',
            '01101',
            '01101',
            '00011',
            '11111'
        ],
        'c': [
            '11111',
            '10011',
            '01101',
            '01111',
            '01111',
            '01101',
            '10011',
            '11111'
        ],
        'd': [
            '11111',
            '00011',
            '01101',
            '01101',
            '01101',
            '01101',
            '00011',
            '11111'
        ],
        'e': [
            '1111',
            '0001',
            '0111',
            '0001',
            '0111',
            '0111',
            '0001',
            '1111'
        ],
        'f': [
            '1111',
            '0001',
            '0111',
            '0001',
            '0111',
            '0111',
            '0111',
            '1111'
        ],
        'g': [
            '11111',
            '10011',
            '01101',
            '01111',
            '01001',
            '01101',
            '10011',
            '11111'
        ],
        'h': [
            '11111',
            '01101',
            '01101',
            '00001',
            '01101',
            '01101',
            '01101',
            '11111'
        ],
        'i': [
            '11',
            '01',
            '11',
            '01',
            '01',
            '01',
            '01',
            '11'
        ],
        'j': [
            '11111',
            '11101',
            '11101',
            '11101',
            '11101',
            '01101',
            '10011',
            '11111'
        ],
        'k': [
            '11111',
            '01101',
            '01011',
            '00111',
            '01011',
            '01101',
            '01101',
            '11111'
        ],
        'l': [
            '1111',
            '0111',
            '0111',
            '0111',
            '0111',
            '0111',
            '0001',
            '1111'
        ],
        'm': [
            '111111',
            '011101',
            '001001',
            '010101',
            '011101',
            '011101',
            '011101',
            '111111'
        ],
        'n': [
            '11111',
            '01101',
            '00101',
            '01001',
            '01101',
            '01101',
            '01101',
            '11111'
        ],
        'o': [
            '11111',
            '10011',
            '01101',
            '01101',
            '01101',
            '01101',
            '10011',
            '11111'
        ],
        'p': [
            '11111',
            '00011',
            '01101',
            '01101',
            '00011',
            '01111',
            '01111',
            '11111'
        ],
        'q': [
            '11111',
            '10011',
            '01101',
            '01101',
            '01101',
            '01101',
            '10001',
            '11111'
        ],
        'r': [
            '11111',
            '00011',
            '01101',
            '01101',
            '00011',
            '01011',
            '01101',
            '11111'
        ],
        's': [
            '11111',
            '10001',
            '01111',
            '10011',
            '11101',
            '01101',
            '10011',
            '11111'
        ],
        't': [
            '111111',
            '000001',
            '110111',
            '110111',
            '110111',
            '110111',
            '110111',
            '111111'
        ],
        'u': [
            '11111',
            '01101',
            '01101',
            '01101',
            '01101',
            '01101',
            '10011',
            '11111'
        ],
        'v': [
            '111111',
            '011101',
            '011101',
            '011101',
            '011101',
            '101011',
            '110111',
            '111111'
        ],
        'w': [
            '111111',
            '011101',
            '011101',
            '011101',
            '010101',
            '001001',
            '011101',
            '111111'
        ],
        'x': [
            '11111',
            '01101',
            '01101',
            '10011',
            '10011',
            '01101',
            '01101',
            '11111'
        ],
        'y': [
            '111111',
            '011101',
            '011101',
            '100011',
            '110111',
            '110111',
            '110111',
            '111111'
        ],
        'z': [
            '11111',
            '00001',
            '11011',
            '10111',
            '01111',
            '01111',
            '00001',
            '11111'
        ],
        ' ': [
            '11',
            '11',
            '11',
            '11',
            '11',
            '11',
            '11',
            '11'
        ],
        '.': [
            '11',
            '11',
            '11',
            '11',
            '11',
            '11',
            '01',
            '11'
        ],
        '!': [
            '11',
            '01',
            '01',
            '01',
            '01',
            '11',
            '01',
            '11'
        ],
        '?': [
            '11111',
            '10011',
            '01101',
            '11011',
            '10111',
            '11111',
            '10111',
            '11111'
        ],
    }

    def __init__(self, speed = 1):
        self.speed = speed
        self.display_matrix = DisplayMatrix()
    
    def display(self, text):
        matrix = self.convert(text)
        
        output = ['', '', '', '', '', '', '', '']
            
        for offset in range(0, len(matrix[0]) - 8):
                
            for i in range(0, len(matrix)):
                output[i] = matrix[i][(offset):(offset + 8)]
                
            for _ in range(0, int(30 * self.speed)):
                self.display_matrix.display(output)

    def convert(self, text):
        matrix = ['', '', '', '', '', '', '', '']
        
        text = '    ' + text + '    '
        
        for c in text:
            char_matrix = self.__class__.aphabet[c]
            for i in range(0, len(char_matrix)):
                matrix[i] = matrix[i] + char_matrix[i]
                
        return matrix
