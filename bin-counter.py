import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
num = 0
sleep_time = 0.2
up=10
down=9


GPIO.setup(leds, GPIO.OUT)
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
GPIO.output(leds, 0)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

while True:
    if GPIO.input(up):
        num = num + 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(up):
            num = num + 1
            print(num, dec2bin(num))
            time.sleep(sleep_time)
    GPIO.output(leds, dec2bin(num))