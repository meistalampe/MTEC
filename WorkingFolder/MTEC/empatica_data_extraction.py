#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script provides all methods necessary to extract the raw data from the csv files provided by the matlab
   recording protocol."""

import os
import collections
from typing import Tuple
from typing import List
import numpy as np
import matplotlib.pyplot as plt

# Initialize named tuple Sample
Sample = collections.namedtuple('Sample',
                                'tag, time, value')
# Types of recorded data
data_tags = list(['E4_Acc', 'E4_Bvp', 'E4_Gsr', 'E4_Temperature', 'E4_Ibi', 'E4_Hr', 'E4_Battery',
                  'E4_Tag'])
# E4_Acc: Acceleration data
#   - The acceleration value for x axis.The x axis is defined by the vector whose starting point is set to the center of
#   the device and whose direction points towards the USB slot.
#   - The acceleration value for y axis.The y axis is defined by the vector whose starting point is set to the center of
#   the device and whose direction points towards the shorter strap.
#   - The acceleration value for z axis.The z axis is defined by the vector whose starting point is set to the center of
#   the device and whose direction points towards the bottom of the device.
# E4_Bvp: Blood volume pulse data
#   - The value of the BVP sample. The value is derived from the light absorbance of the arterial blood. The raw signal
#   is filtered to remove movement artifacts.
# E4_Gsr: Galvanic skin response data
#   - The value of the GSR sample. The value is expressed in microsiemens.
# E4_Temperature: Temperature data
#   - The value of the temperature sample in Celsius degrees. The value is derived from the optical temperature sensor
#   placed on the wrist.
# E4_Ibi: Inter beat interval data
#   - The value of the IBI sample. The value is the distance from the previous detected heartbeat in seconds.
# E4_Hr: Heart rate data
#   - The value of the detected heartbeat, returned together with the inter beat interval data.
# E4_Battery: Battery level data
#   - The battery level of the device. Values: [0.0 - 1.0]
# E4_Tag: Tag data
#   - The tags taken from the device. Time values.

__all__ = ['data_extraction', 'print_header', 'get_folder_from_user', 'search_for_latest_file', 'parse_file_for_tag', 'get_stream_data',
           'get_stream_time']


# ----------------- UI / User Input ----------------- #
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
    data = get_stream_data(stream)
    time = get_stream_time(stream)


def data_extraction(folder: str, stream_tag: str, file_label: str, verbose: bool = False):
    """
    Function that prints a program header. Requires initial execution of the function get_folder_from_user.
    Parameters
    ----------
    folder: string
        full path to the data folder.
    stream_tag: str
        tag decides which data stream will be extracted.
    file_label: str
        look for file_label in data folder files.
    verbose: bool
        print information about function progress.

    Returns
    ----------
    data: np.ndarray
        numpy array holding raw data values.
    time: np.ndarray
        numpy array holding time values.

    References
    -----------
    No references needed.
    """
    if not folder:
        print("We can't search file in this location.")
        return
    else:
        print(folder)

    latest_file = search_for_latest_file(folder=folder, search_text=file_label, verbose=verbose)
    stream = parse_file_for_tag(file_path=latest_file, stream_tag=stream_tag)
    data = get_stream_data(stream=stream)
    time = get_stream_time(stream=stream)
    return data, time


def print_header():
    """
    Function that prints a program header.
    Parameters
    ----------
    Function takes no input parameters.

    Returns
    ----------
    Function returns nothing.

    References
    -----------
    No references needed.
    """
    print('--------------------------------------------------')
    print('                   MTEC APP')
    print('--------------------------------------------------')
    print()


def get_folder_from_user() -> str:
    """
    Function that handles user input regarding the folder in which the data recordings have been stored.
    Parameters
    ----------
    Function takes no input parameters.

    Returns
    ----------
    folder_path: string
        the complete system path of the data folder.

    References
    -----------
    No references needed.
    """

    # input request for folder path
    folder = input('Where is your data file located? [Press <enter> to use default path]: ')
    # check if input is empty, if so return default path
    if not folder or not folder.strip():
        print('Using default path.')
        print()
        default_folder = 'DataRepository'
        folder_path = os.path.abspath(os.path.join('.', 'MTEC', default_folder))
        return folder_path
    # check if input path is a directory
    if not os.path.isdir(folder):
        print('Input is not a valid folder path.')
        return ''
    # if input path is a directory return it
    folder_path = os.path.abspath(folder)
    return folder_path


def search_for_latest_file(folder: str, search_text: str, verbose: bool = False) -> str:
    """
    Function that retrieves the name of the most recently created/edited file in the data folder.
    Parameters
    ----------
    folder: string
        full path of the folder in which the data files are stored.
    search_text: string
        text fragment to find recording files by comparing to file name.
    verbose: bool
        print information about function progress.

    Returns
    ----------
    file_path: string
        full path of the most recently created/ edited file in the data folder.

    References
    -----------
    No references needed.
    """
    # list holding all filenames in folder
    all_files = []
    # search folder for files with names matching search_text
    for entry in os.scandir(folder):
        if entry.name.startswith(search_text) and entry.is_file():
            # file_size = str(os.path.getsize(entry))
            # print(entry.name + '    size: ' + file_size + 'Bytes ')
            all_files.append(entry)

    # check if any files were found
    if len(all_files) > 0:
        # get latest file from all_files
        latest_file = max(all_files, key=os.path.getctime)

        if verbose:
            print('Latest file:', latest_file.name)

        file_path = os.path.abspath(os.path.join(folder, latest_file.name))
        return file_path
    else:
        print('Folder is empty. No file name returned.')
        return ''


def parse_file_for_tag(file_path: str, stream_tag: str) -> List[Sample]:
    """
    Function that retrieves the name of the most recently created/edited file in the data folder.
    Parameters
    ----------
    file_path: string
        full path of the csv file containing the raw data recorded from the empatica E4 device.
    stream_tag: string
        tag to indicate for which kind of data the file will be parsed

    Returns
    ----------
    stream: List[Sample]
        list holding the samples of the chosen data stream.

    References
    -----------
    No references needed.
    """
    with open(file_path, 'r', encoding='utf-8') as fin:
        all_samples = [Sample(*(line.split(' '))) for line in fin]
        stream = []
        for s in all_samples:
            if s.tag == stream_tag:
                stream.append(s)

        if stream:
            return stream
        else:
            print('We could not find a stream with the tag {}.'.format(stream_tag))
            print()
            return []


def get_stream_data(stream: List[Sample]) -> np.ndarray:
    """
    Function that extracts the value element from a list of Samples.
    Parameters
    ----------
    stream: list[Samples]
        list of samples with a certain tag that were retrieved from the raw data file.

    Returns
    ----------
    data: ndarray
        extracted data values from the list of Samples. Unit of the values is in samples.

    References
    -----------
    No references needed.
    """
    # list for value elements of Sample stream
    values = []
    # check if stream is empty
    if stream:
        # store values in the list
        for s in stream:
            v_str = s.value.rstrip()
            v_clr = v_str.replace(',', '.')
            v = float(v_clr)
            values.append(v)

        data = np.array(values)
        return data
    else:
        print('The stream is empty! Could not extract data.')
        print()
        return np.array([])


def get_stream_time(stream: List[Sample]) -> np.ndarray:
    """
    Function that extracts the time element of a list of Samples.
    Parameters
    ----------
    stream: list[Samples]
        list of samples with a certain tag that were retrieved from the raw data file.

    Returns
    ----------
    time_in_seconds: ndarray
         extracted timestamps from the Sample list that have been translated into difference in seconds
         from the start of the recording.

    References
    -----------
    No references needed.
    """
    # list to store all timestamps
    times = []
    # check if stream is empty
    if stream:
        # extract time elements from list of Samples
        for s in stream:
            t_str = s.time.rstrip()
            t_clr = t_str.replace(',', '.')
            t = float(t_clr)
            times.append(t)

        # transform timestamps into values of seconds

        time = np.array(times)
        time_in_seconds = time - time[0]
        return time_in_seconds
    else:
        print('The stream is empty! Could not extract time.')
        print()
        return np.array([])


if __name__ == '__main__':
    main()
