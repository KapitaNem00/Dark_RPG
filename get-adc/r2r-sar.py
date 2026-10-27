import time
import r2r_adc as adc


if __name__ == "__main__":
    try:
        sar = adc.R2R_ADC(3.14, 0.01, True)
        
        while True:
            try:
                print(sar.bin_sar(), "\n")
                time.sleep(1)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        sar.deinit()