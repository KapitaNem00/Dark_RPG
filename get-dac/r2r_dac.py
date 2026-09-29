import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

gpio_bits = [22, 27, 17, 26, 25, 21, 20, 16]
gpio_bits.reverse()
dynamic_range=3.3

GPIO.setup(gpio_bits, GPIO.OUT)

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def set_number(self, number) :
        dcb=[int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.gpio_bits, dcb)

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= dynamic_range):
            print("Устанавлниваем 0.0 В")
            return 0
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        return int(voltage / dynamic_range * 255)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()