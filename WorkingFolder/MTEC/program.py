"""
Title: program.py
Author: Dominik Limbach
Date: 08.06.2019
Description:
    - main program handling all functionality
"""
from extract_data_from_device import print_header, get_folder_from_user, search_for_latest_file, parse_file_for_tag, \
    get_stream_data, get_stream_time
from peak_detecting_algorithm import peak_detection_bvp
from artifact_interpolation_algorithm import artifact_interpolation_bvp
from cubic_spline_interpolation import csi_resampling
from tcp_server import wait_for_new_data
from extract_data_from_device import print_header, get_folder_from_user, search_for_latest_file, parse_file_for_tag, \
    get_stream_data, get_stream_time

from bvp_preprocessing import *
from artifact_interpolation_algorithm import get_inter_beat_intervals
from extracting_features import (get_time_domain_features, get_frequency_domain_features,
                                 get_geometrical_features, get_csi_cvi_features,
                                 get_poincare_plot_features, get_sampen)

from plot import (plot_timeseries, plot_distrib, plot_psd, plot_poincare)
# global to check if a file has already been processed
currently_processed = 'none'
most_recently_processed = 'none'


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

    # ---------------------------------------- print program header -------------------------------------------------- #
    print_header()
    # ---------------------------------------- request user input ---------------------------------------------------- #
    folder = get_folder_from_user()
    if not folder:
        print("We can't search file in this location.")
        return
    else:
        print(folder)
    # ---------------------------------------- start server / log to stream ------------------------------------------ #
    while 1:  # turn off for testing
        server_status = wait_for_new_data()  # turn off for testing
        # server_status = 'go'
        if server_status == 'read stop':
            continue                            # changed from: break
        else:
            # ---------------------------------------- data preparation ---------------------------------------------- #
            search_text = 'rec'
            latest_file = search_for_latest_file(folder, search_text)
            # update current file
            global currently_processed
            currently_processed = latest_file
            # check if file has already been processed
            global most_recently_processed
            if currently_processed == most_recently_processed:
                continue
            else:
                # could make a list of tags and go through it
                stream_tag = 'E4_Bvp'
                stream = parse_file_for_tag(currently_processed, stream_tag)
                # print(stream)
                raw_data = get_stream_data(stream)
                time_in_seconds = get_stream_time(stream)
                # set current file to most recently processed in preparation for the next loop
                most_recently_processed = currently_processed
                # ------------------------------------ data pre-processing ------------------------------------------- #
                peak_amplitudes, peak_locations = bvp_peak_detection(raw_data)
                inter_beat_intervals = get_inter_beat_intervals(peak_data=peak_locations)

                # inter_beat_intervals_list contains integer values of RR-interval
                inter_beat_intervals_list = list(inter_beat_intervals)

                interpolated_nn_intervals, interpolated_inter_beat_intervals, validation_result = \
                    get_nn_intervals(inter_beat_intervals=inter_beat_intervals_list, low_ibi=300, high_ibi=2000,
                                     interpolation_method='linear', ectopic_beats_removal_method='kamath', verbose=True)

                time_domain_features = get_time_domain_features(interpolated_inter_beat_intervals)
                frequency_domain_features = get_frequency_domain_features(interpolated_nn_intervals)

                plot_psd(interpolated_nn_intervals, method="welch")
                interpolated_nn_intervals = [int(x) for x in interpolated_nn_intervals]
                plot_distrib(interpolated_nn_intervals)

                # peak_amplitudes, peak_locations = peak_detection_bvp(raw_data=raw_data)
                # print(type(peak_locations))
                # interpolated_ibi_data = artifact_interpolation_bvp(peak_locations=peak_locations)

                # # ------------------------------------ bvp feature extraction ---------------------------------------- #
                #
                # # time domain
                # # frequency domain
                # csi_resampling(data=interpolated_ibi_data, sampling_frequency=64, resampling_frequency=7)
                # # non-linear methods

                print()
                print('Finished processing.')
                print('--------------------------------------------------')


if __name__ == '__main__':
    main()
