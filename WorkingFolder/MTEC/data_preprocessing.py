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

def artifact_removal_filter():
    pass


def pass_only_valid_peaks():
    pass


if __name__ == '__main__':
    main()
