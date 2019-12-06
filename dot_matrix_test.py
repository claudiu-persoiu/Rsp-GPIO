from DisplayMatrixText import DisplayMatrixText
from DisplayMatrix import DisplayMatrix

display_text = DisplayMatrixText(speed = .5, display_matrix = DisplayMatrix())

try:
    while True:
        text = raw_input("Text to be displayed: ")
        print "Displaying..."
        display_text.display(text)
except Exception:
    pass
except KeyboardInterrupt:
    pass
finally:
    print "Bye bye!"
