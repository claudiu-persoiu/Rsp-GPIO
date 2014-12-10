import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

switch_pin = 12
led_pin = 11

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)

try:
  while True:
    led_state = GPIO.input(switch_pin)
    GPIO.output(led_pin, led_state)
finally:
  GPIO.cleanup()
