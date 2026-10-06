import numpy
import time

pi=numpy.pi

def get_sin_wave_amplitude(freq, time):
    return (1+numpy.sin(2*pi*time/freq))/2

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)

