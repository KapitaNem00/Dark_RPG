import r2r_adc as adc
import matplotlib.pyplot as plt
import time

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)

def plot_sampling_period_hist(time):
    plt.figure(figsize=(10,6))
    plt.hist(time)
    plt.xlim(0, 0.06)
    plt.show()

if __name__ == "__main__":
    try:
        sar = adc.R2R_ADC(3.14, 0.0001, True)
        voltage_values = []
        time_values = []
        time_del = []
        duration = 3.0
        st=time.time()
        while True:
            try:
                while(time.time()-st<3):
                    ms=time.time()
                    voltage_values.append(sar.bin_sar())
                    time_del.append(time.time()-ms)
                    time_values.append(time.time()-st)                
                plot_voltage_vs_time(time_values, voltage_values, 0)
                plot_sampling_period_hist(time_del)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        adcp.deinit()
