from DisplayMatrixMax7219 import DisplayMatrixMax7219
from DisplayMatrixText import DisplayMatrixText

latch = 15
clock = 13
data_in = 11

display_text = DisplayMatrixText(display_matrix = DisplayMatrixMax7219(latch = latch, clock = clock, data_in = data_in))

try:
    while True:
        text = raw_input("Text to be displayed: ")
        print "Displaying..."
        display_text.display(text)
except KeyboardInterrupt:
    pass
finally:
    print "\nBye bye!"

