from scipy.signal import butter, filtfilt, tf2zpk
from extract_data_from_device import print_header, get_folder_from_user, search_for_latest_file, parse_file_for_tag, \
    get_stream_data, get_stream_time
import numpy as np
import sympy as sp
import weakref
import matplotlib.pyplot as plt
import math
import statistics


class Block:
    _instances = set()

    def __init__(self, number, block_start, block_end):
        self.number = number
        self.block_start = block_start
        self.block_end = block_end
        self.width = block_end - block_start

    @classmethod
    def getinstances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead


def main():
    # load data for testing purposes
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("We can't search file in this location.")
        return
    else:
        print(folder)

    search_text = 'rec'
    latest_file = search_for_latest_file(folder, search_text)
    # print(latest_file)
    stream_tag = 'E4_Bvp'
    stream = parse_file_for_tag(latest_file, stream_tag)
    # print(stream)
    raw_data = get_stream_data(stream)
    time_in_seconds = get_stream_time(stream)

    fs = 64
    # step 1: Bandpass filtering
    filtered_signal = zero_phase_filtering(data=raw_data, f_min=0.5, f_max=8, sampling_frequency=fs, filter_order=2)
    # step 2: Clipping
    clipped_signal = clipping(filtered_signal)
    # step 3: Squaring
    squared_clipped_signal = squaring(clipped_signal)
    # step 4: Moving averages
    MA_peak, MA_beat, samples_peak = generate_moving_averages(data=squared_clipped_signal,
                                                              sampling_frequency=fs, window_for_peak=0.111
                                                              , window_for_beat=0.667)
    # step 5: Thresholds and Offset
    first_threshold, second_threshold = thresholding(data=squared_clipped_signal, moving_average_beat=MA_beat,
                                                     window_for_peak_in_samples=samples_peak)
    # step 6: generate blocks of interest
    blocks_of_interest = np.zeros(len(MA_peak))

    for n in range(len(MA_peak)):
        if MA_peak[n] >= first_threshold[n]:
            np.put(blocks_of_interest, [n], 5000.0)
        else:
            np.put(blocks_of_interest, [n], 0.0)

    # # plotting
    # plt.figure(dpi=1200)
    # plt.plot(squared_clipped_signal, linewidth=0.3)
    # plt.plot(MA_peak, color='green', linewidth=0.3)
    # plt.plot(first_threshold, color='black', linewidth=0.3)
    # # plt.legend(('input', 'MA peak', 'MA beat'))
    # plt.plot(blocks_of_interest, color='grey', linewidth=0.3)
    # plt.show()

    # step 7: find valid blocks
    peak_amplitudes, peak_locations = find_valid_peaks(blocks_of_interest, squared_clipped_signal, second_threshold)

    # plotting
    plt.figure(dpi=1200)
    plt.plot(squared_clipped_signal, color='blue', linewidth=0.3, linestyle='-')
    plt.plot(MA_peak, color='red', linewidth=0.3, linestyle='-.')
    plt.plot(first_threshold, color='black', linewidth=0.3, linestyle=':')
    # plt.legend(('input', 'MA peak', 'MA beat'))
    plt.plot(blocks_of_interest, color='grey', linewidth=0.3, linestyle='--')
    plt.plot(peak_locations, peak_amplitudes, '*y', markersize=0.3)
    plt.show()


def bandpass_butterworth(filter_order, cutoff_frequency_low, cutoff_frequency_high, sampling_frequency):
    """Creating a Butterworth bandpass filter, with a frequency band from cutoff_frequency_low - cutoff_frequency_high.
    """
    nyquist_frequency = 0.5 * sampling_frequency
    low_cut = cutoff_frequency_low / nyquist_frequency
    high_cut = cutoff_frequency_high / nyquist_frequency
    b, a = butter(filter_order, [low_cut, high_cut], btype='band')
    print(type(a))
    print(type(b))
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
    # # plot the result
    # plt.figure(dpi=1200)
    # plt.plot(data, linewidth=1.0, label='input')
    # plt.plot(s_n_gust, color='black', linewidth=1.0, label='gust')
    # plt.show()

    return s_n_gust


def clipping(data):
    """Clipping the input signal by keeping the signal above 0. Function will produce the output signal z_n."""
    # test if data is a numpy array
    if type(data) is not np.ndarray:
        s_n = np.array(data)
    else:
        s_n = data

    z_n = np.zeros(len(s_n))

    for e in range(len(s_n)):
        if s_n[e] >= 0:
            np.put(z_n, [e], s_n[e])
        else:
            np.put(z_n, [e], 0)
    # # plot the result
    # plt.figure(dpi=1200)
    # plt.plot(s_n, linewidth=1.0, label='input')
    # plt.plot(z_n, linewidth=1.0, label='clipped')
    # plt.show()

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
    # # plot the result
    # plt.figure(dpi=1200)
    # plt.plot(z_n, linewidth=2.0, label='input')
    # plt.plot(y_n, linewidth=2.0, label='squared')
    # plt.show()

    return y_n


def generate_moving_averages(data, sampling_frequency, window_for_peak, window_for_beat):
    if type(data) is not np.ndarray:
        y_n = np.array(data)
    else:
        y_n = data

    # the window is calculated from the desired time window (window_for_peak) and the sampling frequency
    # this is done to get the number of samples N that make up the window
    N_1 = math.floor(window_for_peak * sampling_frequency)
    # next we have to guarantee the window extends equally to both sides of the current sample
    # therefore we provide it is the size of the nearest uneven integer
    if N_1 % 2 == 0:
        N_1 = N_1 + 1

    # we calculate the moving avg by convolving with a kernel function
    # the kernel has the size of our window and his coefficients provide the same result as a mov avg
    # coeff = 1/N, N being the window size
    # modes are valid, full and same
    moving_average_peak = np.convolve(y_n, np.ones((N_1,)) / N_1, mode='same')
    # repeat for beat region of interest and beat mov avg
    N_2 = math.floor(window_for_beat * sampling_frequency)
    if N_2 % 2 == 0:
        N_2 = N_2 + 1

    moving_average_beat = np.convolve(y_n, np.ones((N_2,)) / N_2, mode='same')
    # # plotting
    # plt.figure(dpi=1200)
    # plt.plot(y_n)
    # plt.plot(moving_average_peak, color='green', linewidth=2.0)
    # plt.plot(moving_average_beat, color='black', linewidth=2.0)
    # # plt.legend(('input', 'MA peak', 'MA beat'))
    # plt.show()

    return moving_average_peak, moving_average_beat, N_1


def thresholding(data, moving_average_beat, window_for_peak_in_samples):
    beta = 0.02
    z_mean = statistics.mean(data)
    offset_alpha = beta * z_mean

    first_dynamic_threshold = moving_average_beat + offset_alpha
    second_static_threshold = window_for_peak_in_samples

    return first_dynamic_threshold, second_static_threshold


def find_valid_peaks(block_array, signal, second_threshold):
    diff_mask = np.diff(block_array, n=1,)

    # plt.figure(dpi=1200)
    # plt.plot(block_array, linewidth=1.0, label='block array')
    # plt.plot(diff_mask, linewidth=1.0, label='diff_mask')
    # plt.show()
    get_flanks = np.argwhere(diff_mask != 0)

    if diff_mask[get_flanks[0]] < diff_mask[get_flanks[1]]:
        start_index = 1
    else:
        start_index = 0

    get_flanks = get_flanks[start_index:]
    valid_peaks_amplitude = np.zeros((len(get_flanks)))
    valid_peaks_location = np.zeros((len(get_flanks)))

    for f in range(0, len(get_flanks), 2):
        block_start = get_flanks[f][0]
        block_end = get_flanks[f+1][0]
        block_width = block_end - block_start

        # signal_block = signal[block_start:block_end]
        signal_block = signal[get_flanks[f][0]:get_flanks[f + 1][0]]

        if block_width >= second_threshold:
            block_maximum = np.amax(signal_block)
            index_maximum = np.argwhere(signal_block == block_maximum)

            np.put(valid_peaks_amplitude, [f][0], block_maximum)
            np.put(valid_peaks_location, [f][0], index_maximum + block_start)

    valid_peaks_amplitude = valid_peaks_amplitude[valid_peaks_amplitude > 0]
    valid_peaks_location = valid_peaks_location[valid_peaks_location > 0]

    return valid_peaks_amplitude, valid_peaks_location


def peak_detection_bvp(raw_data):
    fs = 64
    # step 1: Bandpass filtering
    filtered_signal = zero_phase_filtering(data=raw_data, f_min=0.5, f_max=8, sampling_frequency=fs, filter_order=2)
    # step 2: Clipping
    clipped_signal = clipping(filtered_signal)
    # step 3: Squaring
    squared_clipped_signal = squaring(clipped_signal)
    # step 4: Moving averages
    MA_peak, MA_beat, samples_peak = generate_moving_averages(data=squared_clipped_signal,
                                                              sampling_frequency=fs, window_for_peak=0.111
                                                              , window_for_beat=0.667)
    # step 5: Thresholds and Offset
    first_threshold, second_threshold = thresholding(data=squared_clipped_signal, moving_average_beat=MA_beat,
                                                     window_for_peak_in_samples=samples_peak)
    # step 6: generate blocks of interest
    blocks_of_interest = np.zeros(len(MA_peak))

    for n in range(len(MA_peak)):
        if MA_peak[n] >= first_threshold[n]:
            np.put(blocks_of_interest, [n], 5000.0)
        else:
            np.put(blocks_of_interest, [n], 0.0)

    # # plotting
    # plt.figure(dpi=1200)
    # plt.plot(squared_clipped_signal, linewidth=0.3)
    # plt.plot(MA_peak, color='green', linewidth=0.3)
    # plt.plot(first_threshold, color='black', linewidth=0.3)
    # # plt.legend(('input', 'MA peak', 'MA beat'))
    # plt.plot(blocks_of_interest, color='grey', linewidth=0.3)
    # plt.show()

    # step 7: find valid blocks
    peak_amplitudes, peak_locations = find_valid_peaks(blocks_of_interest, squared_clipped_signal, second_threshold)

    # plotting
    plt.figure(dpi=1200)
    plt.plot(squared_clipped_signal, color='blue', linewidth=0.3, linestyle='-')
    plt.plot(MA_peak, color='red', linewidth=0.3, linestyle='-.')
    plt.plot(first_threshold, color='black', linewidth=0.3, linestyle=':')
    # plt.legend(('input', 'MA peak', 'MA beat'))
    plt.plot(blocks_of_interest, color='grey', linewidth=0.3, linestyle='--')
    plt.plot(peak_locations, peak_amplitudes, '*y', markersize=0.3)
    plt.show()

    return peak_amplitudes, peak_locations


if __name__ == '__main__':
    main()
