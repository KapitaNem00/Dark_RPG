import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.14, True)
        tm=0
        
        while True:
            try:
                voltage = sg.get_sin_wave_amplitude(signal_frequency, tm)*amplitude
                dac.set_voltage(voltage)
                sg.wait_for_sampling_period(sampling_frequency)
                tm=tm+1/signal_frequency

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()