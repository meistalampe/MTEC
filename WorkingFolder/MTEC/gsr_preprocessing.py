#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script provides all methods necessary to prepare the gsr data for feature extraction. Including all necessary
   steps to extract tonic and phasic components from the raw gsr data as well as several methods to clear the data from
   any artifacts."""

from scipy.signal import butter, filtfilt, tf2zpk
from typing import Tuple
from typing import List
import math
import random
import statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

__all__ = ["lowpass_butterworth", "gsr_zero_phase_filtering", 'gsr_generate_moving_averages']


def lowpass_butterworth(filter_order: int, cutoff_frequency: float, sampling_frequency: int) \
        -> Tuple[np.ndarray, np.ndarray]:
    """
    Function that creates a Butterworth lowpass filter, with a certain cutoff frequency.

    Parameters
    ----------
    filter_order: int
        order of the filter.
    cutoff_frequency: float
        frequency at which the cutoff will set in.
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
    low_cut = cutoff_frequency / nyquist_frequency
    print(low_cut)
    if low_cut == 1.0:
        low_cut = 0.99
    b, a = butter(filter_order, [low_cut], btype='low')
    filter_polynomials = (b, a)
    return filter_polynomials


def gsr_zero_phase_filtering(data: np.ndarray, sampling_frequency: int, f_cut: float = 1.0, filter_order: int = 4,
                             verbose: bool = False) -> np.ndarray:
    """
    Filter function using a zero phase second order Butterworth filter, with lowpass at f_cut, is implemented
    to remove baseline wander and high frequencies.

    Parameters
    ----------
    data: np.ndarray
        one dimensional signal that will be filtered.
    f_cut: float
        frequency at which the cutoff will set in.
    sampling_frequency: int
        sampling frequency used in data acquisition.
    filter_order: int
        order of the filter. The default order which is used in this scenario is 4.
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
    filter_polynomials = lowpass_butterworth(filter_order=filter_order, cutoff_frequency=f_cut,
                                             sampling_frequency=sampling_frequency)

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
        plt.figure(dpi=1200)
        plt.plot(data, linewidth=1.0, label='input')
        plt.plot(s_n_gust, color='black', linewidth=1.0, label='gust')
        plt.show()
    return s_n_gust


def gsr_generate_moving_averages(data: np.ndarray, sampling_frequency: int, window: float, mode: str,
                                 verbose: bool = False) -> np.ndarray:
    """
    Function that generates a moving averages.

    Parameters
    ----------
    data: np.ndarray
        one dimensional input signal.
    sampling_frequency: int
        sampling frequency used in acquisition of data parameter.
    window: float
        sets window size for peak detection.
    mode: str
        convolution mode, decides how signal edges are handled.
    verbose: bool
        print information about function progress.

    Returns
    ----------
    moving_average: np.ndarray
        mov avg.

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
    N_1 = math.floor(window * sampling_frequency)
    # next we have to guarantee the window extends equally to both sides of the current sample
    # therefore we provide it is the size of the nearest uneven integer
    if N_1 % 2 == 0:
        N_1 = N_1 + 1

    # we calculate the moving avg by convolving with a kernel function
    # the kernel has the size of our window and his coefficients provide the same result as a mov avg
    # coeff = 1/N, N being the window size
    # modes are valid, full and same
    moving_average = np.convolve(y_n, np.ones((N_1,)) / N_1, mode=mode)
    # repeat for beat region of interest and beat mov avg
    return moving_average
