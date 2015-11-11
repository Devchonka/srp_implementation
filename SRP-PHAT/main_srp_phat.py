"""
Module that contains main srp phat algorithm implementation
"""


import numpy as np

class Data_Signals(object):
    scan_rate = 19000
    def __init__(self, signals_t):
        self.signals_t = self.signals_f = self.signals_f_conj = None
        if self.signals_t is None:
            self.signals_t = signals_t
            self.signals_f = [np.fft.fft(signal) for signal in self.signals_t]
            self.signals_f_conj = [np.conjugate(signal) for signal in self.signals_f]
            # maybe this can be class variable? then filter them by freqs
            self.freqs = 2*np.pi*np.fft.fftfreq(len(self.signals_f), d=1 / Data_Signals.scan_rate)


class Mic_Pair(object):
    pass


class Magic_Box(object):
    def __init__(self):
        self.mic_loc = np.array([(.005, .055), (.056, .018), (.035, -.046), (-.034, -.043), (-.051, .02)])