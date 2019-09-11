from empatica_data_extraction import *
from cubic_spline_interpolation import *
from bvp_preprocessing import *
from gsr_preprocessing import *
from artifact_interpolation_algorithm import get_inter_beat_intervals
from extracting_features import (get_time_domain_features, get_frequency_domain_features,
                                 get_geometrical_features, get_csi_cvi_features,
                                 get_poincare_plot_features, get_sampen)

from plot import (plot_timeseries, plot_distrib, plot_psd, plot_poincare)
import numpy as np
import matplotlib.pyplot as plt


def main():
    # ----------------- DATA EXTRACTION ----------------- #
    label = 'MTEC APP'
    print_header(program_label=label)

    # Get user input
    folder = get_folder_from_user(default_folder_name='DataRepository')
    if not folder:
        print("We can't search file in this location.")
        return
    else:
        print(folder)

    # set info display
    set_verbose = False
    set_save = False
    set_plot = True
    #  Get data folder
    search_text = 'rec'
    stream_data = extract_all(folder=folder, file_label=search_text, verbose=set_verbose)

    # ----------------- BLOOD VOLUME PRESSURE ----------------- #

    # pre-processing
    peak_amplitudes, peak_locations = bvp_peak_detection(bvp_raw_data=stream_data['E4_Bvp_data'], verbose=set_verbose)
    inter_beat_intervals = get_inter_beat_intervals(peak_data=peak_locations)
    inter_beat_intervals_list = list(inter_beat_intervals)
    interpolated_nn_intervals, interpolated_inter_beat_intervals, validation_result = \
        get_nn_intervals(inter_beat_intervals=inter_beat_intervals_list, low_ibi=300, high_ibi=2000,
                         interpolation_method='linear', ectopic_beats_removal_method='kamath', verbose=set_verbose)
    # feature extraction
    time_domain_features = get_time_domain_features(interpolated_inter_beat_intervals)
    frequency_domain_features = get_frequency_domain_features(interpolated_nn_intervals)
    # save results
    if set_save:
        save_dict_to_mat(dictionary=time_domain_features, data_file_name=stream_data['Filename'],
                         save_file_label='time_domain_features', verbose=set_verbose)
    # plot results
    if set_plot:
        plot_psd(interpolated_nn_intervals, method="welch")
        interpolated_nn_intervals = [int(x) for x in interpolated_nn_intervals]
        plot_distrib(interpolated_nn_intervals)

    # ----------------- GALVANIC SKIN RESPONSE ----------------- #

    # pre-processing
    gsr_fs = 4
    gsr_raw = stream_data['E4_Gsr_data']

    if len(gsr_raw) > 0:
        gsr_raw_array = np.array(gsr_raw)
        gsr_time = stream_data['E4_Gsr_time']
        gsr_time_array = np.array(gsr_time)
        gsr_mov_avg = gsr_generate_moving_averages(data=gsr_raw_array, sampling_frequency=gsr_fs, window=4, mode='same',
                                                   verbose=set_verbose)
        print(gsr_raw_array)
        gsr_filtered = gsr_zero_phase_filtering(data=gsr_raw_array, sampling_frequency=gsr_fs, f_cut=1.0,
                                                filter_order=4, verbose=set_verbose)
        # feature extraction

        # plot results
        if set_plot:
            plt.figure()
            plt.plot(gsr_time, gsr_raw_array)
            plt.plot(gsr_time, gsr_filtered)
            plt.plot(gsr_time, gsr_mov_avg)
            plt.show()

    # ----------------- TEMPERATURE ----------------- #

    # pre-processing
    temp_fs = 4
    temp_raw = stream_data['E4_Temperature_data']
    if len(temp_raw) > 0:
        temp_raw_array = np.array(temp_raw)
        temp_time = stream_data['E4_Temperature_time']
        temp_time_array = np.array(temp_time)

        temp_mov_avg = gsr_generate_moving_averages(data=temp_raw_array, sampling_frequency=temp_fs, window=5,
                                                    mode='same', verbose=set_verbose)
        # feature extraction

        # plot results
        if set_plot:
            plt.figure()
            plt.plot(temp_time, temp_raw)
            plt.plot(temp_time, temp_mov_avg)
            plt.show()
    # ----------------- TAGS ----------------- #

    # pre-processing

    # feature extraction

    # plot results


if __name__ == '__main__':
    main()
