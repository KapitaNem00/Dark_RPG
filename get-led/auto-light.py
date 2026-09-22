import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
dat = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(dat, GPIO.IN)

state = 0
period = 1.0

while True:
    state = not GPIO.input(dat)
    GPIO.output(led, state)
    time.sleep(0.2)