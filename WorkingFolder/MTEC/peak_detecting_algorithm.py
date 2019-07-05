from scipy.signal import butter, filtfilt, tf2zpk
import numpy as np
import matplotlib.pyplot as plt
import math
import statistics


def main():
    fs = 64
    filtered_signal = zero_phase_filtering(data=raw_data, f_min=0.5, f_max=8, sampling_frequency=fs, filter_order=2)
    clipped_signal = clipping(filtered_signal)
    squared_clipped_signal = squaring(clipped_signal)
    MA_peak, MA_beat, samples_peak = generate_moving_averages(data=squared_clipped_signal,
                                                              sampling_frequency=fs, window_for_peak=0.111
                                                              , window_for_beat=0.667)
    first_threshold, second_threshold = thresholding(data=squared_clipped_signal, moving_average_beat=MA_beat,
                                                     window_for_peak_in_samples=samples_peak)

    # generate blocks of interest
    # todo: continue ..line of algorithm = 10 (url:https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3805543/#pone.0076585-Elgendi3)

def bandpass_butterworth(filter_order, cutoff_frequency_low, cutoff_frequency_high, sampling_frequency):
    """Creating a Butterworth bandpass filter, with a frequency band from cutoff_frequency_low - cutoff_frequency_high.
    """
    nyquist_frequency = 0.5 * sampling_frequency
    low_cut = cutoff_frequency_low / nyquist_frequency
    high_cut = cutoff_frequency_high / nyquist_frequency
    b, a = butter(filter_order, [low_cut, high_cut], btype='band')
    return b, a


def zero_phase_filtering(data, f_min, f_max, sampling_frequency, filter_order=2):
    """Filter function using a zero phase second order Butterworth filter, with bandpass f_min - f_max, is implemented
    to remove baseline wander and high frequencies. Returns zero phase bandpass filtered signal s_n"""
    # test if data is a numpy array
    if type(data) is not np.ndarray:
        signal = np.array(data)
    else:
        signal = data

    # create a bandpass butterworth filter
    b, a = bandpass_butterworth(filter_order=filter_order, cutoff_frequency_low=f_min, cutoff_frequency_high=f_max,
                                sampling_frequency=sampling_frequency)

    # We use scypi.filtfilt using the Gustafsson's method (include paper)
    # The irlen argument can be used to improve the performance of Gustafsson’s method.
    # (url: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.filtfilt.html#r10879a509a76-1)
    # Estimate the impulse response length of the filter.
    z, p, k = tf2zpk(b, a)
    eps = 1e-9
    r = np.max(np.abs(p))
    approx_impulse_len = int(np.ceil(np.log(eps) / np.log(r)))
    # apply the zero phase bandpass filter with estimated impuls length according to Gustafsson's method
    s_n_gust = filtfilt(b, a, signal, method='gust', irlen=approx_impulse_len)
    # plot the result
    plt.plot(data, 'k-', label='input')
    plt.plot(s_n_gust, 'b-', linewidth=4, label='gust')

    return s_n_gust


def clipping(data):
    """Clipping the input signal by keeping the signal above 0. Function will produce the output signal z_n."""
    # test if data is a numpy array
    if type(data) is not np.ndarray:
        s_n = np.array(data)
    else:
        s_n = data

    z_n = s_n[s_n >= 0]
    # plot the result
    plt.plot(s_n, 'k-', label='input')
    plt.plot(z_n, 'k-', label='clipped')
    return z_n


def squaring(data):
    """Squaring the input signal to emphasize large differences resulting from systolic waves,
    while suppressing small differences arising from diastolic waves and noise. Function produces output y_n"""
    # test if data is a numpy array
    if type(data) is not np.ndarray:
        z_n = np.array(data)
    else:
        z_n = data

    y_n = np.square(z_n)

    return y_n


def generate_moving_averages(data, sampling_frequency, window_for_peak, window_for_beat):
    if type(data) is not np.ndarray:
        y_n = np.array(data)
    else:
        y_n = data

    # the window is calculated from the desired time window (window_for_peak) and the sampling frequency
    # this is done to get the number of samples N that make up the window
    N_1 = window_for_peak * sampling_frequency
    # next we have to guarantee the window extends equally to both sides of the current sample
    # therefore we provide it is the size of the nearest uneven integer
    if math.floor(N_1) % 2 == 0:
        N_1 = N_1 + 1

    # we calculate the moving avg by convolving with a kernel function
    # the kernel has the size of our window and his coefficients provide the same result as a mov avg
    # coeff = 1/N, N being the window size
    # modes are valid, full and same
    moving_average_peak = np.convolve(y_n, np.ones((N_1,)) / N_1, mode='valid')
    # repeat for beat region of interest and beat ov avg
    N_2 = window_for_beat * sampling_frequency
    if math.floor(N_2) % 2 == 0:
        N_2 = N_2 + 1

    moving_average_beat = np.convolve(y_n, np.ones((N_2,)) / N_2, mode='valid')
    # plotting
    plt.plot(y_n)
    plt.plot(moving_average_peak)
    plt.plot(moving_average_beat)
    plt.legend(('input', 'MA peak', 'MA beat'))
    plt.show()

    return moving_average_peak, moving_average_beat, N_1


def thresholding(data, moving_average_beat, window_for_peak_in_samples):
    beta = 0.02
    z_mean = statistics.mean(data)
    offset_alpha = beta * z_mean

    first_dynamic_threshold = moving_average_beat + offset_alpha
    second_static_threshold = window_for_peak_in_samples

    return first_dynamic_threshold, second_static_threshold


if __name__ == '__main__':
    main()
