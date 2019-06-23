import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import butter, lfilter, freqz, signaltools, find_peaks, find_peaks_cwt, welch
from scipy.integrate import simps


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


#def find_positive_peaks_in_signal(data, sampling_frequency, distance_factor, peak_height):
def find_positive_peaks_in_signal(data, peak_height):
    #min_peak_distance = distance_factor * sampling_frequency * 0.01     # extra factor to minimize it
    #peaks, properties = find_peaks(data, distance=min_peak_distance, height=peak_height)
    peaks, properties = find_peaks(data, height=peak_height)
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


# https://raphaelvallat.com/bandpower.html
def bandpower(data, sf, band, method='welch', window_sec=None, relative=False):
    """Compute the average power of the signal x in a specific frequency band.

    Requires MNE-Python >= 0.14.

    Parameters
    ----------
    data : 1d-array
      Input signal in the time-domain.
    sf : float
      Sampling frequency of the data.
    band : list
      Lower and upper frequencies of the band of interest.
    method : string
      Periodogram method: 'welch' or 'multitaper'
    window_sec : float
      Length of each window in seconds. Useful only if method == 'welch'.
      If None, window_sec = (1 / min(band)) * 2.
    relative : boolean
      If True, return the relative power (= divided by the total power of the signal).
      If False (default), return the absolute power.

    Return
    ------
    bp : float
      Absolute or relative band power.
    """
    from scipy.signal import welch
    from scipy.integrate import simps
    from mne.time_frequency import psd_array_multitaper

    band = np.asarray(band)
    low, high = band

    # Compute the modified periodogram (Welch)
    if method == 'welch':
        if window_sec is not None:
            nperseg = window_sec * sf
        else:
            nperseg = (2 / low) * sf

        freqs, psd = welch(data, sf, nperseg=nperseg)

    elif method == 'multitaper':
        psd, freqs = psd_array_multitaper(data, sf, adaptive=True,
                                          normalization='full', verbose=0)

    # Frequency resolution
    freq_res = freqs[1] - freqs[0]

    # Find index of band in frequency vector
    idx_band = np.logical_and(freqs >= low, freqs <= high)

    # Integral approximation of the spectrum using parabola (Simpson's rule)
    bp = simps(psd[idx_band], dx=freq_res)

    if relative:
        bp /= simps(psd, dx=freq_res)
    return bp


def plot_spectrum_methods(data, sf, window_sec, band=None, dB=False):
    """Plot the periodogram, Welch's and multitaper PSD.

    Requires MNE-Python >= 0.14.

    Parameters
    ----------
    data : 1d-array
        Input signal in the time-domain.
    sf : float
        Sampling frequency of the data.
    band : list
        Lower and upper frequencies of the band of interest.
    window_sec : float
        Length of each window in seconds for Welch's PSD
    dB : boolean
        If True, convert the power to dB.
    """
    from mne.time_frequency import psd_array_multitaper
    from scipy.signal import welch, periodogram

    sns.set(style="white", font_scale=1.2)
    # Compute the PSD
    freqs, psd = periodogram(data, sf)
    freqs_welch, psd_welch = welch(data, sf, nperseg=window_sec*sf)
    psd_mt, freqs_mt = psd_array_multitaper(data, sf, adaptive=True,
                                            normalization='full', verbose=0)
    sharey = False

    # Optional: convert power to decibels (dB = 10 * log10(power))
    if dB:
        psd = 10 * np.log10(psd)
        psd_welch = 10 * np.log10(psd_welch)
        psd_mt = 10 * np.log10(psd_mt)
        sharey = True

    # Start plot
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4), sharex=True, sharey=sharey)
    # Stem
    sc = 'slategrey'
    ax1.stem(freqs, psd, linefmt=sc, basefmt=" ", markerfmt=" ")
    ax2.stem(freqs_welch, psd_welch, linefmt=sc, basefmt=" ", markerfmt=" ")
    ax3.stem(freqs_mt, psd_mt, linefmt=sc, basefmt=" ", markerfmt=" ")
    # Line
    lc, lw = 'k', 2
    ax1.plot(freqs, psd, lw=lw, color=lc)
    ax2.plot(freqs_welch, psd_welch, lw=lw, color=lc)
    ax3.plot(freqs_mt, psd_mt, lw=lw, color=lc)
    # Labels and axes
    ax1.set_xlabel('Frequency (Hz)')
    if not dB:
        ax1.set_ylabel('Power spectral density (V^2/Hz)')
    else:
        ax1.set_ylabel('Decibels (dB / Hz)')
    ax1.set_title('Periodogram')
    ax2.set_title('Welch')
    ax3.set_title('Multitaper')
    if band is not None:
        ax1.set_xlim(band)
    ax1.set_ylim(ymin=0)
    ax2.set_ylim(ymin=0)
    ax3.set_ylim(ymin=0)
    sns.despine()


if __name__ == '__main__':
    main()
