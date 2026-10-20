import r2r_adc as adc
import matplotlib.pyplot as plt
import time

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.show()

if __name__ == "__main__":
    try:
        adcp = adc.R2R_ADC(3.14, 0.0001, True)
        voltage_values = []
        time_values = []
        duration = 3.0
        st=time.time()
        while True:
            try:
                while(time.time()-st<3):
                    voltage_values.append(adc.sequential_counting_adc())
                    time_values.append(time.time()-st)                
                plot_voltage_vs_time(time_values, voltage_values, 0)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        adc.deinit()
