import math
import random
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import scipy


def main():
    # for test purposes, later: output of the peak_detecting_algorithm
    peaks = np.array([4.0, 20.0, 72.0, 131.0, 164.0, 227.0, 282.0, 316.0, 364.0, 413.0, 459.0, 505.0, 554.0, 610.0, 666.0,
                      720.0, 776.0, 880.0, 890.0])

    ibi_data = get_inter_beat_intervals(peak_data=peaks)

    ectopic_beat_indices, ectopic_beats, normal_beat_indices, normal_beats = mark_ectopic_beats(ibi_data)

    print()
    for ebi in range(len(ectopic_beat_indices[0])):
        print('Ectopic beat found at pos ', ectopic_beat_indices[0][ebi], ' with the value of ', ectopic_beats[ebi])
    index_sequences, value_sequences = mark_ectopic_beat_sequences(ectopic_beat_indices=ectopic_beat_indices,
                                                                   ectopic_beat_values=ectopic_beats)
    print()
    n_beats_to_replace, n_beats_to_insert, interpolation_mode, adapted_ibi_data, indices_to_replace = \
        calculate_number_of_substitution_intervals(ibi_data=ibi_data, ectopic_beat_indices=ectopic_beat_indices,
                                                   eb_index_sequences=index_sequences,
                                                   eb_value_sequences=value_sequences,
                                                   normal_beat_values=normal_beats)

    print()
    norm_beat_percentage = interval_dismissal_decider(n_beats_to_replace, normal_beat_indices)
    print()
    interpolated_ibi_data = linear_interpolation(new_ibi_data=adapted_ibi_data, interpolation_mode=interpolation_mode,
                                                 number_of_beats_to_insert=n_beats_to_insert,
                                                 indices_to_replace=indices_to_replace)


def get_inter_beat_intervals(peak_data):
    """A function that generates a set of inter beat intervals from a peak data set.
    Following the convention suggested by Task Force (1996). The discrete event series (DES) is the plot of
    R_(i)-R_(i-1) at the time R_(i) occurred."""

    inter_beat_intervals = np.zeros(len(peak_data)-1)

    for p in range(len(peak_data)):
        if p > 0:
            ibi = peak_data[p] - peak_data[p-1]
            np.put(inter_beat_intervals, [p-1], ibi)

    return inter_beat_intervals                 # returns ibi in samples


def mark_ectopic_beats(ibi_data):
    """A function that finds all ectopic or artifact beats as classified by a given method.
    Marks physiologically impossible inter beat intervals as ectopic or artifact beats."""
    # a method that searches for ectopic beats and gives back an array,
    #       holding the indices of all ectopic beats (ectopic_beat_indices)

    # for test purposes an ibi outside the physiologic bounds will be classified as an ectopic beat, or artifact beat
    # HR 50-200 (might adapt to baseline measurement)
    # HR 45 = ibi 1.33 = 85 samples
    # HR 200 = ibi 0.3 =  19 samples
    bins = pd.cut(ibi_data, [0, 19, 85, np.inf], labels=['out_low', 'in_range', 'out_high'])
    ectopic_beat_indices = np.where(bins.T != 'in_range')         # stores all indices inside a tuple
    ectopic_beat_values = ibi_data[bins.T != 'in_range']          # stores all values in an array

    normal_beat_indices = np.where(bins.T == 'in_range')
    normal_beat_values = ibi_data[bins.T == 'in_range']
    # Note: this segment works

    # as suggested in Choi and Shin (2018) according to Kamath
    # an ectopic beat occurred when 0.675*ibi_(n-1) < ibi_(n) < 1.245*ibi_(n-1)
    # ectopic_beat_indices = list([])
    # ectopic_beat_values = list([])
    #
    # for i in range(len(ibi_data)):
    #     print(ibi_data[i])
    #     if i > 0:
    #         if ibi_data[i] > (0.675*ibi_data[i-1]):
    #             ectopic_beat_indices.append(i)
    #             ectopic_beat_values.append(ibi_data[i])
    #         elif ibi_data[i] < (1.245*ibi_data[i-1]):
    #             ectopic_beat_indices.append(i)
    #             ectopic_beat_values.append(ibi_data[i])
    # Note: code segment works but method flagged every ibi as eb

    return ectopic_beat_indices, ectopic_beat_values, normal_beat_indices, normal_beat_values


def mark_ectopic_beat_sequences(ectopic_beat_indices, ectopic_beat_values):
    """A function that identifies sequences or groups of irregular beats.
    Output: Two lists; 1. index_sequences, holding the indices of all the beats and sequences 2. value_sequences,
    holding the values of all the beats and sequences at the indices of index_sequences."""
    # mark ectopic beats as part of a sequence, therefore later the correct calculation is chosen
    index_sequences = list([])
    value_sequences = list([])
    i_sequence = list([])
    v_sequence = list([])
    loop_len = len(ectopic_beat_indices[0])-1

    ebi = 0
    while True:

        if ebi < loop_len:
            if (ectopic_beat_indices[0][ebi+1] - ectopic_beat_indices[0][ebi]) == 1:
                # ebi and ebi +1 are a sequence
                if i_sequence.count(ectopic_beat_indices[0][ebi].astype(int)) == 0:     # check if index was already added
                    i_sequence.append(ectopic_beat_indices[0][ebi].astype(int))         # if not then add index
                    v_sequence.append(ectopic_beat_values[ebi].astype(int))
                    is_sequence = True
            else:
                # ebi was a single eb or a sequence has ended
                is_sequence = False

            if is_sequence:
                i_sequence.append(ectopic_beat_indices[0][ebi+1].astype(int))
                v_sequence.append(ectopic_beat_values[ebi + 1].astype(int))
            else:
                if i_sequence.count(ectopic_beat_indices[0][ebi].astype(int)) == 0:
                    i_sequence.append(ectopic_beat_indices[0][ebi].astype(int))
                    v_sequence.append(ectopic_beat_values[ebi].astype(int))
                index_sequences.append(i_sequence)
                value_sequences.append(v_sequence)
                i_sequence = list([])
                v_sequence = list([])

        else:
            if i_sequence.count(ectopic_beat_indices[0][ebi].astype(int)) == 0:
                i_sequence.append(ectopic_beat_indices[0][ebi].astype(int))
                v_sequence.append(ectopic_beat_values[ebi].astype(int))
            # print(a_sequence)
            index_sequences.append(i_sequence)
            value_sequences.append(v_sequence)
            print()
            # print('Control: ', index_sequences)
            for seq in range(len(index_sequences)):
                if len(index_sequences[seq]) > 1:
                    print('A sequence of ectopic beats has been found at the indices ', index_sequences[seq],
                          'with values ', value_sequences[seq])

            break

        ebi += 1

    return index_sequences, value_sequences


def calculate_number_of_substitution_intervals(ibi_data, ectopic_beat_indices,
                                               eb_index_sequences, eb_value_sequences, normal_beat_values):
    """ A function that calculates the number of beats that have to be inserted to interpolate the ectopic beat and
    artifact intervals. The function uses the equation provided by Lippman (1994). The number of inserted intervals B
    is calculated by the equation: sum_[i->i+N](RR_(i)) / ((RR_(i-1)+ RR_(i+N+1) /2), with N = number_of_beats_to_replace
    N encompasses the inter beat interval before ectopic beat (R_(i)) and the follow up beat (R_(i+1)), adapted for
    ectopic sequences or artifact sequences this means all N beats in the sequence plus the follow up beat (R_(i+N+1))
    Further it marks ectopic sequences with a duration greater than 3 seconds as artifacts.
    Output: Beats to replace, Beats to insert and suggested Interpolation mode, for every ectopic beat or sequence."""

    # find out if single ectopic beat or a sequence of ectopic beats occurred
    # therefore we check the distance of the indices in ectopic_beat_indices

    # check if there were any ectopic beats in ibi_data
    if len(ectopic_beat_indices[0]) == 0:
        print('There were no ectopic beats found.')
    else:
        print('Ectopic beats found. Starting interpolation...')

        # holds the number of beats that have to be replaced for every ectopic beat or every sequence
        number_of_beats_to_replace = list([])
        # holds number of beats that will be inserted, value >= 0.5 will be rounded to the next higher integer
        number_of_beats_to_insert = list([])
        # will holt the indices of all beats to replace
        indices_to_replace = list([])
        # holds the interpolation method specifier for each ectopic beat or sequence
        interpolation_mode = list([])
        # temporary data set, adapted from the original ibi set to cater the needs of the interpolation algorithm
        new_ibi_data = ibi_data
        # check if there were any ectopic sequences
        print('Checking for ectopic beat sequences...')
        if len(eb_value_sequences) > 0:                             # check if the sequence list is holding any elements
            index_correction = 0

            for s in range(len(eb_value_sequences)):                # if it does work through the list
                number_of_beats_to_replace.append([])               # for every run generate an additional list space
                number_of_beats_to_insert.append([])
                indices_to_replace.append([])
                interpolation_mode.append([])
                # if len(eb_index_sequences[s]) > 1:
                #     print('Sequence found: ', eb_index_sequences[s])    # print sequences for monitoring

                # ectopic beats,as well as the follow up beat will be replaced
                # get start and target index for calculation
                start_index = eb_index_sequences[s][0] + index_correction                   # the initial ectopic beat
                target_index = start_index + len(eb_value_sequences[s])                     # first beat after the ectopic sequence
                # check if there is a value after the sequence

                if (new_ibi_data.size - target_index) == 0:
                    # if there is no value after the sequence, that can be used, we extend the original ibi array by
                    # two random normal beat picked from the measurement
                    # choose random element
                    rnd = random.sample(range(0, len(normal_beat_values)-1), 2)

                    # grab random value from normal beat collection
                    extension_value = normal_beat_values[rnd[0]]
                    extension_value_2 = normal_beat_values[rnd[1]]
                    # extend ibi data set
                    new_ibi_data = np.append(new_ibi_data, [extension_value])
                    new_ibi_data = np.append(new_ibi_data, [extension_value_2])
                    # beats_to_replace = eb_value_sequences[s]
                    # beats_to_replace.append(ibi_data[target_index])
                elif (new_ibi_data.size - target_index) == 1:
                    # if there is only one value after the sequence, that can be used, we extend the original ibi array
                    # by a random normal beat picked from the measurement
                    # choose random element
                    rnd = random.randint(0, len(normal_beat_values) - 1)
                    # grab random value from normal beat collection
                    extension_value = normal_beat_values[rnd]
                    # extend ibi data set
                    new_ibi_data = np.append(ibi_data, [extension_value])

                elif start_index == 0:
                    # if there is no value before the sequence, e.g. the sequence contains the first few data points
                    # in the ibi data set, we have to account for that by extending the set with a random normal beat
                    # choose random element
                    rnd = random.randint(0, len(normal_beat_values) - 1)

                    # grab random value from normal beat collection
                    extension_value = normal_beat_values[rnd]
                    # extend ibi data set
                    new_ibi_data = np.append([extension_value], new_ibi_data)
                    # # account for shift in the data
                    index_correction += 1
                    start_index += index_correction
                    target_index += index_correction
                    # calculation with new ibi data set and target index
                beats_to_replace = eb_value_sequences[s]
                beats_to_replace.append(new_ibi_data[target_index])
                # adapt indices
                eb_ind_seq_adapted = [x+index_correction for x in eb_index_sequences[s]]
                eb_ind_seq_adapted.append(target_index)
                indices_to_replace[s].append(eb_ind_seq_adapted)

                number_of_beats_to_replace[s].append(len(beats_to_replace))
                # else:
                #     # this is the case when its a single ectopic beat
                #     beats_to_replace = eb_value_sequences[s]
                #     beats_to_replace.append(ibi_data[target_index])
                # according to lippman 1994 the number of inserted intervals B is calculated by
                # sum[i->i+N](RR_(i)) / ((RR_(i-1)+ RR_(i+N+1) /2), with N = number_of_beats_to_replace
                # calculate the total duration of the interval that needs to be replaced
                sum_of_btr = sum(beats_to_replace)
                # we decide the way of interpolation according to the length of the interval
                # Fs is the sampling frequency
                fs = 64

                if sum_of_btr > 3 * fs:
                    # according to kamath, artifact sequences over 3 sec should be deleted from the data
                    interpolation_mode[s].append('delete')
                else:
                    interpolation_mode[s].append('interpolate')

                beats_to_insert = round(sum_of_btr / ((new_ibi_data[start_index-1] + new_ibi_data[target_index + 1]) / 2))
                number_of_beats_to_insert[s].append(beats_to_insert)

                print('Replace: ', number_of_beats_to_replace[s], 'Insert: ', number_of_beats_to_insert[s], 'at ', indices_to_replace[s])
        else:
            print('No sequences found. Processing single ectopic beats...')

            # cover same eventualities as for sequences
            # eb at the start of the ibi data set, extend by one randomly picked value from normal beats

            # eb at the end of the ibi data set, extend by

    return number_of_beats_to_replace, number_of_beats_to_insert, interpolation_mode, new_ibi_data, indices_to_replace


def interval_dismissal_decider(number_of_beats_to_replace, normal_beat_indices):
    """A function that evaluates the level of noise in the data set, according to percentage of beats that were marked
    as irregular in comparison to the normal beats in the set. It is suggested that a set with a percentage of normal
    beats below 80% should lead to the dismissal of the interval."""
    normal_beats = len(normal_beat_indices[0])
    irregular_beats = 0
    for e in number_of_beats_to_replace:
        irregular_beats = irregular_beats + sum(e)
    normal_beat_percentage = 100 - (irregular_beats / normal_beats) * 100
    return normal_beat_percentage


def linear_interpolation(new_ibi_data, interpolation_mode, number_of_beats_to_insert, indices_to_replace):
    print(len(indices_to_replace))

    for n in range(len(indices_to_replace)):
        if interpolation_mode[n][0] == 'interpolate':
            # print('Number of beats to insert: ', n)

            start_index = 1
            target_index = int(number_of_beats_to_insert[n][0])
            x_to_interpolation = np.linspace(start_index, target_index, endpoint=True, num=target_index)
            x = [start_index-1, target_index+1]

            grab_start_pos = indices_to_replace[n][0][0]-1
            grab_end_pos = indices_to_replace[n][0][-1]+1
            y = [new_ibi_data[grab_start_pos], new_ibi_data[grab_end_pos]]
            interpolated_beats = np.interp(x_to_interpolation, x, y)

            plt.figure(dpi=400)
            plt.plot(x, y, 'o')
            plt.plot(x_to_interpolation, interpolated_beats, '-x')
            plt.show()

            # remove the irregular beats from the ibi data set
            if grab_start_pos == 0:
                rem_ibi_data_pre = np.array([new_ibi_data[grab_start_pos]])
            else:
                rem_ibi_data_pre = new_ibi_data[0:grab_start_pos]
            if grab_end_pos == len(new_ibi_data):
                rem_ibi_data_post = new_ibi_data[grab_end_pos]
            else:
                rem_ibi_data_post = new_ibi_data[grab_end_pos:]

            corrected_ibi_data = np.concatenate([rem_ibi_data_pre, interpolated_beats, rem_ibi_data_post], axis=0)
            # generate enough space for interpolated values and the place them at the index of the ectopic beat
            # inside the ibi data set interpolated_data = ibi_set[:, ind-1] , interpolated values ,
            # ibi_set[ind+len(interpolated values)+1,:]
        elif interpolation_mode[n][0] == 'delete':
            grab_start_pos = indices_to_replace[n][0][0] - 1
            grab_end_pos = indices_to_replace[n][0][-1] + 1

            if grab_start_pos == 0:
                rem_ibi_data_pre = np.array([new_ibi_data[grab_start_pos]])
            else:
                rem_ibi_data_pre = new_ibi_data[0:grab_start_pos]
            if grab_end_pos == len(new_ibi_data):
                rem_ibi_data_post = new_ibi_data[grab_end_pos]
            else:
                rem_ibi_data_post = new_ibi_data[grab_end_pos:]
            # rem_ibi_data_pre = new_ibi_data[:, indices_to_replace[n][0]-1]
            # rem_ibi_data_post = new_ibi_data[indices_to_replace[n][-1]+1, :]
            corrected_ibi_data = np.concatenate([rem_ibi_data_pre, rem_ibi_data_post], axis=0)
        else:
            print('No indicator for interpolation mode found.')

    return corrected_ibi_data


def artifact_interpolation_bvp(peak_locations):
    ibi_data = get_inter_beat_intervals(peak_data=peak_locations)

    ectopic_beat_indices, ectopic_beats, normal_beat_indices, normal_beats = mark_ectopic_beats(ibi_data)

    print()
    for ebi in range(len(ectopic_beat_indices[0])):
        print('Ectopic beat found at pos ', ectopic_beat_indices[0][ebi], ' with the value of ', ectopic_beats[ebi])
    index_sequences, value_sequences = mark_ectopic_beat_sequences(ectopic_beat_indices=ectopic_beat_indices,
                                                                   ectopic_beat_values=ectopic_beats)
    print()
    n_beats_to_replace, n_beats_to_insert, interpolation_mode, adapted_ibi_data, indices_to_replace = \
        calculate_number_of_substitution_intervals(ibi_data=ibi_data, ectopic_beat_indices=ectopic_beat_indices,
                                                   eb_index_sequences=index_sequences,
                                                   eb_value_sequences=value_sequences,
                                                   normal_beat_values=normal_beats)

    print()
    norm_beat_percentage = interval_dismissal_decider(n_beats_to_replace, normal_beat_indices)
    print()
    interpolated_ibi_data = linear_interpolation(new_ibi_data=adapted_ibi_data, interpolation_mode=interpolation_mode,
                                                 number_of_beats_to_insert=n_beats_to_insert,
                                                 indices_to_replace=indices_to_replace)

    return interpolated_ibi_data


if __name__ == '__main__':
    main()

