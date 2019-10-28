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
import os
from os import listdir
from os.path import isfile, join
import statistics


def main():
    # todo: solve I/O error, write to csv won't create a file
    # todo: revisit the whole console feedback to make sure everything works
    # todo: implement input to add rating to the dictionary
    # todo: create a clear console log for every file processed.
    # todo: check if a segment is rejected..if so..make it visible in the name of the saved file
    # ----------------- DATA EXTRACTION ----------------- #
    label = 'FEATURE EXTRACTION'
    print_header(program_label=label)

    # Get user input
    folder = get_folder_from_user(default_folder_name='ProcessingRepository')
    if not folder:
        print("We can't search file in this location.")
        return
    else:
        print(folder)

    # set info display
    set_verbose = False
    set_save = True
    set_plot = False

    # Get user input: subject name
    subject = input('Please enter subject initials.')
    # Create a handle to identify files that should be analysed
    identifier = "_data_" + subject + "_"
    # Find all Files in the folder
    all_file_paths = [f for f in listdir(folder) if isfile(join(folder, f))]

    for fp in all_file_paths:
        file_name = fp
        print('-------------------------------------')
        print('Next Up:' + file_name)

        saving_name = fp[:-4]
        # Create a handle to identify files that should be analysed

        # Go through matches
        if identifier in file_name:
            print('Match! Processing file.')
            file_path = os.path.abspath(os.path.join(folder, file_name))
            stream_data = read_list_from_text_file(file_path=file_path)
            stream_data_float = [float(dp) for dp in stream_data]
            stream_array = np.array(stream_data_float)
            if 'bvp' in file_name:
                fs = 64
                print('Data type = bvp, sampling frequency set to ' + str(fs))

                # ----------------- BLOOD VOLUME PRESSURE ----------------- #

                # pre-processing
                peak_amplitudes, peak_locations = bvp_peak_detection(bvp_raw_data=stream_array, sampling_frequency=fs,
                                                                     verbose=set_verbose)
                inter_beat_intervals = get_inter_beat_intervals(peak_data=peak_locations)
                inter_beat_intervals_list = list(inter_beat_intervals)
                interpolated_nn_intervals, interpolated_inter_beat_intervals, validation_result = \
                    get_nn_intervals(inter_beat_intervals=inter_beat_intervals_list, low_ibi=300, high_ibi=2000,
                                     interpolation_method='linear', ectopic_beats_removal_method='kamath',
                                     verbose=set_verbose)
                # feature extraction
                time_domain_features = get_time_domain_features(interpolated_inter_beat_intervals)
                frequency_domain_features = get_frequency_domain_features(interpolated_nn_intervals)
                # save results
                write_dict_to_csv(my_dict=time_domain_features, file_name=saving_name + '_time_features',
                                  file_index=subject)
                write_dict_to_csv(my_dict=frequency_domain_features, file_name=saving_name + '_freq_features',
                                  file_index=subject)

                if set_save:
                    save_dict_to_mat(dictionary=time_domain_features, data_file_name=saving_name + '_',
                                     save_file_label='time_domain_features', verbose=set_verbose)
                    save_dict_to_mat(dictionary=frequency_domain_features, data_file_name=saving_name + '_',
                                     save_file_label='freq_domain_features', verbose=set_verbose)

                print('Processing done.')
                print('-------------------------------------')

                # plot results
                if set_plot:
                    plot_psd(interpolated_nn_intervals, method="welch")
                    interpolated_nn_intervals = [int(x) for x in interpolated_nn_intervals]
                    plot_distrib(interpolated_nn_intervals)

            elif 'gsr' in file_name:
                fs = 4
                print('Data type = gsr, sampling frequency set to ' + str(fs))

                # ----------------- GALVANIC SKIN RESPONSE ----------------- #

                # pre-processing
                gsr_fs = 4
                # gsr_raw = stream_data['E4_Gsr_data']
                gsr_raw = []
                for e in stream_data:
                    gsr_raw.append(float(e))

                if len(gsr_raw) > 0:
                    gsr_raw_array = np.array(gsr_raw)
                    # gsr_time = stream_data['E4_Gsr_time']
                    # gsr_time_array = np.array(gsr_time)
                    gsr_mov_avg = gsr_generate_moving_averages(data=gsr_raw_array, sampling_frequency=gsr_fs, window=4,
                                                               mode='same',
                                                               verbose=set_verbose)
                    # print(gsr_raw_array)
                    gsr_filtered = gsr_zero_phase_filtering(data=gsr_raw_array, sampling_frequency=gsr_fs, f_cut=1.0,
                                                            filter_order=4, verbose=set_verbose)
                    # feature extraction
                    gsr_min_zf = min(gsr_filtered)
                    gsr_max_zf = max(gsr_filtered)
                    gsr_mean_zf = statistics.mean(gsr_filtered)    # related to arousal , Lang
                    gsr_sd_zf = statistics.stdev(gsr_filtered)

                    gsr_min_ma = min(gsr_mov_avg)
                    gsr_max_ma = max(gsr_mov_avg)
                    gsr_mean_ma = statistics.mean(gsr_mov_avg)  # related to arousal , Lang
                    gsr_sd_ma = statistics.stdev(gsr_mov_avg)
                    # peaks per minute

                    gsr_features = {
                        'gsr_min_ma': gsr_min_ma,
                        'gsr_max_ma': gsr_max_ma,
                        'gsr_mean_ma': gsr_mean_ma,
                        'gsr_sd_ma': gsr_sd_ma,
                        'gsr_min_zf': gsr_min_zf,
                        'gsr_max_zf': gsr_max_zf,
                        'gsr_mean_zf': gsr_mean_zf,
                        'gsr_sd_zf': gsr_sd_zf
                    }

                    write_dict_to_csv(my_dict=gsr_features, file_name=saving_name + '_features', file_index=subject)

                    if set_save:
                        save_dict_to_mat(dictionary=gsr_features, data_file_name=saving_name + '_',
                                         save_file_label='features', verbose=set_verbose)
                    # plot results
                    if set_plot:
                        plt.figure()
                        plt.plot(gsr_raw_array)
                        plt.plot(gsr_filtered)
                        # plt.plot(gsr_mov_avg)
                        plt.show()

            elif 'temp' in file_name:
                fs = 4
                print('Data type = temp, sampling frequency set to ' + str(fs))

                # ----------------- TEMPERATURE ----------------- #

                # pre-processing
                temp_fs = 4
                # temp_raw = stream_data['E4_Temperature_data']
                temp_raw = []
                for e in stream_data:
                    temp_raw.append(float(e))

                if len(temp_raw) > 0:
                    temp_raw_array = np.array(temp_raw)
                    # temp_time = stream_data['E4_Temperature_time']
                    # temp_time_array = np.array(temp_time)

                    temp_mov_avg = gsr_generate_moving_averages(data=temp_raw_array, sampling_frequency=temp_fs,
                                                                window=5,
                                                                mode='same', verbose=set_verbose)
                    temp_filtered = gsr_zero_phase_filtering(data=temp_raw_array, sampling_frequency=temp_fs, f_cut=1.0,
                                                             filter_order=4, verbose=set_verbose)
                    # feature extraction
                    temp_min_ma = min(temp_mov_avg)
                    temp_max_ma = max(temp_mov_avg)
                    temp_mean_ma = statistics.mean(temp_mov_avg)
                    temp_sd_ma = statistics.stdev(temp_mov_avg)

                    temp_min_zf = min(temp_filtered)
                    temp_max_zf = max(temp_filtered)
                    temp_mean_zf = statistics.mean(temp_filtered)
                    temp_sd_zf = statistics.stdev(temp_filtered)

                    temp_features = {
                        'temp_min_ma': temp_min_ma,
                        'temp_max_ma': temp_max_ma,
                        'temp_mean_ma': temp_mean_ma,
                        'temp_sd_ma': temp_sd_ma,
                        'temp_min_zf': temp_min_zf,
                        'temp_max_zf': temp_max_zf,
                        'temp_mean_zf': temp_mean_zf,
                        'temp_sd_zf': temp_sd_zf
                    }

                    write_dict_to_csv(my_dict=temp_features, file_name=saving_name + '_features', file_index=subject)

                    if set_save:
                        save_dict_to_mat(dictionary=temp_features, data_file_name=saving_name + '_',
                                         save_file_label='features', verbose=set_verbose)
                    # plot results
                    if set_plot:
                        plt.figure()
                        plt.plot(temp_raw)
                        plt.plot(temp_mov_avg)
                        plt.show()

            elif 'tag' in file_name:
                fs = 0
                print('Data type = tag, sampling frequency set to ' + str(fs))
                # ----------------- TAGS ----------------- #

                # pre-processing

                # feature extraction

                # plot results

            else:
                print('Invalid data type. Please try again')
        else:
            print('No Match! Discarding file.')
            print('-------------------------------------')


if __name__ == '__main__':
    main()
