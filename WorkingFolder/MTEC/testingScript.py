import math

from extract_data_from_device import print_header, get_folder_from_user, search_for_latest_file, parse_file_for_tag, \
    get_stream_data, get_stream_time

from bvp_preprocessing import *
from artifact_interpolation_algorithm import get_inter_beat_intervals
from extracting_features import (get_time_domain_features, get_frequency_domain_features,
                                 get_geometrical_features, get_csi_cvi_features,
                                 get_poincare_plot_features, get_sampen)

from plot import (plot_timeseries, plot_distrib, plot_psd, plot_poincare)


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
    raw_data = get_stream_data(stream=stream)
    time_in_seconds = get_stream_time(stream=stream)
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


if __name__ == '__main__':
    main()
