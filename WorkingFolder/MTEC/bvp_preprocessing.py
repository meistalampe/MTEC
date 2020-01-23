#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script provides all methods necessary to prepare the bvp data for feature extraction. Including all necessary
   steps to extract inter-beat-intervals (ibi) from the raw bvp data as well as several methods to clear the data from
   any abnormal and ectopic beats."""

from scipy.signal import butter, filtfilt, tf2zpk
from typing import Tuple
from typing import List
import math
import random
import statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Static name for methods params
MALIK_RULE = "malik"
KARLSSON_RULE = "karlsson"
KAMATH_RULE = "kamath"
ACAR_RULE = "acar"
CUSTOM_RULE = "custom"


# define block class
class Block:
    _instances = set()

    def __init__(self, number, block_start, block_end):
        self.number = number
        self.block_start = block_start
        self.block_end = block_end
        self.width = block_end - block_start

    @classmethod
    def getinstances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead


__all__ = ["bvp_peak_detection", "bandpass_butterworth", "zero_phase_filtering", "clipping", "squaring",
           "generate_moving_averages", "thresholding", "find_valid_peaks", "get_inter_beat_intervals", "samples_to_ms",
           "remove_outliers", "find_sequences", "calculate_substitution_intervals", "remove_artifacts",
           "prepare_interpolation", "interpolate_nan_values", "is_outlier", "remove_ectopic_beats_old",
           "remove_ectopic_beats", "get_nn_intervals_old", "get_nn_intervals", "nan_check"]


# ----------------- Bvp peak detection algorithm ----------------- #


def bvp_peak_detection(bvp_raw_data: np.ndarray, sampling_frequency: int = 64, verbose: bool = False):
    """
    Function that handles peak detection in bvp data.

    Parameters
    ----------
    bvp_raw_data: list
        list containing bvp values from recording file.
    sampling_frequency: int
        sampling frequency that was used for the bvp recording. Default set to 64 Hz as it is the sampling rate of the
        empatica E4 device.
    verbose: bool
        print information about function progress.

    Returns
    ----------
    peak_amplitude:

    peak_locations:

    References
    -----------
    ..[1] M. Elgendi, I. Norton, M. Brearley, D. Abbott, D. Schuurmans. Systolic peak Detection in Acceleration
    Photoplethysmograms Measured from Emergency Responders in Tropical Conditions.
    """
    # step 1: Bandpass filtering
    filtered_signal = zero_phase_filtering(data=bvp_raw_data, f_min=0.5, f_max=8.0,
                                           sampling_frequency=sampling_frequency, filter_order=2)
    # step 2: Clipping
    clipped_signal = clipping(data=filtered_signal)
    # step 3: Squaring
    squared_clipped_signal = squaring(data=clipped_signal)
    # step 4: Moving averages
    MA_peak, MA_beat, samples_peak = generate_moving_averages(data=squared_clipped_signal,
                                                              sampling_frequency=sampling_frequency,
                                                              window_for_peak=0.111, window_for_beat=0.667)
    # step 5: Thresholds and Offset
    first_threshold, second_threshold = thresholding(data=squared_clipped_signal, moving_average_beat=MA_beat,
                                                     window_for_peak_in_samples=samples_peak)
    # step 6: generate blocks of interest
    blocks_of_interest = np.zeros(len(MA_peak))

    for n in range(len(MA_peak)):
        if MA_peak[n] >= first_threshold[n]:
            np.put(blocks_of_interest, [n], 2500.0)
        else:
            np.put(blocks_of_interest, [n], 0.0)

    # step 7: find valid blocks
    peak_amplitudes, peak_locations = find_valid_peaks(block_array=blocks_of_interest, signal=squared_clipped_signal,
                                                       second_threshold=second_threshold)

    if verbose:
        # plotting
        time = list(range(0, len(filtered_signal)))
        timed = [x / 64 for x in time]
        x_axis = np.array(timed)
        peaked = [x / 64 for x in peak_locations]
        p_axis = np.array(peaked)
        plt.figure()
        # plt.plot(x_axis, filtered_signal, color='blue', linewidth=0.5, linestyle='-', label='S[n]')
        # plt.plot(x_axis, clipped_signal, color='blue', linewidth=0.5, linestyle='-', label='Z[n]')
        plt.plot(x_axis, squared_clipped_signal, color='blue', linewidth=0.5, linestyle='-', label='Z[n] **2')
        plt.plot(x_axis, MA_peak, color='red', linewidth=0.5, linestyle='-.', label='MA_peak')
        plt.plot(x_axis, first_threshold, color='black', linewidth=0.5, linestyle=':', label='MA_beat')
        # plt.legend(('input', 'MA peak', 'MA beat'))
        plt.plot(x_axis, blocks_of_interest, color='grey', linewidth=0.5, linestyle='--')
        plt.plot(p_axis, peak_amplitudes, 'vy', markersize=5.0)
        #plt.plot(peak_locations, peak_amplitudes, 'vy', markersize=5.0)
        plt.xlabel('time (seconds)')
        plt.legend()
        plt.show()

    return peak_amplitudes, peak_locations


def bandpass_butterworth(filter_order: int, cutoff_frequency_low: float, cutoff_frequency_high: float,
                         sampling_frequency: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Function that creates a Butterworth bandpass filter, with a frequency band ranging from cutoff_frequency_low to
    cutoff_frequency_high.

    Parameters
    ----------
    filter_order: int
        order of the filter. The default order which is used in this scenario is 2.
    cutoff_frequency_low: float
        lower bound of the frequency band. Frequencies lower than this bound will be filtered. The default frequency
        used in this scenario is 0.5.
    cutoff_frequency_high: float
        upper bound of the frequency band. Frequencies higher than this bound will be filtered. The default frequency
        used in this scenario is 8.0.
    sampling_frequency: int
        sampling frequency used in data acquisition.

    Returns
    ----------
    filter_polynomials: Tuple[np.ndarray, np.ndarray]
        tuple containing the numerator (b) and denominator (a) polynomials of the IIR filter

    References
    -----------
    No references needed.
    """

    nyquist_frequency = 0.5 * sampling_frequency
    low_cut = cutoff_frequency_low / nyquist_frequency
    high_cut = cutoff_frequency_high / nyquist_frequency
    b, a = butter(filter_order, [low_cut, high_cut], btype='band', output='ba')
    filter_polynomials = (b, a)
    return filter_polynomials


def zero_phase_filtering(data: np.ndarray, f_min: float, f_max: float, sampling_frequency: int, filter_order: int = 2,
                         verbose: bool = False) -> np.ndarray:
    """
    Filter function using a zero phase second order Butterworth filter, with bandpass f_min - f_max, is implemented
    to remove baseline wander and high frequencies.

    Parameters
    ----------
    data: np.ndarray
        one dimensional signal that will be filtered.
    f_min: float
        lower bound of the frequency band. Frequencies lower than this bound will be filtered. The default frequency
        used in this scenario is 0.5.
    f_max: float
        upper bound of the frequency band. Frequencies higher than this bound will be filtered. The default frequency
        used in this scenario is 8.0.
    sampling_frequency: int
        sampling frequency used in data acquisition.
    filter_order: int
        order of the filter. The default order which is used in this scenario is 2.
    verbose: bool
        print information about function progress.

    Returns
    ----------
    s_n_gust: ndarray
        the zero phase filtered signal with estimated impulse length according to Gustafsson's method

    References
    -----------
    No references needed.
    """
    # test if data is a numpy array
    if type(data) is not np.ndarray:
        signal = np.array(data)
    else:
        signal = data

    # create a bandpass butterworth filter
    filter_polynomials = bandpass_butterworth(filter_order=filter_order, cutoff_frequency_low=f_min,
                                              cutoff_frequency_high=f_max, sampling_frequency=sampling_frequency)

    # We use scypi.filtfilt using the Gustafsson's method (include paper)
    # The irlen argument can be used to improve the performance of Gustafsson’s method.
    # (url: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.filtfilt.html#r10879a509a76-1)
    # Estimate the impulse response length of the filter.
    z, p, k = tf2zpk(filter_polynomials[0], filter_polynomials[1])
    eps = 1e-9
    r = np.max(np.abs(p))
    approx_impulse_len = int(np.ceil(np.log(eps) / np.log(r)))
    # apply the zero phase bandpass filter with estimated impulse length according to Gustafsson's method
    s_n_gust = filtfilt(filter_polynomials[0], filter_polynomials[1], signal, method='gust', irlen=approx_impulse_len)

    if verbose:
        # plot the result
        time = list(range(0, len(s_n_gust)))
        timed = [x / 64 for x in time]
        x_axis = np.array(timed)
        plt.figure()
        # plt.plot(data, linewidth=1.0, label='x[n]')
        plt.plot(x_axis, s_n_gust, color='blue', linewidth=1.0, label='S[n]')
        plt.xlabel('time (seconds)')
        plt.legend()
        plt.show()

    return s_n_gust


def clipping(data, verbose: bool = False) -> np.ndarray:
    """
    Clipping the input signal by keeping the signal above 0. Function will produce the output signal z_n.

    Parameters
    ----------
    data: np.ndarray
        one dimensional signal that will be clipped.
    verbose: bool
        print information about function progress.

    Returns
    ----------
    z_n: ndarray
        clipped signal.

    References
    -----------
    No references needed.
    """
    # test if data is a numpy array
    if type(data) is not np.ndarray:
        s_n = np.array(data)
    else:
        s_n = data

    z_n = np.zeros(len(s_n))

    for e in range(len(s_n)):
        if s_n[e] >= 0:
            np.put(z_n, [e], s_n[e])
        else:
            np.put(z_n, [e], 0)

    if verbose:
        # plot the result
        time = list(range(0, len(s_n)))
        timed = [x / 64 for x in time]
        x_axis = np.array(timed)
        plt.figure()
        plt.plot(x_axis, s_n, linewidth=1.0, label='S[n]')
        plt.plot(x_axis, z_n, linewidth=1.0, label='Z[n]')
        plt.xlabel('time (seconds)')
        plt.legend()
        plt.show()
    return z_n


def squaring(data: np.ndarray, verbose: bool = False) -> np.ndarray:
    """
    Squaring the input signal to emphasize large differences resulting from systolic waves,
    while suppressing small differences arising from diastolic waves and noise. Function produces output y_n

    Parameters
    ----------
    data: np.ndarray
        one dimensional signal that will be squared.
    verbose: bool
        print information about function progress.

    Returns
    ----------
    y_n: ndarray
        squared signal.

    References
    -----------
    No references needed.
    """
    # test if data is a numpy array
    if type(data) is not np.ndarray:
        z_n = np.array(data)
    else:
        z_n = data

    y_n = np.square(z_n)

    if verbose:
        # plot the result
        plt.figure()
        plt.plot(z_n, linewidth=2.0, label='input')
        plt.plot(y_n, linewidth=2.0, label='squared')
        plt.show()

    return y_n


def generate_moving_averages(data: np.ndarray, sampling_frequency: int, window_for_peak: float, window_for_beat: float,
                             verbose: bool = False) -> Tuple[np.ndarray, np.ndarray, int]:
    """
    Function that generates the two moving averages and window values needed for thresholding in bvp peak detection.

    Parameters
    ----------
    data: np.ndarray
        one dimensional input signal.
    sampling_frequency: int
        sampling frequency used in acquisition of data parameter.
    window_for_peak: float
        sets window size for peak detection.
    window_for_beat: float
        sets window size for beat detection.
    verbose: bool
        print information about function progress.

    Returns
    ----------
    moving_average_peak: np.ndarray
        mov avg for peak detection.
    moving_average_beat: np.ndarray
        mov avg for beat detection.
    N_1: int
        first threshold, used for peak detection.

    References
    -----------
    No references needed.
    """
    if type(data) is not np.ndarray:
        y_n = np.array(data)
    else:
        y_n = data

    # the window is calculated from the desired time window (window_for_peak) and the sampling frequency
    # this is done to get the number of samples N that make up the window
    N_1 = math.floor(window_for_peak * sampling_frequency)
    # next we have to guarantee the window extends equally to both sides of the current sample
    # therefore we provide it is the size of the nearest uneven integer
    if N_1 % 2 == 0:
        N_1 = N_1 + 1

    # we calculate the moving avg by convolving with a kernel function
    # the kernel has the size of our window and his coefficients provide the same result as a mov avg
    # coeff = 1/N, N being the window size
    # modes are valid, full and same
    moving_average_peak = np.convolve(y_n, np.ones((N_1,)) / N_1, mode='same')
    # repeat for beat region of interest and beat mov avg
    N_2 = math.floor(window_for_beat * sampling_frequency)
    if N_2 % 2 == 0:
        N_2 = N_2 + 1

    moving_average_beat = np.convolve(y_n, np.ones((N_2,)) / N_2, mode='same')

    return moving_average_peak, moving_average_beat, N_1


def thresholding(data: np.ndarray, moving_average_beat: np.ndarray, window_for_peak_in_samples: int,
                 verbose: bool = False) -> Tuple[np.ndarray, int]:
    """
    Function that generates the two thresholding used in bvp peak detection.

    Parameters
    ----------
    data: np.ndarray
        one dimensional input signal.
    moving_average_beat: np.ndarray
        moving average for beat detection.
    window_for_peak_in_samples: int
        window size in samples used for peak detection.
    verbose: bool
        print information about function progress.

    Returns
    ----------
    first_dynamic_threshold: np.ndarray
        first threshold, used for peak detection.
    second_static_threshold: int
        second threshold, used for peak detection.

    References
    -----------
    No references needed.
    """
    beta = 0.02
    z_mean = statistics.mean(data)
    offset_alpha = beta * z_mean

    first_dynamic_threshold = moving_average_beat + offset_alpha
    second_static_threshold = window_for_peak_in_samples

    return first_dynamic_threshold, second_static_threshold


def find_valid_peaks(block_array: np.ndarray, signal: np.ndarray, second_threshold: int):
    """
        Function that evaluates valid blocks from the block array created in step 6 and located peaks in said blocks.

        Parameters
        ----------
        block_array: np.ndarray
            one dimensional array holding information on all block of interest that were found by thresholding.
        signal: np.ndarray
            one dimensional input signal..
        second_threshold: int
            threshold, used for peak detection.

        Returns
        ----------
        valid_peaks_amplitude, valid_peaks_location : np.ndarray, np.ndarray : dtype(float64)

        References
        -----------
        No references needed.
        """
    diff_mask = np.diff(block_array, n=1, )

    get_flanks = np.argwhere(diff_mask != 0)

    if diff_mask[get_flanks[0]] < diff_mask[get_flanks[1]]:
        start_index = 1
    else:
        start_index = 0

    get_flanks = get_flanks[start_index:]

    if len(get_flanks) % 2 != 0:
        get_flanks = get_flanks[:-1]
    else:
        pass

    valid_peaks_amplitude = np.zeros((len(get_flanks)))
    valid_peaks_location = np.zeros((len(get_flanks)))

    for f in range(0, len(get_flanks), 2):
        block_start = get_flanks[f][0]
        block_end = get_flanks[f + 1][0]
        block_width = block_end - block_start

        # signal_block = signal[block_start:block_end]
        signal_block = signal[get_flanks[f][0]:get_flanks[f + 1][0]]

        if block_width >= second_threshold:
            block_maximum = np.amax(signal_block)
            index_maximum = np.argwhere(signal_block == block_maximum)

            np.put(valid_peaks_amplitude, [f][0], block_maximum)
            np.put(valid_peaks_location, [f][0], index_maximum + block_start)

    valid_peaks_amplitude = valid_peaks_amplitude[valid_peaks_amplitude > 0]
    valid_peaks_location = valid_peaks_location[valid_peaks_location > 0]

    return valid_peaks_amplitude, valid_peaks_location


# ----------------- Calculate inter beat intervals ----------------- #


def get_inter_beat_intervals(peak_data: np.ndarray):
    """
    A function that generates a set of inter beat intervals from a peak data set.
    Following the convention suggested by Task Force (1996). The discrete event series (DES) is the plot of
    R_(i)-R_(i-1) at the time R_(i) occurred.

    Parameters
    ----------
    peak_data: ndarray
        a one dimensional array holding the location (in samples) of all valid peaks in the preprocessed signal.

    Returns
    ----------
    inter_beat_intervals: list
        a list holding the inter beat intervals calculated from the peak data set.

    References
    -----------
    ..[2] Task Force of The European Society of Cardiology and The North American Society of Pacing and
    Electrophysiology (Membership of the Task Force listed in the Appendix). Heart rate variability Standards of
    measurement, physiological interpretation, and clinical use
    """

    inter_beat_intervals = np.zeros(len(peak_data) - 1)

    for p in range(len(peak_data)):
        if p > 0:
            ibi = peak_data[p] - peak_data[p - 1]
            np.put(inter_beat_intervals, [p - 1], ibi)

    return list(inter_beat_intervals)  # returns ibi in samples


def samples_to_ms(inter_beat_intervals: List[float], sampling_frequency: int = 64) -> list:
    """
    A function that transforms units of samples into units of milliseconds.

    Parameters
    ---------
    inter_beat_intervals : list
        raw signal extracted. Inter beat intervals in units of samples.
    sampling_frequency: int
        sampling frequency of bvp signal.

    Returns
    ---------
    inter_beat_intervals_ms : list
        a list holding inter beat interval values in units of milliseconds.

    References
    ----------
    """
    # Conversion sample units to ms units
    # ibi (samples) --> number of samples / sampling frequency * 1000 = ibi (ms)
    # inter_beat_intervals_ms = [int((x / sampling_frequency) * 1000) for x in inter_beat_intervals]
    inter_beat_intervals_ms = [(x / sampling_frequency) * 1000 for x in inter_beat_intervals]
    return inter_beat_intervals_ms


# ----------------- Remove outliers and ectopic beats ----------------- #


def remove_outliers(inter_beat_intervals: List[float], verbose: bool = True, low_ibi: int = 314,
                    high_ibi: int = 1333):
    """
    Function that replaces inter beat interval outliers by nan. Outliers are values that are considered physiologically
    impossible and therefore must be artifacts.

    Parameters
    ---------
    inter_beat_intervals : list
        raw signal extracted. Inter beat intervals in ms.
    low_ibi : int
        lowest inter beat Interval to be considered plausible in ms.
    high_ibi : int
        highest inter beat Interval to be considered plausible ms.
    verbose : bool
        Print information about deleted outliers.

    Returns
    ---------
    inter_beat_intervals_zo : list
        a list of inter beat intervals without outliers.
    outliers_list: list
        a list of all outlier values that have been removed from inter_beat_intervals.
    outliers_indices: list
        a list of all the indices of the removed outliers in outliers_list.
    valid_list: list
        a list of all valid interval values.
    valid_indices: list
        a list of all valid interval indices.

    References
    ----------
    .. [1] O. Inbar, A. Oten, M. Scheinowitz, A. Rotstein, R. Dlin, R.Casaburi. Normal \
    cardiopulmonary responses during incremental exercise in 20-70-yr-old men.
    .. [2] W. C. Miller, J. P. Wallace, K. E. Eggert. Predicting max HR and the HR-VO2 relationship\
    for exercise prescription in obesity.
    .. [3] H. Tanaka, K. D. Monahan, D. R. Seals. Age-predictedmaximal heart rate revisited.
    .. [4] M. Gulati, L. J. Shaw, R. A. Thisted, H. R. Black, C. N. B.Merz, M. F. Arnsdorf. Heart \
    rate response to exercise stress testing in asymptomatic women.
    """
    # Conversion Inter beat Interval to Heart rate ==> ibi (ms) =  1000 / (bpm / 60)
    # ibi 2000 => bpm 30 / ibi 300 => bpm 200
    inter_beat_intervals_zo = [ibi if high_ibi >= ibi >= low_ibi else np.nan for ibi in inter_beat_intervals]

    outliers_list = []
    outliers_indices = []
    valid_list = []
    valid_indices = []
    count = 0
    for ibi in inter_beat_intervals:
        if high_ibi >= ibi >= low_ibi:
            valid_list.append(ibi)
            valid_indices.append(count)
        else:
            outliers_list.append(ibi)
            outliers_indices.append(count)
        count += 1
    nan_count = sum(np.isnan(inter_beat_intervals_zo))
    if verbose:
        if nan_count == 0:
            print("{} outlier(s) have been deleted.".format(nan_count))
        else:
            print("{} outlier(s) have been deleted.".format(nan_count))
            print("The outlier(s) value(s) are : {}".format(outliers_list))

    return inter_beat_intervals_zo, outliers_list, outliers_indices, valid_list, valid_indices


def find_sequences(outlier_indices: list, outlier_values: list, verbose: bool = False) -> Tuple[list, list]:
    """
    A function that identifies sequences or groups of irregular inter beat intervals.

    Parameters
    ---------
    outlier_indices: list
        a list containing the indices of all outliers detected in an inter beat interval data set.
    outlier_values: list
        a list containing the values of all outliers detected in an inter beat interval data set.
    verbose : bool
        Print information about deleted outliers.

    Returns
    ---------
    sequence_indices: list
        a list holding all detected intervals/sequences in the form of a separate list holding the corresponding
        interval indices.
    sequence_values: list
        a list holding all detected intervals/sequences in the form of a separate list holding the corresponding
        interval values.

    References
    ----------
    """
    # mark ectopic beats as part of a sequence, therefore later the correct calculation is chosen
    sequence_indices = list([])
    sequence_values = list([])
    i_sequence = list([])
    v_sequence = list([])
    loop_len = len(outlier_indices) - 1

    # if len(outlier_indices) == 0:
    #     sequence_indices = list([])
    #     sequence_values = list([])
    #     if verbose:
    #         print('There were no ectopic beats found.')
    #     return sequence_indices, sequence_values
    # else:
    #     if verbose:
    #         print('Ectopic beats found. Starting interpolation...')

    o = 0
    while True:

        if o < loop_len:
            if (outlier_indices[o + 1] - outlier_indices[o]) == 1:
                # o and o+1 are a sequence
                if i_sequence.count(int(outlier_indices[o])) == 0:  # check if index was already added
                    i_sequence.append(int(outlier_indices[o]))  # if not then add index
                    v_sequence.append(int(outlier_values[o]))
                    is_sequence = True
            else:
                # ebi was a single eb or a sequence has ended
                is_sequence = False

            if is_sequence:
                i_sequence.append(int(outlier_indices[o + 1]))
                v_sequence.append(int(outlier_values[o + 1]))
            else:
                if i_sequence.count(int(outlier_indices[o])) == 0:
                    i_sequence.append(int(outlier_indices[o]))
                    v_sequence.append(int(outlier_values[o]))
                sequence_indices.append(i_sequence)
                sequence_values.append(v_sequence)
                i_sequence = list([])
                v_sequence = list([])

        else:
            if i_sequence.count(int(outlier_indices[o])) == 0:
                i_sequence.append(int(outlier_indices[o]))
                v_sequence.append(int(outlier_values[o]))
            # print(a_sequence)
            sequence_indices.append(i_sequence)
            sequence_values.append(v_sequence)
            # print()
            # print('Control: ', index_sequences)
            if verbose:
                for seq in range(len(sequence_indices)):
                    if len(sequence_indices[seq]) > 1:
                        print('A sequence of outliers has been found. Outlier indices are {} with respective values {}.'
                              .format(sequence_indices[seq], sequence_values[seq]))
                    else:
                        print('An outlier has been found at position {} with the value {}'
                              .format(sequence_indices[seq], sequence_values[seq]))
            break

        o += 1
    return sequence_indices, sequence_values


def calculate_substitution_intervals(inter_beat_intervals: list, outlier_indices: list, sequence_indices: list,
                                     sequence_values: list, valid_intervals: list, ibi_max: float = 1333,
                                     ibi_min: float = 314, verbose: bool = False):
    """
    A function that calculates the number of beats that have to be inserted to interpolate the ectopic beat and
    artifact intervals. The function uses the equation provided by Lippman (1994). The number of inserted intervals B
    is calculated by the equation: sum_[i->i+N](RR_(i)) / ((RR_(i-1)+ RR_(i+N+1) /2), with N = number_of_beats_to_replace
    N encompasses the inter beat interval before ectopic beat (R_(i)) and the follow up beat (R_(i+1)), adapted for
    ectopic sequences or artifact sequences this means all N beats in the sequence plus the follow up beat (R_(i+N+1))
    Further it marks ectopic sequences with a duration greater than 3 seconds as artifacts.

    Parameters
    ---------
    inter_beat_intervals: list
        a list holding inter beat intervals.
    outlier_indices: list
        a list containing the indices of all outliers detected in an inter beat interval data set.
    sequence_indices: list
        a list holding indices of outliers, that were detected in inter_beat_intervals, in the form of lists of single
        outliers or sequences of outliers.
    sequence_values: list
        a list holding the corresponding values to sequence_indices, also in the form of lists grouped by sequences.
    valid_intervals: list
        a list of all valid inter beat intervals detected in inter_beat_intervals.
    ibi_max: float
        value to check if a ibi value can be used for calculation
    ibi_min: float
        vlaue to check if a ibi value can be used for calculation
    verbose : bool
        Print information about deleted outliers.

    Returns
    ---------
    number_of_beats_to_replace: List[list]
        stores the number of intervals that need to be replaced for each of the outlier sequences found in
        inter_beat_intervals.
    number_of_beats_to_insert: list[list]
        stores the number of beats that will be inserted for each outlier sequence.
    interpolation_mode: list[list]
        used to remove artifacts later.
    new_ibi_data: list
        augmented version of inter_beat_intervals, which may has been altered to fit the algorithm criteria.
    indices_to_replace: list[list]
        holds all indices of the beats that were marked for replacement.

    References
    ----------
    """
    # check if there were any ectopic beats in ibi_data
    if len(outlier_indices) == 0:
        number_of_beats_to_replace = []
        number_of_beats_to_insert = []
        interpolation_mode = []
        new_ibi_data = inter_beat_intervals
        indices_to_replace = []

        if verbose:
            print('There were no ectopic beats found.')

    else:
        if verbose:
            print('Ectopic beats found. Starting interpolation...')

        # holds the number of beats that have to be replaced for every ectopic beat or every sequence
        number_of_beats_to_replace = list([])
        # holds number of beats that will be inserted, value >= 0.5 will be rounded to the next higher integer
        number_of_beats_to_insert = list([])
        # will hold the indices of all beats to replace
        indices_to_replace = list([])
        # holds the interpolation method specifier for each ectopic beat or sequence
        interpolation_mode = list([])
        # temporary data set, adapted from the original ibi set to cater the needs of the interpolation algorithm
        new_ibi_data = inter_beat_intervals
        # check if there were any ectopic sequences
        if verbose:
            print('Checking for ectopic beat sequences...')
        # check if the sequence list is holding any elements
        if len(sequence_values) > 0:
            index_correction = 0
            # if it does work through the list
            for s in range(len(sequence_values)):
                # for every run generate an additional list space
                number_of_beats_to_replace.append([])
                number_of_beats_to_insert.append([])
                indices_to_replace.append([])
                interpolation_mode.append([])
                # if len(eb_index_sequences[s]) > 1:
                #     print('Sequence found: ', eb_index_sequences[s])    # print sequences for monitoring

                # ectopic beats,as well as the follow up beat will be replaced
                # get start and target index for calculation
                # the initial ectopic beat
                start_index = sequence_indices[s][0] + index_correction
                # first beat after the ectopic sequence
                target_index = start_index + len(sequence_values[s])
                # check if there is a value after the sequence

                if (len(new_ibi_data) - target_index) == 0:
                    # if there is no value after the sequence, that can be used, we extend the original ibi array by
                    # two random normal beat picked from the measurement
                    # choose random element
                    rnd = random.sample(range(0, len(valid_intervals) - 1), 2)

                    # grab random value from normal beat collection
                    extension_value = valid_intervals[rnd[0]]
                    extension_value_2 = valid_intervals[rnd[1]]
                    # extend ibi data set
                    new_ibi_data.append(extension_value)
                    new_ibi_data.append(extension_value_2)
                    # beats_to_replace = eb_value_sequences[s]
                    # beats_to_replace.append(ibi_data[target_index])
                elif (len(new_ibi_data) - target_index) == 1:
                    # if there is only one value after the sequence, that can be used, we extend the original ibi array
                    # by a random normal beat picked from the measurement
                    # choose random element
                    rnd = random.randint(0, len(valid_intervals) - 1)
                    # grab random value from normal beat collection
                    extension_value = valid_intervals[rnd]
                    # extend ibi data set
                    new_ibi_data.append(extension_value)

                elif start_index == 0:
                    # if there is no value before the sequence, e.g. the sequence contains the first few data points
                    # in the ibi data set, we have to account for that by extending the set with a random normal beat
                    # choose random element
                    rnd = random.randint(0, len(valid_intervals) - 1)

                    # grab random value from normal beat collection
                    extension_value = [valid_intervals[rnd]]
                    # extend ibi data set
                    new_ibi_data = extension_value + new_ibi_data
                    # account for shift in the data
                    index_correction += 1
                    start_index += index_correction
                    target_index += index_correction

                # calculation with new ibi data set and target index
                beats_to_replace = sequence_values[s]
                beats_to_replace.append(new_ibi_data[target_index])
                # adapt indices
                eb_ind_seq_adapted = [x + index_correction for x in sequence_indices[s]]
                eb_ind_seq_adapted.append(target_index)
                # indices_to_replace[s].append(eb_ind_seq_adapted)
                indices_to_replace[s] = eb_ind_seq_adapted
                # number_of_beats_to_replace[s].append(len(beats_to_replace))
                number_of_beats_to_replace[s] = len(beats_to_replace)
                # else:
                #     # this is the case when its a single ectopic beat
                #     beats_to_replace = eb_value_sequences[s]
                #     beats_to_replace.append(ibi_data[target_index])
                # according to Lippman 1994 the number of inserted intervals B is calculated by
                # sum[i->i+N](RR_(i)) / ((RR_(i-1)+ RR_(i+N+1) /2), with N = number_of_beats_to_replace
                # calculate the total duration of the interval that needs to be replaced
                sum_of_btr = sum(beats_to_replace)
                # we decide the way of interpolation according to the length of the interval
                if sum_of_btr >= 3000.0:
                    # according to Kamath, artifact sequences over 3 sec should be deleted from the data
                    # interpolation_mode[s].append('delete')
                    interpolation_mode[s] = 'delete'
                else:
                    # interpolation_mode[s].append('interpolate')
                    interpolation_mode[s] = 'interpolate'

                # solution for alternating beats
                # find out if the beat in front of the sequence is a number, if not replace with random for calculation
                if np.isnan(new_ibi_data[start_index - 1]):
                    rnd = random.randint(0, len(valid_intervals) - 1)
                    # grab random value from normal beat collection
                    pre_sequence_beat = valid_intervals[rnd]
                else:
                    # find out if the beat in front of the sequence is valid, if not replace with random for calculation
                    count_matches = 0
                    test_index = start_index - 1
                    for indseq in indices_to_replace:
                        if indseq.count(test_index) == 0:
                            count_matches += 0
                        else:
                            count_matches += 1

                    if count_matches > 0:
                        rnd = random.randint(0, len(valid_intervals) - 1)
                        # grab random value from normal beat collection
                        pre_sequence_beat = valid_intervals[rnd]
                    else:
                        pre_sequence_beat = new_ibi_data[start_index - 1]
                # find out if the beat following the sequence is valid, if not replace with random for calculation
                if np.isnan(new_ibi_data[target_index + 1]):
                    rnd = random.randint(0, len(valid_intervals) - 1)
                    # grab random value from normal beat collection
                    post_sequence_beat = valid_intervals[rnd]
                else:
                    # find out if the beat following the sequence is valid, if not replace with random for calculation
                    test_index = target_index + 1

                    if ibi_max >= new_ibi_data[test_index] >= ibi_min:
                        post_sequence_beat = new_ibi_data[target_index + 1]
                    else:
                        rnd = random.randint(0, len(valid_intervals) - 1)
                        # grab random value from normal beat collection
                        post_sequence_beat = valid_intervals[rnd]
                # calculate the number of beats that need to be inserted
                beats_to_insert = \
                    round(sum_of_btr / ((pre_sequence_beat + post_sequence_beat) / 2))
                # number_of_beats_to_insert[s].append(beats_to_insert)
                # old
                # number_of_beats_to_insert[s] = beats_to_insert

                # new
                number_of_beats_to_insert[s] = int(beats_to_insert)
                if verbose:
                    print('Replace {} outlier(s) with {} interpolated value(s), starting from index {}'
                          .format(number_of_beats_to_replace[s], number_of_beats_to_insert[s], indices_to_replace[s][0]))
        else:
            if verbose:
                print('No sequences found. ')

    return number_of_beats_to_replace, number_of_beats_to_insert, interpolation_mode, new_ibi_data, indices_to_replace


def remove_artifacts(inter_beat_intervals: list, interpolation_mode: List[str], indices_to_replace: List[list]) \
        -> list:
    """
    A function that removes sequences, that were marked as artifacts (i.e. outlier sequences > 3 seconds).

    Parameters
    ---------
    inter_beat_intervals: list
        a list holding inter beat intervals. Cave: use output of prepare_interpolation.
    interpolation_mode: List[str]
        a list with all sequence dismissal indicators.
    indices_to_replace: List[list]
        a list holding all indices of every detected sequence.

    Returns
    ---------
    inter_beat_intervals_za: list
        a list with all inter beat intervals, but without artifact sequences.

    References
    ----------
    """
    # for m in range(len(interpolation_mode)-1):
    #     if interpolation_mode[m] == 'delete':
    #         for i in range(len(indices_to_replace[m])-1):
    #             inter_beat_intervals.pop(i)
    for m in range(len(interpolation_mode)):
        if interpolation_mode[m] == 'delete':
            for i in range(len(indices_to_replace[m])):
                inter_beat_intervals[indices_to_replace[m][i]] = 0
    inter_beat_intervals_za = inter_beat_intervals
    return inter_beat_intervals_za


def prepare_interpolation(inter_beat_intervals: list, interpolation_mode: list, indices_to_replace: List[list],
                          number_of_beats_to_insert: list):
    """
    A function that replaces all outliers in sequences marked for interpolation with NaN. Further it calculates the
    limit, needed for interpolation.

    Parameters
    ---------
    inter_beat_intervals: list
        a list holding inter beat intervals. Cave: use output of calculate_substitution_intervals
    interpolation_mode: List[str]
        a list with all sequence dismissal indicators.
    indices_to_replace: List[list]
        a list holding all indices of every detected sequence.
    number_of_beats_to_insert: list
        number of intervals that will be inserted to replace the sequence marked for interpolation.
    Returns
    ---------
    inter_beat_intervals_cleaned: list
        a list with all inter beat intervals, outliers are marked with NaN.
    limit: int
        the maximum number of subsequent NaN that will be interpolated.

    References
    ----------
    """
    # sequence length
    seq_len = list([])
    mode = 'interpolate'
    index_correction = 0
    temp_ibi_data = inter_beat_intervals
    for m in range(len(interpolation_mode)):
        # print(interpolation_mode[m])
        if interpolation_mode[m] == mode:
            # print(indices_to_replace[m])
            replacement = list([])
            discrepancy = number_of_beats_to_insert[m] - len(indices_to_replace[m])
            if discrepancy == 0:
                for i in range(len(indices_to_replace[m])):
                    temp_ibi_data[indices_to_replace[m][i] + index_correction] = np.nan
                index_correction += discrepancy
            else:
                rep_len = number_of_beats_to_insert[m]
                # correct the indices according to the discrepancy of earlier iterations
                before_rep_seq = indices_to_replace[m][0] - 1 + index_correction
                after_rep_seq = indices_to_replace[m][-1] + 1 + index_correction
                for s in range(rep_len):
                    replacement.append(np.nan)

                # remove indices to replace
                if before_rep_seq == 0:
                    ibi_head = [temp_ibi_data[before_rep_seq]]
                else:
                    ibi_head = temp_ibi_data[0:before_rep_seq] + [temp_ibi_data[before_rep_seq]]

                if after_rep_seq == len(temp_ibi_data):
                    ibi_tail = [temp_ibi_data[after_rep_seq]]
                else:
                    ibi_tail = temp_ibi_data[after_rep_seq:]

                # insert replacement
                inter_beat_intervals_rep = ibi_head + replacement + ibi_tail
                temp_ibi_data = inter_beat_intervals_rep
                # account for added/deleted samples
                index_correction += discrepancy

            seq_len.append(number_of_beats_to_insert[m])

    # set limit for interpolation
    if len(seq_len) > 0:
        limit = max(seq_len) * 2
    else:
        limit = 3

    inter_beat_intervals_cleaned = list([])
    for ibi in temp_ibi_data:
        if ibi == 0:
            pass
        else:
            inter_beat_intervals_cleaned.append(ibi)

    return inter_beat_intervals_cleaned, limit


def remove_ectopic_beats_old(inter_beat_intervals: List[float], method: str = "kamath",
                             custom_removing_rule: float = 0.2, verbose: bool = True) -> list:
    """
    Inter beat intervals differing by more than the removing_rule from the one proceeding it are removed.

    Parameters
    ---------
    inter_beat_intervals : list
        list of inter_beat_intervals.
    method : str
        method to use to clean outlier. malik, kamath, karlsson, acar or custom.
    custom_removing_rule : int
        Percentage criteria of difference with previous inter beat interval at which we consider
        that it is abnormal. If method is set to Karlsson, it is the percentage of difference
        between the absolute mean of previous and next inter beat interval at which  to consider the beat
        as abnormal.
    verbose : bool
        Print information about ectopic beats.
    Returns
    ---------
    nn_intervals : list
        list of NN Interval
    outlier_count : int
        Count of outlier detected in inter_beat_intervals list
    References
    ----------
    .. [5] Kamath M.V., Fallen E.L.: Correction of the Heart Rate Variability Signal for Ectopics \
    and Miss- ing Beats, In: Malik M., Camm A.J.
    .. [6] Geometric Methods for Heart Rate Variability Assessment - Malik M et al
    """
    if method not in [MALIK_RULE, KAMATH_RULE, KARLSSON_RULE, ACAR_RULE, CUSTOM_RULE]:
        raise ValueError("Not a valid method. Please choose between malik, kamath, karlsson, acar.\
         You can also choose your own removing critera with custom_rule parameter.")

    if method == KARLSSON_RULE:
        nn_intervals, outlier_count = _remove_outlier_karlsson(inter_beat_intervals=inter_beat_intervals,
                                                               removing_rule=custom_removing_rule)

    elif method == ACAR_RULE:
        nn_intervals, outlier_count = _remove_outlier_acar(inter_beat_intervals=inter_beat_intervals)

    else:
        # set first element in list
        outlier_count = 0
        previous_outlier = False
        nn_intervals = [inter_beat_intervals[0]]
        for i, rr_interval in enumerate(inter_beat_intervals[:-1]):

            if previous_outlier:
                nn_intervals.append(inter_beat_intervals[i + 1])
                previous_outlier = False
                continue

            if is_outlier(rr_interval, inter_beat_intervals[i + 1], method=method,
                          custom_rule=custom_removing_rule):
                nn_intervals.append(inter_beat_intervals[i + 1])
            else:
                nn_intervals.append(np.nan)
                outlier_count += 1
                previous_outlier = True

    if verbose:
        print("{} ectopic beat(s) have been deleted with {} rule.".format(outlier_count, method))

    return nn_intervals


def remove_ectopic_beats(inter_beat_intervals: List[float], method: str = 'kamath', custom_removing_rule: float = 0.2,
                         verbose: bool = True):
    # set first element in list
    outlier_count = 0
    previous_outlier = False
    nn_intervals = [inter_beat_intervals[0]]
    ectopic_beats = list([])
    ectopic_beat_indices = list([])

    valid_beats = list([inter_beat_intervals[0]])
    valid_beat_indices = list([0])
    for i, ibi in enumerate(inter_beat_intervals[:-1]):

        if previous_outlier:
            nn_intervals.append(inter_beat_intervals[i + 1])
            valid_beats.append(inter_beat_intervals[i + 1])
            valid_beat_indices.append(i + 1)
            previous_outlier = False
            continue

        if is_outlier(ibi, inter_beat_intervals[i + 1], method=method,
                      custom_rule=custom_removing_rule):
            nn_intervals.append(inter_beat_intervals[i + 1])
            valid_beats.append(inter_beat_intervals[i + 1])
            valid_beat_indices.append(i + 1)
        else:
            nn_intervals.append(np.nan)
            ectopic_beats.append(inter_beat_intervals[i + 1])
            ectopic_beat_indices.append(i + 1)
            outlier_count += 1
            previous_outlier = True

    if verbose:
        print("{} ectopic beat(s) have been deleted with {} rule.".format(outlier_count, method))

    return nn_intervals, ectopic_beats, ectopic_beat_indices, valid_beats, valid_beat_indices


def is_outlier(inter_beat_interval: float, next_inter_beat_interval: float, method: str = "kamath",
               custom_rule: float = 0.2) -> bool:
    """
    Test if the inter beat interval is an outlier
    Parameters
    ----------
    inter_beat_interval : float
        inter_beat_interval
    next_inter_beat_interval : float
        consecutive inter_beat_interval
    method : str
        method to use to clean outlier. malik, kamath, karlsson, acar or custom
    custom_rule : float
        percentage criteria of difference with previous inter beat interval at which we consider
        that it is abnormal
    Returns
    ----------
    outlier : bool
        True if inter beat interval is valid, False if not
    """
    if method == MALIK_RULE:
        outlier = abs(inter_beat_interval - next_inter_beat_interval) <= 0.2 * inter_beat_interval
    elif method == KAMATH_RULE:
        # According to Kamath’s suggestion, we considered an abnormal heartbeat when the heartbeat interval increased
        # by more than 32.5 % or decreased by more than 24.5 %
        outlier = 0 <= (next_inter_beat_interval - inter_beat_interval) <= 0.325 * inter_beat_interval or 0 <= \
                  (inter_beat_interval - next_inter_beat_interval) <= 0.245 * inter_beat_interval
    else:
        outlier = abs(inter_beat_interval - next_inter_beat_interval) <= custom_rule * inter_beat_interval
    return outlier


def _remove_outlier_karlsson(inter_beat_intervals: List[float], removing_rule: float = 0.2) -> Tuple[list, int]:
    """
    Inter beat intervals differing by more than the 20 % of the mean of previous and next inter beat interval
    are removed.

    Parameters
    ---------
    inter_beat_intervals : list
        list of inter beat intervals
    removing_rule : float
        Percentage of difference between the absolute mean of previous and next inter beat interval at which \
        to consider the beat as abnormal.
    Returns
    ---------
    nn_intervals : list
        list of NN Interval
    References
    ----------
    .. [7]  Automatic filtering of outliers in RR-intervals before analysis of heart rate \
    variability in Holter recordings: a comparison with carefully edited data - Marcus Karlsson, \
    Rolf Hörnsten, Annika Rydberg and Urban Wiklund
    """
    # set first element in list
    nn_intervals = [inter_beat_intervals[0]]
    outlier_count = 0

    for i in range(len(inter_beat_intervals)):
        # Condition to go out of loop at limits of list
        if i == len(inter_beat_intervals) - 2:
            nn_intervals.append(inter_beat_intervals[i + 1])
            break
        mean_prev_next_ibi = (inter_beat_intervals[i] + inter_beat_intervals[i + 2]) / 2
        if abs(mean_prev_next_ibi - inter_beat_intervals[i + 1]) < removing_rule * mean_prev_next_ibi:
            nn_intervals.append(inter_beat_intervals[i + 1])
        else:
            nn_intervals.append(np.nan)
            outlier_count += 1
    return nn_intervals, outlier_count


def _remove_outlier_acar(inter_beat_intervals: List[float], custom_rule=0.2) -> Tuple[list, int]:
    """
    Inter beat intervals differing by more than the 20 % of the mean of last 9 inter beat intervals
    are removed.
    Parameters
    ---------
    inter_beat_intervals : list
        list of inter beat intervals
    custom_rule : int
        percentage criteria of difference with mean of  9 previous inter beat intervals at
        which we consider that inter beat interval is abnormal. By default, set to 20 %
    Returns
    ---------
    nn_intervals : list
        list of NN intervals
    References
    ----------
    .. [8] Automatic ectopic beat elimination in short-term heart rate variability measurements \
    Acar B., Irina S., Hemingway H., Malik M.
    """
    nn_intervals = []
    outlier_count = 0
    for i, ibi in enumerate(inter_beat_intervals):
        if i < 9:
            nn_intervals.append(ibi)
            continue
        acar_rule_elt = np.nanmean(nn_intervals[-9:])
        if abs(acar_rule_elt - ibi) < custom_rule * acar_rule_elt:
            nn_intervals.append(ibi)
        else:
            nn_intervals.append(np.nan)
            outlier_count += 1
    return nn_intervals, outlier_count


def interpolate_nan_values(inter_beat_intervals: list, interpolation_method: str = "linear", limit=1) -> list:
    """
    Function that interpolate Nan values with linear interpolation.

    Parameters
    ---------
    inter_beat_intervals : list
        inter beat interval list.
    interpolation_method : str
        method used to interpolate Nan values of series.
    limit: int
        length of longest sequence.

    Returns
    ---------
    interpolated_inter_beat_intervals : list
        new list with outliers replaced by interpolated values.
    """
    ibi_series = pd.Series(inter_beat_intervals)
    cycles = 0
    # Interpolate nan values and convert pandas object to list of values
    interpolated_inter_beat_intervals = ibi_series.interpolate(method=interpolation_method, limit=limit,
                                                               limit_area="inside")

    while True:
        nan_check_interpolation = sum(np.isnan(interpolated_inter_beat_intervals))

        if nan_check_interpolation == 0:
            break
        elif cycles > 2:
            i_ibi_series = [ibi for ibi in interpolated_inter_beat_intervals if not np.isnan(ibi)]
            interpolated_inter_beat_intervals = pd.Series(i_ibi_series)
        else:
            interpolated_inter_beat_intervals = \
                interpolated_inter_beat_intervals.interpolate(method=interpolation_method, limit=limit,
                                                              limit_area="inside")
            cycles += 1

    return interpolated_inter_beat_intervals.values.tolist()


def get_nn_intervals_old(inter_beat_intervals: List[float], low_ibi: int = 300, high_ibi: int = 2000,
                         interpolation_method: str = "linear", ectopic_beats_removal_method: str = KAMATH_RULE,
                         verbose: bool = True) -> List[float]:
    """
    Function that computes NN Intervals from inter beat intervals.

    Parameters
    ---------
    inter_beat_intervals : list
        inter beat intervals list.
    interpolation_method : str
        Method used to interpolate Nan values of series.
    ectopic_beats_removal_method : str
        method to use to clean outlier. malik, kamath, karlsson, acar or custom.
    low_ibi : int
        lowest RrInterval to be considered plausible.
    high_ibi : int
        highest RrInterval to be considered plausible.
    verbose : bool
        Print information about deleted outliers.
    Returns
    ---------
    interpolated_nn_intervals : list
        list of NN Interval interpolated
    """
    inter_beat_intervals_cleaned = remove_outliers(inter_beat_intervals, low_ibi=low_ibi, high_ibi=high_ibi,
                                                   verbose=verbose)
    interpolated_inter_beat_intervals = interpolate_nan_values(inter_beat_intervals_cleaned, interpolation_method)
    nn_intervals = remove_ectopic_beats_old(interpolated_inter_beat_intervals,
                                            method=ectopic_beats_removal_method)
    interpolated_nn_intervals = interpolate_nan_values(nn_intervals, interpolation_method)
    return interpolated_nn_intervals

# -------------------------------------------------------------------------------------------------------------------- #


def get_nn_intervals(inter_beat_intervals: List[float], low_ibi: int = 300, high_ibi: int = 1333,
                     interpolation_method: str = "linear", ectopic_beats_removal_method: str = KAMATH_RULE,
                     sampling_frequency: int = 64, verbose: bool = False):
    """
    Function that computes NN Intervals from inter beat intervals.

    Parameters
    ---------
    inter_beat_intervals : list
        inter beat intervals list. Units of samples.
    interpolation_method : str
        Method used to interpolate Nan values of series.
    ectopic_beats_removal_method : str
        method to use to clean outlier. malik, kamath, karlsson, acar or custom.
    low_ibi : int
        lowest RrInterval to be considered plausible.
    high_ibi : int
        highest RrInterval to be considered plausible.
    sampling_frequency: int
        sampling frequency of the bvp raw data set.
    verbose : bool
        Print information about deleted outliers.
    Returns
    ---------
    interpolated_nn_intervals : list
        list of NN Interval interpolated
    """
    # converse units to ms
    inter_beat_intervals_ms = samples_to_ms(inter_beat_intervals=inter_beat_intervals,
                                            sampling_frequency=sampling_frequency)

    # find outliers
    inter_beat_intervals_mo, outlier_list, outlier_indices, valid_list, valid_indices = \
        remove_outliers(inter_beat_intervals_ms, low_ibi=low_ibi, high_ibi=high_ibi, verbose=verbose)

    if not empty_check(outlier_list):
        # check for sequences of outliers
        o_sequence_indices, o_sequence_values = find_sequences(outlier_indices=outlier_indices,
                                                               outlier_values=outlier_list, verbose=verbose)

        # calculate size of substitution intervals
        outliers_to_replace, outliers_to_insert, interpolation_mode, new_ibi_data, outlier_indices_to_replace = \
            calculate_substitution_intervals(inter_beat_intervals=inter_beat_intervals_ms,
                                             outlier_indices=outlier_indices, sequence_indices=o_sequence_indices,
                                             sequence_values=o_sequence_values, valid_intervals=valid_list,
                                             verbose=True)

        # check for artifact sequences
        inter_beat_intervals_za = remove_artifacts(inter_beat_intervals=new_ibi_data,
                                                   interpolation_mode=interpolation_mode,
                                                   indices_to_replace=outlier_indices_to_replace)

        # insert substitution intervals, remove artifact intervals, calculate interpolation limit
        inter_beat_intervals_cleaned, o_limit = prepare_interpolation(inter_beat_intervals=inter_beat_intervals_za,
                                                                      interpolation_mode=interpolation_mode,
                                                                      indices_to_replace=outlier_indices_to_replace,
                                                                      number_of_beats_to_insert=outliers_to_insert)
        # interpolate outliers
        interpolated_inter_beat_intervals = interpolate_nan_values(inter_beat_intervals=inter_beat_intervals_cleaned,
                                                                   interpolation_method=interpolation_method,
                                                                   limit=o_limit)
    else:
        interpolated_inter_beat_intervals = inter_beat_intervals_ms

    # remove ectopic beats according to kamath method
    nn_intervals, ectopic_beat_list, ectopic_beat_indices, valid_beat_list, valid_beat_indices = \
        remove_ectopic_beats(inter_beat_intervals=interpolated_inter_beat_intervals,
                             method=ectopic_beats_removal_method, verbose=True)

    if not empty_check(ectopic_beat_list):
        # todo: using this part of the algorithm causes immense rise in energy of the ULF and LF components
        # # check for sequences of ectopic beats
        # eb_sequence_indices, eb_sequence_values = find_sequences(outlier_indices=ectopic_beat_indices,
        #                                                          outlier_values=ectopic_beat_list, verbose=True)
        #
        # # calculate the size of substitution intervals
        # ectopic_beats_to_replace, ectopic_beats_to_insert, interpolation_mode, new_nn_data, eb_indices_to_replace = \
        #     calculate_substitution_intervals(inter_beat_intervals=nn_intervals,
        #                                      outlier_indices=ectopic_beat_indices, sequence_indices=eb_sequence_indices,
        #                                      sequence_values=eb_sequence_values, valid_intervals=valid_list, verbose=True)
        #
        # # check for artifacts
        # nn_intervals_za = remove_artifacts(inter_beat_intervals=new_nn_data, interpolation_mode=interpolation_mode,
        #                                    indices_to_replace=eb_indices_to_replace)
        #
        # # insert substitution intervals, remove artifact intervals, calculate interpolation limit
        # nn_intervals_cleaned, eb_limit = prepare_interpolation(inter_beat_intervals=nn_intervals_za,
        #                                                        interpolation_mode=interpolation_mode,
        #                                                        indices_to_replace=eb_indices_to_replace,
        #                                                        number_of_beats_to_insert=ectopic_beats_to_insert)

        # interpolate ectopic beats
        interpolated_nn_intervals = interpolate_nan_values(inter_beat_intervals=nn_intervals,
                                                           interpolation_method=interpolation_method, limit=2)
        # if any NaN are left run interpolation again
        # nan_found = nan_check(interpolated_nn_intervals)
    else:
        interpolated_nn_intervals = interpolated_inter_beat_intervals

    # data sample validation
    outlier_total = len(outlier_list)
    validation_result = is_valid_sample(nn_intervals=interpolated_nn_intervals, outlier_count=outlier_total,
                                        removing_rule=0.2)

    return interpolated_nn_intervals, interpolated_inter_beat_intervals, validation_result


# ----------------- Data Sample Validation ----------------- #


def empty_check(a_list: list):
    """
    A function that checks if a list is empty.

    Parameters
    ---------
    a_list: list
        a list.

    Returns
    ---------
    True, False: bool

    """
    if len(a_list) == 0:
        return True
    else:
        return False


def nan_check(data: list, verbose: bool = False) -> bool:
    """
    A function that checks for NaN values in a list.

    Parameters
    ---------
    data: list
        any list.
    verbose: bool
        if True, additional information will be printed.

    Returns
    ---------
    True, False: bool

    """
    # if type(data) == np.ndarray:
    #     pass
    # else:
    #     data = np.array(data)
    nan_found = np.isnan(data)

    if nan_found.any():
        return True
    else:
        return False


def is_valid_sample(nn_intervals: List[float], outlier_count: int, removing_rule: float = 0.04) -> bool:
    """
    Test if the sample meet the condition to be used for analysis.

    Parameters
    ----------
    nn_intervals : list
        list of Normal to Normal Interval
    outlier_count : int
        count of outliers or ectopic beats removed from the interval
    removing_rule : str
        rule to follow to determine whether the sample is valid or not
    Returns
    ----------
    bool
        True if sample is valid, False if not
    """
    result = True
    if (outlier_count / len(nn_intervals)) > removing_rule:
        print("Too much outlier for analyses ! You should discard the sample.")
        result = False
    if len(nn_intervals) < 240:
        print("Not enough Heart beat for Nyquist criteria ! ")
        result = False
    return result
