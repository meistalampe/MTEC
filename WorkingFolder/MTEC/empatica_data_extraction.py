#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script provides all methods necessary to extract the raw data from the csv files provided by the matlab
   recording protocol."""

import os
import csv
import collections
from typing import Tuple
from typing import List
import numpy as np
import scipy.io as sio
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

__all__ = ['data_extraction', 'print_header', 'get_folder_from_user', 'search_for_latest_file', 'parse_file_for_tag',
           'get_stream_data', 'get_stream_time', 'extract_all','save_dict_to_mat', 'write_to_text_file',
           'read_list_from_text_file', 'write_dict_to_csv']


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
    latest_file: str
        returns current filename.
    References
    -----------
    No references needed.
    """
    if not folder:
        print("We can't search file in this location.")
        return
    else:
        pass
        # print(folder)

    latest_file = search_for_latest_file(folder=folder, search_text=file_label, verbose=verbose)
    stream = parse_file_for_tag(file_path=latest_file, stream_tag=stream_tag)
    data = get_stream_data(stream=stream)
    time = get_stream_time(stream=stream)
    return data, time, latest_file


def extract_all(folder: str, file_label: str, verbose: bool = False):
    """
    A function that executes data extraction for all possible tags.

    Parameters
    ----------
    folder: string
        full path to the data folder.
    file_label: str
        look for file_label in data folder files.
    verbose: bool
        print information about function progress.

    Returns
    ----------
    data: dictionary

    References
    -----------
    No references needed.
    """
    stream_tags = list(['E4_Acc', 'E4_Bvp', 'E4_Gsr', 'E4_Temperature', 'E4_Tag'])
    # stream_fs = list([32, 64, 4, 4, 0])

    stream_data = {
        'Filename': '',
        'E4_Acc_data': [],
        'E4_Acc_time': [],
        'E4_Bvp_data': [],
        'E4_Bvp_time': [],
        'E4_Gsr_data': [],
        'E4_Gsr_time': [],
        'E4_Temperature_data': [],
        'E4_Temperature_time': [],
        'E4_Tag_data': [],
        'E4_Tag_time': [],
    }

    for tag in stream_tags:
        data_name = tag + '_data'
        time_name = tag + '_time'

        stream_data[data_name], stream_data[time_name], stream_data['Filename'] = \
            data_extraction(folder=folder, stream_tag=tag,  file_label=file_label, verbose=verbose)

        if verbose:
            if stream_data[data_name].size > 0:
                print('Tag: {} was successfully extracted from file.'.format(tag))
            else:
                print('Could not locate {}. No data with this tag extracted.'.format(tag))

    return stream_data


def print_header(program_label: str):
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
    print('                  ' + program_label)
    print('--------------------------------------------------')
    print()


def get_folder_from_user(default_folder_name: str) -> str:
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
        # default_folder = 'DataRepository'
        folder_path = os.path.abspath(os.path.join('.', 'MTEC', default_folder_name))
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
            print('Latest file: ', latest_file.name)

        file_path = os.path.abspath(os.path.join(folder, latest_file.name))
        return file_path
    else:
        print('Folder is empty. No file name returned.')
        return ''


def parse_file_for_tag(file_path: str, stream_tag: str, verbose: bool = False) -> List[Sample]:
    """
    Function that retrieves the name of the most recently created/edited file in the data folder.
    Parameters
    ----------
    file_path: string
        full path of the csv file containing the raw data recorded from the empatica E4 device.
    stream_tag: string
        tag to indicate for which kind of data the file will be parsed
    verbose: bool
        if true print additional information.

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
            if verbose:
                print('We could not find a stream with the tag {}.'.format(stream_tag))
                print()
            return []


def get_stream_data(stream: List[Sample], verbose: bool = False) -> np.ndarray:
    """
    Function that extracts the value element from a list of Samples.
    Parameters
    ----------
    stream: list[Samples]
        list of samples with a certain tag that were retrieved from the raw data file.
    verbose: bool
        if true print additional information.

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
        if verbose:
            print('The stream is empty! Could not extract data.')
            print()
        return np.array([])


def get_stream_time(stream: List[Sample], verbose: bool = False) -> np.ndarray:
    """
    Function that extracts the time element of a list of Samples.

    Parameters
    ----------
    stream: list[Samples]
        list of samples with a certain tag that were retrieved from the raw data file.
    verbose: bool
        if true print additional information.

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
        # time_in_seconds = time - time[0]
        # return time_in_seconds
        return time
    else:
        if verbose:
            print('The stream is empty! Could not extract time.')
            print()
        return np.array([])


def save_dict_to_mat(dictionary: dict, data_file_name: str, save_file_label: str,
                     verbose: bool = False):
    """
    A function that saves a dictionary to a mat file.

    Parameters
    ----------
    dictionary: dict
        a dictionary holding some kind of information or results from processing a data file.

    data_file_name: str
        name of the data file whose information was stored in dictionary.

    verbose: bool
        if True print information about saving process.

    save_file_label: str
        prefix to identify the contents of dictionary.

    Returns
    ----------
    None

    References
    -----------
    No references needed.
    """
    save_file_label = '_' + save_file_label + '.mat'
    save_file_name = data_file_name + save_file_label
    sio.savemat(save_file_name, dictionary)

    if verbose:
        print('File has been saved to path: {}'.format(save_file_name))


def write_to_text_file(file_name: str, file_index: str, folder: str, data_list: List, file_type: str = '.txt'):
    """
        A function that writes a list to a text file, line by line.

        Parameters
        ----------
        file_name: str
            name of the data file that will be created

        file_index: str
            index, which is added to the file_name for identification, usually subject initials

        folder: str
            folder to which the file will be saved

        data_list: List[Sample]
            list that will be stored in the new file.

        file_type: str
            file ending, file type

        Returns
        ----------
        None

        References
        -----------
        No references needed.
        """
    # create file name
    file_name = file_name + file_index + file_type
    file_path = os.path.abspath(os.path.join(folder, file_name))

    # create merge file
    if os.path.isfile(file_path):
        # clear and then write
        print('file found')
        file = open(file_path, 'w')
        file.truncate()
        print('file cleared')
        file.close()
    else:
        file = open(file_path, 'w')
        print('new file created')
        file.close()

    with open(file_path, 'w') as fout:
        for i in data_list:
            fout.write(str(i))
            fout.write('\n')


def read_list_from_text_file(file_path: str):
    stream = list()
    with open(file_path) as f:
        for line in f:
            stream.append(line.rstrip('\n'))
    return stream


def write_dict_to_csv(my_dict: dict, file_name: str, folder: str = 'FeatureRepository',
                      header: List[str] = ['feature', 'value']):
    """
    A function that takes a dictionary and writes its content to a csv file.

    Parameters
        ----------
        my_dict: dict
            the dictionary that will be saved to the file

        file_name: str
            name of the data file that will be created

        folder: str
            folder to which the file will be saved, default is set to FeatureRepository

        header: List[str]
            first line of the csv file, contains all keys of the dictionary, default is set to feature and value


        Returns
        ----------
        None

        References
        -----------
        No references needed.
        """

    csv_columns = header
    dict_data = my_dict

    # create file name
    csv_file = file_name + '.txt'
    file_path = os.path.abspath(os.path.join('MTEC', folder, csv_file))

    # if os.path.isfile(file_path):
    #     # clear and then write
    #     print('File found.')
    #     file = open(file_path, 'w')
    #     file.truncate()
    #     print('File cleared.')
    #     file.close()
    # else:
    #     file = open(file_path, 'w')
    #     print('New file created.')
    #     file.close()

    try:
        with open(file_path, 'w', newline='') as csvout:
            my_writer = csv.writer(csvout, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            my_writer.writerow(header)
            for key in dict_data.keys():
                my_writer.writerow([key] + [dict_data[key]])

    except IOError:
        print("I/O ERROR")


if __name__ == '__main__':
    main()
