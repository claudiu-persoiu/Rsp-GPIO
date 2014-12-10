import RPi.GPIO as GPIO
import time

led_pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

try:
	while True:
		for i in range(100):
			time.sleep(0.01)
			pwm_led.ChangeDutyCycle(i)

		for i in range(100):
			time.sleep(0.01)
			pwm_led.ChangeDutyCycle(100 - i)
except KeyboardInterrupt:
	pass

finally:
	GPIO.cleanup()
