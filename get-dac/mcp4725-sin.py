import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.1
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = mcp.MCP(4.2, True)
        tm=0
        
        while True:
            try:
                voltage = sg.get_sin_wave_amplitude(signal_frequency, tm)*amplitude
                dac.set_voltage(voltage)
                sg.wait_for_sampling_period(sampling_frequency)
                tm=tm+1/sampling_frequency

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
