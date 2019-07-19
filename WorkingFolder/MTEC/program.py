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
    find_negative_peaks_in_signal, get_frequency_bands, find_positive_peaks_in_signal, pass_only_valid_peaks, \
    bandpower, plot_spectrum_methods
from feature_extraction import feature_extraction_frequency_domain, feature_extraction_time_domain, feature_extraction_non_linear
from tcp_server import wait_for_new_data

import numpy as np
import matplotlib.pyplot as plt


def main():
    """ Main function process order:
        - print program header
        - request user input (data folder)
        - server start up
        - listen for client commands (on 'start' command: handle data processing, return to listening
                                      on 'stop' command: shut down server, stop program)

        Data processing process order:
        - track most recent file
        - scan file for data tag
        - extract data from file (resulting in two np.arrays (data, time))

        - run peak detection algorithm (filtering, clipping, squaring, moving averages, thresholding, block of interest,
                                        peak detection, block validation)
        - run artifact interpolation algorithm (calculate inter beat intervals, mark ectopic beats, mark ectopic beat
                                                sequences, calculate number of substitution intervals, interval
                                                dismissal, "linear interpolation")

        Data evaluation algorithm:
        - bvp recording
        - microcomputer digesting
        - artifact identification
        - "RR" data editing
        - "RR" interval rejection
        => Ibi data sequence
                |-----------------------------------------> - Interpolation
                v                                           - Resampling
        => TIME DOMAIN                                      => FREQUENCY DOMAIN
               HRV                                                  HRV
        """
    print_header()  # imported from process data

    folder = get_folder_from_user()
    if not folder:
        print("We can't search file in this location.")
        return
    else:
        print(folder)

    while 1:                                                          # turn off for testing
        server_status = wait_for_new_data()                           # turn off for testing

        if server_status == 'read stop':
            break
        else:

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
            #
            # # detrend the filtered signal data
            # detrend_data = detrend_the_signal(filtered_data)
            #
            # # peak detection
            # negative_peaks, properties = find_negative_peaks_in_signal(detrend_data, sampling_frequency,
            #                                                            distance_factor=0.3, peak_prominence=25)
            # threshold = 25
            # positive_peaks, properties = find_positive_peaks_in_signal(detrend_data, peak_height=threshold)
            # valid_peaks = pass_only_valid_peaks(negative_peaks, positive_peaks)
            #
            # inter_beat_intervals = np.diff(valid_peaks)
            # frequency_band = get_frequency_bands(inter_beat_intervals, (0.0, 0.4))
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
