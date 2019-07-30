"""
Title: extract_data_from_device.py
Author: Dominik Limbach
Date: 07.06.2019
Description:
Block 1:
    - load data from csv file in DataRepository
    - parse data for tag
    - extract data streams according to tag
Block 2:
    - process data
    - extract features
Block 3:
    - machine learning block
    - train classifier
"""
import os
import collections
import numpy as np
import matplotlib.pyplot as plt

Sample = collections.namedtuple('Sample',
                                'tag, time, value')


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("We can't search file in this location.")
        return
    else:
        print(folder)

    search_text = 'rec'
    latest_file = search_for_latest_file(folder, search_text)
    # print(latest_file)
    stream_tag = 'E4_Gsr'
    stream = parse_file_for_tag(latest_file, stream_tag)
    # print(stream)
    data = get_stream_data(stream)
    time = get_stream_time(stream)

    plt.plot(data)
    plt.show()
    # features = feature_extraction()
    # todo: implement machine learning block


def print_header():
    print('--------------------------------------------------')
    print('                   MTEC APP')
    print('--------------------------------------------------')
    print()


def get_folder_from_user():

    folder = input('Where is your data file located? [Press <enter> to use default path]: ')

    if not folder or not folder.strip():    # check if input is empty, if so return default path
        print('Using default path.')
        print()
        default_folder = 'DataRepository'
        return os.path.abspath(os.path.join('.', "MTEC", default_folder))

    if not os.path.isdir(folder):   # check if input path is a directory
        return None

    return os.path.abspath(folder)  # if input path is a directory return it


def search_for_latest_file(folder, search_text):
    all_files = []
    for entry in os.scandir(folder):
        if entry.name.startswith(search_text) and entry.is_file():
            # file_size = str(os.path.getsize(entry))
            # print(entry.name + '    size: ' + file_size + 'Bytes ')
            all_files.append(entry)

    latest_file = max(all_files, key=os.path.getctime)
    # print(latest_file.name)
    return os.path.abspath(os.path.join(folder, latest_file.name))


def parse_file_for_tag(filename, stream_tag):
    with open(filename, 'r', encoding='utf-8') as fin:
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


def get_stream_data(stream: Sample, return_type='ndarray'):
    values = []
    if stream:
        for s in stream:
            v_str = s.value.rstrip()
            v_clr = v_str.replace(',', '.')
            v = float(v_clr)
            values.append(v)

        if return_type == 'list':
            data = values
        elif return_type == 'ndarray':
            data = np.array(values)
        else:
            print('ERROR: choose a proper return type. ["ndarray, "list"].')
            print('CAVE: data returned as type "list".')
            print()
            data = values

        return data
    else:
        print('The stream is empty! Could not extract data.')
        print()
        return []


def get_stream_time(stream: Sample, return_type='ndarray'):
    times = []
    if stream:
        for s in stream:
            t_str = s.time.rstrip()
            t_clr = t_str.replace(',', '.')
            t = float(t_clr)
            times.append(t)

        if return_type == 'list':
            time = times
            time_in_seconds = [x - time[0] for x in time]
        elif return_type == 'ndarray':
            time = np.array(times)
            time_in_seconds = time - time[0]
        else:
            print('ERROR: choose a proper return type. ["ndarray, "list"].')
            print('CAVE: data returned as type "list".')
            print()
            time = times
            time_in_seconds = [x - time[0] for x in time]

        return time_in_seconds
    else:
        print('The stream is empty! Could not extract time.')
        print()
        return []


if __name__ == '__main__':
    main()


