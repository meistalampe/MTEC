"""
Title: program.py
Author: Dominik Limbach
Date: 08.06.2019
Description:
    - main program handling all functionality
"""
from extract_data_from_device import print_header, get_folder_from_user, search_for_latest_file, parse_file_for_tag, get_stream_data, get_stream_time
from data_preprocessing import low_pass_signal_filter, detrend_the_signal, find_peaks_in_signal, artifact_removal_filter, pass_only_valid_peaks
from feature_extraction import feature_extraction_frequency_domain, feature_extraction_time_domain, feature_extraction_non_linear
from tcp_server import wait_for_new_data

import matplotlib.pyplot as plt


def main():

    print_header()  # imported from process data

    folder = get_folder_from_user()
    if not folder:
        print("We can't search file in this location.")
        return
    else:
        print(folder)

    while 1:
        command = wait_for_new_data()
        print('Valid command received. Start processing...')

        search_text = 'rec'
        latest_file = search_for_latest_file(folder, search_text)
        # print(latest_file)
        stream_tag = 'E4_Gsr'
        stream = parse_file_for_tag(latest_file, stream_tag)
        # print(stream)
        data = get_stream_data(stream)
        time = get_stream_time(stream)
        plt.plot(data)
        plt.show()
        print('Finished processing.')


if __name__ == '__main__':
    main()
