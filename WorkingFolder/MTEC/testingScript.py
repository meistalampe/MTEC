from extract_data_from_device import print_header, get_folder_from_user, search_for_latest_file, parse_file_for_tag, \
    get_stream_data, get_stream_time
from data_preprocessing import butter_lowpass_filter, butter_lowpass, detrend_the_signal, \
    find_negative_peaks_in_signal, get_frequency_bands, find_positive_peaks_in_signal, pass_only_valid_peaks, \
    bandpower, plot_spectrum_methods, get_interpolated_ibi
from feature_extraction import feature_extraction_frequency_domain, feature_extraction_time_domain, feature_extraction_non_linear
from tcp_server import wait_for_new_data

import numpy as np
import matplotlib.pyplot as plt


def main():
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

    # filtering (lowpass butterworth, at 3.6 Hz)
    filter_order = 6
    sampling_frequency = 64  # Hz
    max_heart_rate = 220  # bpm
    cutoff_frequency = round((max_heart_rate / 60), ndigits=3)  # desired max frequency in Hz

    # filter the raw signal data
    filtered_data = butter_lowpass_filter(raw_data, cutoff_frequency, sampling_frequency, filter_order)
    # # display filtered signal
    #
    # plt.subplot(2, 1, 2)
    # plt.plot(time_in_seconds, raw_data, 'b-', label='data')
    # plt.plot(time_in_seconds, filtered_data, 'g-', linewidth=2, label='filtered data')
    # plt.xlabel('Time [sec]')
    # plt.grid()
    # plt.legend()
    #
    # plt.subplots_adjust(hspace=0.35)
    # plt.show()
    #
    import pywt
    import matplotlib.pyplot as plt
    # x = time_in_seconds[0:1000]
    # y = filtered_data[0:1000]
    # coef, freqs = pywt.cwt(y, np.arange(1, 250), 'gaus1')
    # plt.matshow(coef)
    # plt.show()
    #
    # t = time_in_seconds
    # sig = filtered_data
    # widths = np.arange(1, 31)
    # cwtmatr, freqs = pywt.cwt(sig, widths, 'mexh')
    # plt.imshow(cwtmatr, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',
    #            vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())
    # plt.show()
    # detrend the filtered signal data
    detrend_data = detrend_the_signal(filtered_data)

    # peak detection
    negative_peaks, properties = find_negative_peaks_in_signal(detrend_data, sampling_frequency,
                                                               distance_factor=0.3, peak_prominence=25)
    threshold = 25
    positive_peaks, properties = find_positive_peaks_in_signal(detrend_data, peak_height=threshold)

    valid_peaks = pass_only_valid_peaks(negative_peaks, positive_peaks, sampling_frequency)
    # print('valid_peaks: ', valid_peaks)
    inter_beat_intervals = get_interpolated_ibi(valid_peaks)
    # print('ibi: ', inter_beat_intervals)

    # x = time_in_seconds
    # y = inter_beat_intervals
    # coef, freqs = pywt.cwt(y, np.arange(1, 250), 'gaus1')
    # plt.matshow(coef)
    # plt.show()
    #
    # t = time_in_seconds
    # sig = inter_beat_intervals
    # widths = np.arange(1, 31)
    # cwtmatr, freqs = pywt.cwt(sig, widths, 'mexh')
    # plt.imshow(cwtmatr, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',
    #            vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())
    # plt.show()

    frequency_band = get_frequency_bands(inter_beat_intervals, (0.02, 0.4))
    #
    # # trial code bandpower methods
    # data = inter_beat_intervals
    # sf = 64
    # # Multitaper delta power
    # bp = bandpower(data, sf, [0.0, 0.4], 'multitaper')
    # bp_rel = bandpower(data, sf, [0.0, 0.4], 'multitaper', relative=True)
    # print('Absolute delta power: %.3f' % bp)
    # print('Relative delta power: %.3f' % bp_rel)
    #
    # # Delta-beta ratio
    # # One advantage of the multitaper is that we don't need to define a window length.
    # db = bandpower(data, sf, [0.0, 0.4], 'multitaper') / bandpower(data, sf, [12, 30], 'multitaper')
    # # Ratio based on the relative power
    # db_rel = bandpower(data, sf, [0.0, 0.4], 'multitaper', relative=True) / \
    #          bandpower(data, sf, [0.0, 32], 'multitaper', relative=True)
    # print('Delta/beta ratio (absolute): %.3f' % db)
    # print('Delta/beta ratio (relative): %.3f' % db_rel)
    print()
    print('Finished processing.')
    print('--------------------------------------------------')
    # # Example: plot the 0.5 - 2 Hz band
    # plot_spectrum_methods(data, sf, 4, [0.5, 2], dB=True)


if __name__ == '__main__':
    main()
