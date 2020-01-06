import os
import collections
import numpy as np
from empatica_data_extraction import *

__all__ = ['create_data_samples']


def main():
    datasets = create_data_samples()


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
    data_points: nd.array
        2 dimensional np.array, each row is a single data point (i.e. one measured segment), each column is a single
        feature (order of features is documented in feature list)
    labels: nd.array
        1 dimensional np.array, each column is the label corresponding to the same number row in data points,
        a total of 4 different labels, 0=baseline, 1=cd, 2=emotion, 3=stress
    labels_bin: nd.array
        same as labels but only 2 different labels. 0=baseline, 1=no baseline
    complete_feat_list: List(str)
        a list of all features in the order they are listed for each data point

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
    # same as array
    # data_point_array = np.empty([105, 62])
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
            'baseline_label_': list([0]),

            'cd_one_bvp_time': list([]),
            'cd_one_bvp_freq': list([]),
            'cd_one_bvp_nl': list([]),
            'cd_one_gsr_': list([]),
            'cd_one_temp_': list([]),
            'cd_one_label_': list([1]),

            'cd_two_bvp_time': list([]),
            'cd_two_bvp_freq': list([]),
            'cd_two_bvp_nl': list([]),
            'cd_two_gsr_': list([]),
            'cd_two_temp_': list([]),
            'cd_two_label_': list([1]),

            'cd_three_bvp_time': list([]),
            'cd_three_bvp_freq': list([]),
            'cd_three_bvp_nl': list([]),
            'cd_three_gsr_': list([]),
            'cd_three_temp_': list([]),
            'cd_three_label_': list([1]),

            'emotion_one_bvp_time': list([]),
            'emotion_one_bvp_freq': list([]),
            'emotion_one_bvp_nl': list([]),
            'emotion_one_gsr_': list([]),
            'emotion_one_temp_': list([]),
            'emotion_one_label_': list([2]),

            'emotion_two_bvp_time': list([]),
            'emotion_two_bvp_freq': list([]),
            'emotion_two_bvp_nl': list([]),
            'emotion_two_gsr_': list([]),
            'emotion_two_temp_': list([]),
            'emotion_two_label_': list([3]),

            'stress_one_bvp_time': list([]),
            'stress_one_bvp_freq': list([]),
            'stress_one_bvp_nl': list([]),
            'stress_one_gsr_': list([]),
            'stress_one_temp_': list([]),
            'stress_one_label_': list([4]),

            'stress_two_bvp_time': list([]),
            'stress_two_bvp_freq': list([]),
            'stress_two_bvp_nl': list([]),
            'stress_two_gsr_': list([]),
            'stress_two_temp_': list([]),
            'stress_two_label_': list([5]),

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
                if '_gsr_' in e.name:
                    index_correction = 0
                elif '_temp_' in e.name:
                    index_correction = 0
                else:
                    index_correction = 1

            elif '_emotion_two_' in e.name:
                segment_tag = 'emotion_two'
                if '_gsr_' in e.name:
                    index_correction = 0
                elif '_temp_' in e.name:
                    index_correction = 0
                else:
                    index_correction = 1

            elif '_stress_one_' in e.name:
                segment_tag = 'stress_one'
                if '_gsr_' in e.name:
                    index_correction = 0
                elif '_temp_' in e.name:
                    index_correction = 0
                else:
                    index_correction = 1

            elif 'stress_two' in e.name:
                segment_tag = 'stress_two'
                if '_gsr_' in e.name:
                    index_correction = 0
                elif '_temp_' in e.name:
                    index_correction = 0
                else:
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

        seg_tags = ['baseline', 'cd_one', 'cd_two', 'cd_three', 'emotion_one', 'emotion_two', 'stress_one',
                    'stress_two']
        ft_tags = ['_bvp_time', '_bvp_freq', '_bvp_nl', '_gsr_', '_temp_', '_label_']
        # ls_tags = ['_bvp_time_feat_list', '_bvp_freq_feat_list', '_bvp_nl_feat_list', '_gsr__feat_list',
        #           '_temp__feat_list']

        label = 0
        for t in seg_tags:
            new_data_point = list([])
            for f in ft_tags:
                new_data_point += data_segments[t + f]

            if len(new_data_point) == 63:
                data_points.append(new_data_point)

                if t == seg_tags[0]:
                    label = 0
                elif t in (seg_tags[1], seg_tags[2], seg_tags[3]):
                    label = 1
                elif t in (seg_tags[4]):
                    label = 2
                elif t in (seg_tags[5]):
                    label = 3
                elif t in (seg_tags[6]):
                    label = 4
                elif t in (seg_tags[7]):
                    label = 5
            else:
                placeholder_row = [0] * 63
                data_points.append(placeholder_row)
                label = -1

            labels.append(label)
        # Note: The last feature is only for verification purposes, should not be considered in learning algorithm
        complete_feat_list = \
            data_segments['_bvp_time_feat_list'][0:16] + data_segments['_bvp_freq_feat_list'][0:7] + \
            data_segments['_bvp_nl_feat_list'][0:3] + data_segments['_gsr__feat_list'][0:18] + \
            data_segments['_temp__feat_list'][0:18] + list(['label'])

    data_point_array = np.empty((0, len(complete_feat_list)))
    for dp in data_points:
        # print(len(dp))
        new_row = np.array(dp)
        data_point_array = np.vstack((data_point_array, new_row))

    # datasets that use all samples

    # ------------------- Complete ------------------- #
    complete_description = "complete dataset, with a single label for each state, except cds " \
                           "[baseline = 0, cd (1-3) =1, emotion_one = 2, emotion_two = 3, stress_one = 4, " \
                           "stress_two = 5], Cave: remove last feature!"
    # convert label list to array
    label_array = np.array(labels)
    # delete row 11 and 22 due to flawed measurements data
    dp_twenty_two_del = np.delete(data_point_array, 22, 0)
    dp_eleven_del = np.delete(dp_twenty_two_del, 11, 0)
    l_twenty_two_del = np.delete(label_array, 22, 0)
    l_eleven_del = np.delete(l_twenty_two_del, 11, 0)
    # final dataset
    # convert sample array and label array to type float
    data_point_array_f = dp_eleven_del.astype(np.float64)
    label_array_f = l_eleven_del.astype(np.float64)
    # create dictionary
    complete_dict = {
        'name': 'complete_dict',
        'data': data_point_array_f[:, :-1],
        'target': label_array_f,
        'target_names': ['baseline', 'cd', 'emotion_one', 'emotion_two', 'stress_one',
                         'stress_two'],
        'feature_names': complete_feat_list[:-1],
        'description': complete_description,
    }

    # ------------------- Complete no cd------------------- #
    complete_no_cd_description = "reduced dataset containing all datapoints except for cds, with a single label " \
                                 "for each state [baseline = 0, emotion_one = 1, emotion_two = 2, stress_one = 3, " \
                                 "stress_two = 4], Cave: remove last feature!"
    # convert label list to array
    label_array = np.array(labels)
    # delete row 11 and 22 due to flawed measurements data
    dp_twenty_two_del = np.delete(data_point_array, 22, 0)
    dp_eleven_del = np.delete(dp_twenty_two_del, 11, 0)
    l_twenty_two_del = np.delete(label_array, 22, 0)
    l_eleven_del = np.delete(l_twenty_two_del, 11, 0)
    # final dataset
    # convert sample array and label array to type float
    data_point_array_f = dp_eleven_del.astype(np.float64)
    label_array_f = l_eleven_del.astype(np.float64)

    # find cd samples and mark them for removal
    label_no_cd = [-1 if lab == 1 else lab for lab in label_array_f]
    label_no_cd_2 = [lab if lab == 0 or lab == -1 else lab-1 for lab in label_no_cd]
    # convert placeholder list for new, reduced label list
    label_no_cd_r = list([])
    # create placeholder array for samples
    no_cd_array = np.empty((0, len(complete_feat_list)))
    for row_index in range(len(label_no_cd_2)):
        if label_no_cd_2[row_index] != -1:
            new_row = np.array(data_points[row_index])
            no_cd_array = np.vstack((no_cd_array, new_row))
            label_no_cd_r.append(label_no_cd_2[row_index])

    # final dataset
    no_cd_array_f = no_cd_array.astype(np.float64)
    label_no_cd_array_f = np.array(label_no_cd_r).astype(np.float64)
    # create dictionary
    complete_no_cd_dict = {
        'name': 'complete_no_cd_dict',
        'data': no_cd_array_f[:, :-1],
        'target': label_no_cd_array_f,
        'target_names': ['baseline', 'emotion_one', 'emotion_two', 'stress_one',
                         'stress_two'],
        'feature_names': complete_feat_list[:-1],
        'description': complete_no_cd_description,
    }
    # ------------------- Rest vs All ------------------- #
    rest_v_all_description = "complete dataset, with only two labels (baseline vs rest) [baseline = 1, cd (1-3) =0, " \
                             "emotion_one = 0, emotion_two = 0, stress_one = 0, stress_two = 0], " \
                             "Cave: remove last feature!"
    # find all resting samples and transform label list to match the binary values from the description
    label_rest_v_all = [1 if lab == 0 else 0 for lab in labels]
    # convert new label list to array
    label_rest_v_all_array = np.array(label_rest_v_all)
    # delete row 11 and 22 due to flawed measurements data
    lb_twenty_two_del = np.delete(label_rest_v_all_array, 22, 0)
    lb_eleven_del = np.delete(lb_twenty_two_del, 11, 0)
    # final dataset
    # convert new sample array and new label array to type float
    rest_v_all_array_f = data_point_array_f
    label_rest_v_all_array_f = lb_eleven_del.astype(np.float64)
    # create dict
    rest_v_all_dict = {
        'name': 'rest_v_all_dict',
        'data': rest_v_all_array_f[:, :-1],
        'target': label_rest_v_all_array_f,
        'target_names': ["no_rest", "rest"],
        'feature_names': complete_feat_list[:-1],
        'description': rest_v_all_description,
    }

    # ------------------- Stress 1 vs Stress 2 ------------------- #
    stress_v_stress_description = "reduced dataset (only stress samples), with only two labels " \
                                  "(stress one vs stress two) [stress_one = 0, stress_two = 1], " \
                                  "Cave: remove last feature!"
    # find stress segments, individually by label
    label_stress_v_stress = [lab if lab == 4 or lab == 5 else -1 for lab in labels]
    # initiate placeholder for the new, reduced label list
    label_stress_v_stress_r = list([])
    # initiate placeholder for the new, reduced sample array
    stress_v_stress_array = np.empty((0, len(complete_feat_list)))
    # fill new sample array and label list with stress samples and labels, respectively
    for row_index in range(len(label_stress_v_stress)):
        if label_stress_v_stress[row_index] != -1:
            new_row = np.array(data_points[row_index])
            stress_v_stress_array = np.vstack((stress_v_stress_array, new_row))
            label_stress_v_stress_r.append(label_stress_v_stress[row_index])

    # final dataset
    # convert type of sample array to float
    stress_v_stress_array_f = stress_v_stress_array.astype(np.float64)
    # transform new, reduced label list to fit the binary description values
    label_stress_v_stress_rb = [0 if lab == 4 else 1 for lab in label_stress_v_stress_r]
    # convert label list to array of type float
    label_stress_v_stress_array_f = np.array(label_stress_v_stress_rb).astype(np.float64)
    # create dict
    stress_v_stress_dict = {
        'name': 'stress_v_stress_dict',
        'data': stress_v_stress_array_f[:, :-1],
        'target': label_stress_v_stress_array_f,
        'target_names': ["stress_one", "stress_two"],
        'feature_names': complete_feat_list[:-1],
        'description': stress_v_stress_description,
    }

    # ------------------- Stress vs All ------------------- #
    stress_v_all_description = "complete dataset, with only two labels (stress vs no stress), " \
                               "[stress = 1, no stress = 0], Cave: remove last feature!"
    # find all emotion samples by label
    label_stress_v_all = [1 if lab == 4 or lab == 5 else 0 for lab in labels]
    # convert new list to array
    label_stress_v_all_array = np.array(label_stress_v_all)
    # delete row 11 and 22 due to flawed measurements data
    eb_twenty_two_del = np.delete(label_stress_v_all_array, 22, 0)
    eb_eleven_del = np.delete(eb_twenty_two_del, 11, 0)
    # final dataset
    stress_v_all_array_f = data_point_array_f
    label_stress_v_all_array_f = eb_eleven_del.astype(np.float64)
    # create dict
    stress_v_all_dict = {
        'name': 'stress_v_all_dict',
        'data': stress_v_all_array_f[:, :-1],
        'target': label_stress_v_all_array_f,
        'target_names': ["no_stress", "stress"],
        'feature_names': complete_feat_list[:-1],
        'description': stress_v_all_description,
    }

    # ------------------- Stress vs Rest ------------------- #
    stress_v_rest_description = "reduced dataset, with two labels (stress vs rest), [stress = 1, rest = 0], " \
                                "Cave: remove last feature!"
    # find stress and rest samples by label and transform them to match the binary representation from the description
    label_stress_v_rest = [1 if lab == 4 or lab == 5 else 0 if lab == 0 else -1 for lab in labels]
    # convert placeholder list for new, reduced label list
    label_stress_v_rest_r = list([])
    # create placeholder array for samples
    stress_v_rest_array = np.empty((0, len(complete_feat_list)))
    for row_index in range(len(label_stress_v_rest)):
        if label_stress_v_rest[row_index] != -1:
            new_row = np.array(data_points[row_index])
            stress_v_rest_array = np.vstack((stress_v_rest_array, new_row))
            label_stress_v_rest_r.append(label_stress_v_rest[row_index])

    # final dataset
    stress_v_rest_array_f = stress_v_rest_array.astype(np.float64)
    label_stress_v_rest_array_f = np.array(label_stress_v_rest_r).astype(np.float64)
    # create dict
    stress_v_rest_dict = {
        'name': 'stress_v_rest_dict',
        'data': stress_v_rest_array_f[:, :-1],
        'target': label_stress_v_rest_array_f,
        'target_names': ["rest", "stress"],
        'feature_names': complete_feat_list[:-1],
        'description': stress_v_rest_description,
    }

    # ------------------- Emotion 1 vs Emotion 2 ------------------- #
    emotion_v_emotion_description = "reduced dataset (only emotion samples), with only two labels " \
                                    "(emotion one vs emotion two), [emotion_one = 0, emotion_two = 1], " \
                                    "Cave: remove last feature!"
    # find emotion samples, individually by label
    label_emotion_v_emotion = [lab if lab == 2 or lab == 3 else -1 for lab in labels]
    # initiate placeholder for the new, reduced label list
    label_emotion_v_emotion_r = list([])
    # initiate placeholder for the new, reduced sample array
    emotion_v_emotion_array = np.empty((0, len(complete_feat_list)))
    # fill new sample array and label list with stress samples and labels, respectively
    for row_index in range(len(label_emotion_v_emotion)):
        if label_emotion_v_emotion[row_index] != -1:
            new_row = np.array(data_points[row_index])
            emotion_v_emotion_array = np.vstack((emotion_v_emotion_array, new_row))
            label_emotion_v_emotion_r.append(label_emotion_v_emotion[row_index])

    # final dataset
    # convert type of sample array to float
    emotion_v_emotion_array_f = emotion_v_emotion_array.astype(np.float64)
    # transform new, reduced label list to fit the binary description values
    label_emotion_v_emotion_rb = [0 if lab == 2 else 1 for lab in label_emotion_v_emotion_r]
    # convert label list to array of type float
    label_emotion_v_emotion_array_f = np.array(label_emotion_v_emotion_rb).astype(np.float64)
    # create dict
    emotion_v_emotion_dict = {
        'name': 'emotion_v_emotion_dict',
        'data': emotion_v_emotion_array_f[:, :-1],
        'target': label_emotion_v_emotion_array_f,
        'target_names': ["emotion_one", "emotion_two"],
        'feature_names': complete_feat_list[:-1],
        'description': emotion_v_emotion_description,
    }

    # ------------------- Emotion vs All ------------------- #
    emotion_v_all_description = "complete dataset, with only two labels (emotion vs no emotion), " \
                                "[emotion = 1, no emotion = 0], Cave: remove last feature!"
    # find all emotion samples by label
    label_emotion_v_all = [1 if lab == 2 or lab == 3 else 0 for lab in labels]
    # convert new list to array
    label_emotion_v_all_array = np.array(label_emotion_v_all)
    # delete row 11 and 22 due to flawed measurements data
    eb_twenty_two_del = np.delete(label_emotion_v_all_array, 22, 0)
    eb_eleven_del = np.delete(eb_twenty_two_del, 11, 0)
    # final dataset
    emotion_v_all_array_f = data_point_array_f
    label_emotion_v_all_array_f = eb_eleven_del.astype(np.float64)
    # create dict
    emotion_v_all_dict = {
        'name': 'emotion_v_all_dict',
        'data': emotion_v_all_array_f[:, :-1],
        'target': label_emotion_v_all_array_f,
        'target_names': ["no emotion", "emotion"],
        'feature_names': complete_feat_list[:-1],
        'description': emotion_v_all_description,
    }

    # ------------------- Emotion vs Rest ------------------- #
    emotion_v_rest_description = "reduced dataset, with two labels (emotion vs rest), [emotion = 1, rest = 0], " \
                                 "Cave: remove last feature!"
    # find emotion and rest samples by label and transform them to match the binary representation from the description
    label_emotion_v_rest = [1 if lab == 2 or lab == 3 else 0 if lab == 0 else -1 for lab in labels]
    # convert placeholder list for new, reduced label list
    label_emotion_v_rest_r = list([])
    # create placeholder array for samples
    emotion_v_rest_array = np.empty((0, len(complete_feat_list)))
    for row_index in range(len(label_emotion_v_rest)):
        if label_emotion_v_rest[row_index] != -1:
            new_row = np.array(data_points[row_index])
            emotion_v_rest_array = np.vstack((emotion_v_rest_array, new_row))
            label_emotion_v_rest_r.append(label_emotion_v_rest[row_index])

    # final dataset
    emotion_v_rest_array_f = emotion_v_rest_array.astype(np.float64)
    label_emotion_v_rest_array_f = np.array(label_emotion_v_rest_r).astype(np.float64)
    # create dict
    emotion_v_rest_dict = {
        'name': 'emotion_v_rest_dict',
        'data': emotion_v_rest_array_f[:, :-1],
        'target': label_emotion_v_rest_array_f,
        'target_names': ["rest", "emotion"],
        'feature_names': complete_feat_list[:-1],
        'description': emotion_v_rest_description,
    }

    # create a dictionary holding al datasets
    datasets_dict = [complete_dict, complete_no_cd_dict, rest_v_all_dict, stress_v_all_dict, stress_v_rest_dict,
                     stress_v_stress_dict, emotion_v_all_dict, emotion_v_rest_dict, emotion_v_emotion_dict]

    return datasets_dict


if __name__ == '__main__':
    main()
