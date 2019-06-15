import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz, signaltools, find_peaks, find_peaks_cwt


def main():
    filter_order = 6
    sampling_frequency = 64                 # Hz
    max_heart_rate = 220                    # bpm
    cutoff_frequency = round((max_heart_rate / 60), ndigits=3)  # desired max frequency in Hz

    # Get the filter coefficients so we can check its frequency response.
    b, a = butter_lowpass(cutoff_frequency, sampling_frequency, filter_order)
    # Plot the frequency response.
    w, h = freqz(b, a, worN=8000)
    plt.subplot(2, 1, 1)
    plt.plot(0.5 * sampling_frequency * w / np.pi, np.abs(h), 'b')
    plt.plot(cutoff_frequency, 0.5 * np.sqrt(2), 'ko')
    plt.axvline(cutoff_frequency, color='k')
    plt.xlim(0, 0.5 * sampling_frequency)
    plt.title("Lowpass Filter Frequency Response")
    plt.xlabel('Frequency [Hz]')
    plt.grid()

    plt.subplots_adjust(hspace=0.35)
    plt.show()


def butter_lowpass(cutoff, fs, order):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


def detrend_the_signal(data):
    detrend_data = signaltools.detrend(data)
    return detrend_data


def find_negative_peaks_in_signal(data, sampling_frequency, distance_factor, peak_prominence):
    inverted_data = -data
    min_peak_distance = distance_factor * sampling_frequency
    peaks, properties = find_peaks(inverted_data, distance=min_peak_distance, prominence=peak_prominence)
    plt.plot(inverted_data)
    plt.plot(peaks, inverted_data[peaks], "x")
    plt.plot(np.zeros_like(inverted_data), "--", color="gray")
    plt.show()
    return peaks, properties


def find_positive_peaks_in_signal(data, sampling_frequency, distance_factor, peak_height):
    min_peak_distance = distance_factor * sampling_frequency * 0.01     # extra factor to minimize it
    peaks, properties = find_peaks(data, distance=min_peak_distance, height=peak_height)
    plt.plot(data)
    plt.plot(peaks, data[peaks], "x")
    plt.plot(np.zeros_like(data), "--", color="gray")
    plt.show()
    return peaks, properties


def pass_only_valid_peaks(negative_peaks, positive_peaks):
    i = 0
    valid_peak_locations = np.zeros(shape=(1, len(positive_peaks)))

    while i <= len(negative_peaks)+1:

        if i == 0:
            interval_peak_locations = positive_peaks[positive_peaks <= negative_peaks[i]]
        elif (i > 0) & (i <= len(negative_peaks)):
            interval_peak_locations = np.logical_and(positive_peaks >= negative_peaks[i - 1], positive_peaks <= negative_peaks[i])
        elif i == len(negative_peaks)+1:
            interval_peak_locations = positive_peaks[positive_peaks >= negative_peaks[i-1]]

        if interval_peak_locations:
            valid_peak_locations[i] = interval_peak_locations[0]

        i += 1

    valid_peak_locations = valid_peak_locations > 0
    valid_peaks = positive_peaks[valid_peak_locations]

    return valid_peaks


def get_frequency_bands(ibi_data, frequencies: tuple):
    signal = ibi_data
    min_frequency = frequencies[0]
    max_frequency = frequencies[1]

    # print(signal)
    # plt.figure(dpi=600)
    # plt.plot(signal)
    # plt.xlabel('sample')
    # plt.ylabel('HRV')
    # plt.show()

    hanning_window = np.hanning(len(signal))
    ft_signal = np.fft.fft(hanning_window * signal)
    n = math.floor(len(ft_signal) / 2) + 1
    fa = 1.0 / 64
    # print('fa=%.4f Hz  (Frequency)' % fa)

    ft_frequency_range = np.linspace(0, fa / 2, n, endpoint=True)
    ft_signal_pv = 2.0 * np.abs(ft_signal[:n]) / n  # get physical values for fft amplitudes by mult with 2/n

    plt.figure(dpi=600)
    plt.plot(ft_frequency_range, ft_signal_pv)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.show()

    index_mask = np.logical_and(ft_frequency_range >= min_frequency, ft_frequency_range <= max_frequency)
    # print(index_mask)
    ft_frequency_band = ft_signal_pv[index_mask]
    # ft_frequency_band = ft_signal_pv[np.logical_and(ft_frequency_range >= min_frequency,
    #                                                 ft_frequency_range <= max_frequency)]
    ft_band_range = ft_frequency_range[index_mask]

    plt.figure(dpi=600)
    plt.plot(ft_band_range, ft_frequency_band)
    plt.xlabel('Frequency Hz')
    plt.ylabel('A')
    plt.show()


if __name__ == '__main__':
    main()
