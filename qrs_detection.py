import numpy as np
import scipy as sp
import scipy.signal as signal
import matplotlib.pyplot as plt
import timeit


class Detectors:

    def __init__(self, fs):
        self.f_sample = fs

    # Based on "A Real-Time QRS Detection Algorithm" by Pan & Tompkins
    def pan_tompkins(self, data):
        #Band pass filter, passband 5-15Hz, B=10Hz
        f_nyq = self.f_sample / 2
        f_l = 2
        f_h = 20

        #butterworth filter method takes passband freqs as fractions of nyquist freq
        f_1 = f_l/f_nyq
        f_2 = f_h/f_nyq

        b, a = signal.butter(1, [f_1, f_2], btype='bandpass')
        bp_filtered = signal.lfilter(b, a, data)

        plt.plot(bp_filtered)
        #plt.show()

