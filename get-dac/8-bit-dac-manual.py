import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

leds = [22, 27, 17, 26, 25, 21, 20, 16]
dynamic_range=3.3



GPIO.setup(leds, GPIO.OUT)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def number_to_dac(value):
    GPIO.output(leds, dec2bin(value))

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print("Устанавлниваем 0.0 В")
        return 0
    print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
    return int(voltage / dynamic_range * 255)

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            print(number)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()