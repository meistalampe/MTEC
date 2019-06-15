"""
Title: program.py
Author: Dominik Limbach
Date: 08.06.2019
Description:
    - main program handling all functionality
"""
from extract_data_from_device import print_header, get_folder_from_user, search_for_latest_file, parse_file_for_tag, \
    get_stream_data, get_stream_time
from data_preprocessing import butter_lowpass_filter, butter_lowpass, detrend_the_signal, \
    find_negative_peaks_in_signal, get_frequency_bands, find_positive_peaks_in_signal, pass_only_valid_peaks
from feature_extraction import feature_extraction_frequency_domain, feature_extraction_time_domain, feature_extraction_non_linear
from tcp_server import wait_for_new_data

import numpy as np
import matplotlib.pyplot as plt


def main():

    print_header()  # imported from process data

    folder = get_folder_from_user()
    if not folder:
        print("We can't search file in this location.")
        return
    else:
        print(folder)

    # while 1:                                                          # turn off for testing
        # command = wait_for_new_data()                                 # turn off for testing
        print('Valid command received. Start processing...')

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
        # display filtered signal

        plt.subplot(2, 1, 2)
        plt.plot(time_in_seconds, raw_data, 'b-', label='data')
        plt.plot(time_in_seconds, filtered_data, 'g-', linewidth=2, label='filtered data')
        plt.xlabel('Time [sec]')
        plt.grid()
        plt.legend()

        plt.subplots_adjust(hspace=0.35)
        plt.show()

        # detrend the filtered signal data
        detrend_data = detrend_the_signal(filtered_data)

        # peak detection
        negative_peaks, properties = find_negative_peaks_in_signal(detrend_data, sampling_frequency,
                                                                   distance_factor=0.3, peak_prominence=25)
        threshold = 25
        positive_peaks, properties = find_positive_peaks_in_signal(detrend_data, sampling_frequency,
                                                                   distance_factor=0.3, peak_height=threshold)
        valid_peaks = pass_only_valid_peaks(negative_peaks, positive_peaks)

        inter_beat_intervals = np.diff(valid_peaks)
        frequency_band = get_frequency_bands(inter_beat_intervals, (0.0, 0.4))

        print('Finished processing.')


if __name__ == '__main__':
    main()
