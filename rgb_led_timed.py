import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pins = [11, 12, 13]

for pin in pins:
  GPIO.setup(pin, GPIO.OUT)

try:
  pwd_led_old = GPIO.PWM(pins[-1], 500)
  pwd_led_old.start(0)
  
  while True:
    for led in pins:
      pwm_led = GPIO.PWM(led, 500)
      pwm_led.start(0)

      for i in range(100):
        time.sleep(0.03)
        pwm_led.ChangeDutyCycle(i)
        pwd_led_old.ChangeDutyCycle(100 - i)
      
      pwd_led_old.ChangeDutyCycle(0)
      pwd_led_old = pwm_led
except KeyboardInterrupt:
  pass

finally:
  GPIO.cleanup()