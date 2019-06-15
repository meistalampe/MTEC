from extract_data_from_device import print_header, get_folder_from_user, search_for_latest_file, parse_file_for_tag, get_stream_data, get_stream_time
from data_preprocessing import butter_lowpass_filter, butter_lowpass, detrend_the_signal, find_negative_peaks_in_signal, artifact_removal_filter, pass_only_valid_peaks
from feature_extraction import feature_extraction_frequency_domain, feature_extraction_time_domain, feature_extraction_non_linear
from tcp_server import wait_for_new_data

import math
import pandas as pd
import numpy as np
import pywt
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft


def main():
    print_header()  # imported from process data
    folder = "E:\GitHub\MTEC\WorkingFolder\MTEC\DataRepository"
    # folder = get_folder_from_user()
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
        print(type(raw_data))
        print(len(raw_data))
        print(raw_data)
        time = get_stream_time(stream)


if __name__ == '__main__':
    main()
