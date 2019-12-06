from DisplayMatrixMax7219 import DisplayMatrixMax7219

latch = 15
clock = 13
data_in = 11

display = DisplayMatrixMax7219(latch = latch, clock = clock, data_in = data_in)

try:
    while True:
        display.display([
            '00010000',
            '00111000',
            '01111100',
            '00111000',
            '01111100',
            '11111110',
            '00010000',
            '00000000'
        ])
        input('Press ENTER to stop...')
except KeyboardInterrupt:
    pass
except SyntaxError:
    pass
finally:
    print "\nBye bye!"
