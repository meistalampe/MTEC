import os
import collections
import numpy as np
from empatica_data_extraction import *


def main():
    create_data_samples()


def create_data_samples(repository_name: str = 'ClassificationRepository', folder_name: str = 'Datapoints'):
    """
    A function that loads all feature dictionaries from csv files  in a certain repository and creates datasample arrays
    for machine learning algorithms.

    Parameters
    ---------
    repository_name: str
        name of the general repository the feature files are located
    folder_name: str
        name of the datapoint folder, holds all samples in the form of feature files
    Returns
    ---------

    References
    ----------
    """
    print_header(program_label='Build Dataset')
    # get user input (folder)
    folder = input('Where is your data file located? [Press <enter> to use default path]: ')
    # check if input is empty, if so return default path
    if not folder or not folder.strip():
        print('Using default path.')
        print()
        # default_folder = 'DataRepository'
        folder_path = os.path.abspath(os.path.join('.', 'MTEC', repository_name, folder_name))

    # check if input path is a directory
    elif not os.path.isdir(folder):
        print('Input is not a valid folder path.')
        folder_path = ''
    # if input path is a directory return it
    else:
        folder_path = os.path.abspath(os.path.join('.', 'MTEC', repository_name, folder))

    # path verification
    # print(folder_path)

    # find all feature files
    # list holding all filenames in folder
    all_files = []
    # search folder for files with names matching search_text
    search_text = '.txt'
    for entry in os.scandir(folder_path):
        if entry.name.endswith(search_text) and entry.is_file():
            # file_size = str(os.path.getsize(entry))
            # print(entry.name + '    size: ' + file_size + 'Bytes ')
            all_files.append(entry)

    # print all files
    # print(all_files)

    # separate all_files by subject
    feature_data = {
        'subject_names': ['_ap_', '_ar_', '_es_', '_fw_', '_ka_', '_lb_', '_lp_', '_lw_', '_mb_', '_mch_', '_md_',
                          '_mf_', '_rs_'],  # - pg
        '_ap_files': list([]),
        '_ar_files': list([]),
        '_es_files': list([]),
        '_fw_files': list([]),
        '_ka_files': list([]),
        '_lb_files': list([]),
        '_lp_files': list([]),
        '_lw_files': list([]),
        '_mb_files': list([]),
        '_mch_files': list([]),
        '_md_files': list([]),
        '_mf_files': list([]),
        '_rs_files': list([])
    }

    for f in all_files:
        if feature_data['subject_names'][0] in f.name:
            # ap
            feature_data['_ap_files'].append(f)
        elif feature_data['subject_names'][1] in f.name:
            # ar
            feature_data['_ar_files'].append(f)
        elif feature_data['subject_names'][2] in f.name:
            # es
            feature_data['_es_files'].append(f)
        elif feature_data['subject_names'][3] in f.name:
            # fw
            feature_data['_fw_files'].append(f)
        elif feature_data['subject_names'][4] in f.name:
            # ka
            feature_data['_ka_files'].append(f)
        elif feature_data['subject_names'][5] in f.name:
            # lb
            feature_data['_lb_files'].append(f)
        elif feature_data['subject_names'][6] in f.name:
            # lp
            feature_data['_lp_files'].append(f)
        elif feature_data['subject_names'][7] in f.name:
            # lw
            feature_data['_lw_files'].append(f)
        elif feature_data['subject_names'][8] in f.name:
            # mb
            feature_data['_mb_files'].append(f)
        elif feature_data['subject_names'][9] in f.name:
            # mch
            feature_data['_mch_files'].append(f)
        elif feature_data['subject_names'][10] in f.name:
            # md
            feature_data['_md_files'].append(f)
        elif feature_data['subject_names'][11] in f.name:
            # mf
            feature_data['_mf_files'].append(f)
        elif feature_data['subject_names'][12] in f.name:
            # rs
            feature_data['_rs_files'].append(f)

    # final product
    # each row of data_points holds all features for one measurement
    data_points = list([])
    # each element of labels holds the corresponding label to every datapoint in data_points
    labels = list([])
    # complete feature list shows the order of features in data_points i.e. names for each column
    complete_feat_list = list([])

    # create dataset from subject files
    for s in feature_data['subject_names']:
        # str to find subject related files in the feature dictionary
        dict_element_name = s + 'files'
        # create a main dictionary to hold all features of all the data points until they are assigned by datapoints
        # the goal is to have a datapoint for each of the 8 measured segments , each datapoint should have all features
        # from bvp, gsr and temp for this segment that means the dictionary has to fit 3x8 + 8 + 8  segments
        data_segments = {
            'baseline_bvp_time': list([]),
            'baseline_bvp_freq': list([]),
            'baseline_bvp_nl': list([]),
            'baseline_gsr_': list([]),
            'baseline_temp_': list([]),

            'cd_one_bvp_time': list([]),
            'cd_one_bvp_freq': list([]),
            'cd_one_bvp_nl': list([]),
            'cd_one_gsr_': list([]),
            'cd_one_temp_': list([]),

            'cd_two_bvp_time': list([]),
            'cd_two_bvp_freq': list([]),
            'cd_two_bvp_nl': list([]),
            'cd_two_gsr_': list([]),
            'cd_two_temp_': list([]),

            'cd_three_bvp_time': list([]),
            'cd_three_bvp_freq': list([]),
            'cd_three_bvp_nl': list([]),
            'cd_three_gsr_': list([]),
            'cd_three_temp_': list([]),

            'emotion_one_bvp_time': list([]),
            'emotion_one_bvp_freq': list([]),
            'emotion_one_bvp_nl': list([]),
            'emotion_one_gsr_': list([]),
            'emotion_one_temp_': list([]),

            'emotion_two_bvp_time': list([]),
            'emotion_two_bvp_freq': list([]),
            'emotion_two_bvp_nl': list([]),
            'emotion_two_gsr_': list([]),
            'emotion_two_temp_': list([]),

            'stress_one_bvp_time': list([]),
            'stress_one_bvp_freq': list([]),
            'stress_one_bvp_nl': list([]),
            'stress_one_gsr_': list([]),
            'stress_one_temp_': list([]),

            'stress_two_bvp_time': list([]),
            'stress_two_bvp_freq': list([]),
            'stress_two_bvp_nl': list([]),
            'stress_two_gsr_': list([]),
            'stress_two_temp_': list([]),

            '_bvp_time_feat_list': list([]),
            '_bvp_freq_feat_list': list([]),
            '_bvp_nl_feat_list': list([]),
            '_gsr__feat_list': list([]),
            '_temp__feat_list': list([])
        }
        # go through all subject related entries
        for e in feature_data[dict_element_name]:
            # select all files from the same segment (=data point)
            # create file path from folder path and file name
            file_path = os.path.abspath(os.path.join(folder_path, e))

            # initiate tags
            segment_tag = ''
            type_tag = ''
            feat_tag = ''
            # initiate indices
            start_at_row = 0
            end_at_row = -1
            index_correction = 0

            # divide by data type to select relevant features
            if '_bvp_' in e.name:
                type_tag = '_bvp'
                if '_time_features_' in e.name:
                    # interesting rows for bvp time features are taken from no artifacts ibi intervals
                    start_at_row = 20
                    end_at_row = 35
                    feat_tag = '_time'

                elif '_freq_features_' in e.name:
                    # interesting rows for bvp freq features are taken from interpolated nn-intervals
                    start_at_row = 11
                    end_at_row = 17
                    feat_tag = '_freq'
                elif '_non_linear_features' in e.name:
                    # interesting rows for bvp non linear features are taken from no artifacts ibi intervals
                    start_at_row = 7
                    end_at_row = 9
                    feat_tag = '_nl'

            elif '_gsr_' in e.name:
                type_tag = '_gsr'
                # for gsr and temp data we want to read the whole file
                start_at_row = 1
                end_at_row = 18
                feat_tag = '_'
            elif '_temp_' in e.name:
                type_tag = '_temp'
                # for gsr and temp data we want to read the whole file
                start_at_row = 1
                end_at_row = 18
                feat_tag = '_'
            else:
                type_tag = 'invalid'
                feat_tag = 'invalid'
                print('Error: Invalid Type or Feature tag.')

            # select segment by tag
            if '_baseline_' in e.name:
                segment_tag = 'baseline'
                index_correction = 0

            elif '_cd_one_' in e.name:
                segment_tag = 'cd_one'
                index_correction = 0

            elif '_cd_two_' in e.name:
                segment_tag = 'cd_two'
                index_correction = 0

            elif '_cd_three_' in e.name:
                segment_tag = 'cd_three'
                index_correction = 0

            elif '_emotion_one_' in e.name:
                segment_tag = 'emotion_one'
                index_correction = 1

            elif '_emotion_two_' in e.name:
                segment_tag = 'emotion_two'
                index_correction = 1

            elif '_stress_one_' in e.name:
                segment_tag = 'stress_one'
                index_correction = 1

            elif 'stress_two' in e.name:
                segment_tag = 'stress_two'
                index_correction = 1

            else:
                segment_tag = 'invalid'
                print('Error: Segment tag could not be assigned.')

            # load entry content into a list
            dict_name = segment_tag + type_tag + feat_tag
            dict_feat_list = type_tag + feat_tag + '_feat_list'
            current_dict = read_csv_from_text_file(file_path=file_path, read_from_row=start_at_row + index_correction,
                                                   read_to_row=end_at_row + index_correction)

            for key in current_dict:
                data_segments[dict_name].append(current_dict[key])
                data_segments[dict_feat_list].append(key)

        seg_tags = ['baseline', 'cd_one', 'cd_two', 'cd_three', 'emotion_one', 'emotion_two', 'stress_one', 'stress_two']
        ft_tags = ['_bvp_time', '_bvp_freq', '_bvp_nl', '_gsr_', '_temp_']
        ls_tags = ['_bvp_time_feat_list', '_bvp_freq_feat_list', '_bvp_nl_feat_list', '_gsr__feat_list',
                   '_temp__feat_list']

        label = 0
        for t in seg_tags:
            new_data_point = list([])
            for f in ft_tags:
                new_data_point += data_segments[t + f]

            data_points.append(new_data_point)

            if t == seg_tags[0]:
                label = 0
            elif t in (seg_tags[1], seg_tags[2], seg_tags[3]):
                label = 1
            elif t in (seg_tags[4], seg_tags[5]):
                label = 2
            elif t in (seg_tags[6], seg_tags[7]):
                label = 3

            labels.append(label)

        # for lt in ls_tags:
            # complete_feat_list.append(data_segments[])


if __name__ == '__main__':
    main()
