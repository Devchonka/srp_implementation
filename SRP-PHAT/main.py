"""

Tasks:

 Read in signals from 5 microphones
 Get mic locations
 Get mic search volumes
 Get fft of signals in w domain
 Find weighting function
 Find P at point X
 Find cross corr of signals at point X
 Find power using cross corrs at point X
 Find location of max power

"""
from pyfirmata import Arduino

from math import sqrt, pi
from numpy import fft, conjugate, absolute, linalg, array, exp, linspace, cos, sin, argmax, arctan2, degrees
from itertools import combinations

import streamer
import plotting

def filter_based_on_freq(data, freq, min_freq, max_freq):
  return data[(min_freq <= freq) & (freq <= max_freq)]


def main():
    mic_loc = array([(-.005, -.055), (-.056, -.018), (-.035, .046), (.034, .043), (.051, -.02)]) * -1

    arduino_ = Arduino('/dev/ttyACM0', timeout=10)
    arduino_.servo_config(10)
    arduino_.digital[10].write(90)

    analog_ports = list(range(5))
    scan_rate = 19000
    sample_rate = scan_rate * 5
    extra_delays = array(range(5))[::-1] / sample_rate
    scans_per_read = scan_rate / 5

    labjack_class = streamer.LabjackAnalogReader(analog_ports, scan_rate, scans_per_read)
    labjack_class.open()

    plotter = plotting.DynamicScatterPlotter('Mic Array Beam')
    while(True):
        data = labjack_class.get_data()
        search_grid = get_point_cloud(3, 20) # get point cloud around center for all mics
        powers = srp(data, mic_loc, scan_rate, search_grid, extra_delays)
        max_point = search_grid[argmax(absolute(powers))]
        max_power = max(absolute(powers))
        print(max_power)
        if max_power > 1000:
            angle = arctan2(max_point[0], max_point[1])
            angle_deg = degrees(angle)
            if angle_deg < -90:
                angle_deg = -90
            if angle_deg > 90:
                angle_deg = 90
            arduino_.digital[10].write(90 + angle_deg)
        x_search_point,y_search_point = zip(*search_grid)
        plotter.update(x_search_point, y_search_point, absolute(powers))

    labjack_class.close()


def srp(data, mic_loc, scan_rate, search_grid, extra_delays):
    # GCC- PHAT
    data_f_domain = []
    conj_data_f_domain = []
    for signal in data:
        signal_fft = fft.fft(signal)
        freqs = 2*pi*fft.fftfreq(len(signal_fft), d=1 / scan_rate)
        signal_fft = filter_based_on_freq(signal_fft, freqs, 900 * 2 * pi, 3000 * 2 * pi)
        freqs = filter_based_on_freq(freqs, freqs, 900 * 2 * pi, 3000 * 2 * pi)
        data_f_domain.append(signal_fft)  # FFT of the original signals
        conj_data_f_domain.append(conjugate(signal_fft))

    pairs = list(combinations(range(5), 2))

    power = []
    for point in search_grid:
        power.append(get_pwr(point, data_f_domain,
                     conj_data_f_domain, mic_loc, pairs, freqs, extra_delays))
    return power


def get_point_cloud(radius, num_points):
    # returns a list of tuples of (x,y) points in upper hemisphere

    thetas = linspace(0, 2 * pi, num_points + 1)[:-1]
    xs = radius * cos(thetas)
    ys = radius * sin(thetas)
    return list(zip(xs, ys))


def get_tau(pointX, point_k, point_l, extra_delay_k, extra_delay_l):
    tempC = 21.0
    csound = 331.4 * sqrt(1.0 + (tempC / 273))  # speed of sound through dry air
    return (linalg.norm(array(pointX) - point_k)+extra_delay_k - linalg.norm(array(pointX) - point_l) + extra_delay_l) / csound


def get_cross_corr(pointX, data_f_domain, conj_data_f_domain, mic_loc, pair, freqs, extra_delays):
    cross_corr = data_f_domain[pair[0]] * conj_data_f_domain[pair[1]]
    phi_kl = 1 / absolute(cross_corr)
    tau = get_tau(pointX, mic_loc[pair[0]], mic_loc[pair[1]], extra_delays[pair[0]], extra_delays[pair[1]])
    return sum(phi_kl * cross_corr * exp(1j * freqs * tau))


def get_pwr(pointX, data_f_domain, conj_data_f_domain, mic_loc, pairs, freqs, extra_delays):
    pwr = 0
    for pair in pairs:
        pwr += get_cross_corr(pointX, data_f_domain, conj_data_f_domain, mic_loc, pair, freqs, extra_delays)
    return pwr


if __name__ == '__main__':
    main()
