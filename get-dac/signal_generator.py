import numpy
import time

pi=numpy.pi

def get_sin_wave_amplitude(freq, time):
    sn=numpy.sin(2*pi*time/freq)
    return (sn+1)/2

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)
