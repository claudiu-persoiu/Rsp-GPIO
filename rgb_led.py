import RPi.GPIO as GPIO
import time

red_pin = 13
blue_pin = 11
green_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

GPIO.output(red_pin,GPIO.HIGH)
time.sleep(1)
GPIO.output(red_pin,GPIO.LOW) 

GPIO.output(blue_pin,GPIO.HIGH)  
time.sleep(1)
GPIO.output(blue_pin,GPIO.LOW) 

GPIO.output(green_pin,GPIO.HIGH)  
time.sleep(1)
GPIO.output(green_pin,GPIO.LOW) 

GPIO.cleanup()