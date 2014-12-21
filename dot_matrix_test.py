from DisplayMatrixText import DisplayMatrixText

display_text = DisplayMatrixText()

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