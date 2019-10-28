import os
from typing import List

from empatica_data_extraction import *


def main():
    """
    A function that reads a data file, stores its contents into a list and extracts the time segment, specified by two
    timestamps as specified by the user. Afterwards the segment is saved into a new file.
    """

    # set info display
    set_verbose = False

    # sampling frequencies
    fs_dict = {
        'bvp': 64,
        'gsr': 4,
        'temp': 4,
        'tag': 0
    }

    # ----------------- DATA EXTRACTION ----------------- #
    label = 'CUT ALL SEGMENTS'
    print_header(program_label=label)

    # Get user input
    folder = get_folder_from_user(default_folder_name='ProcessingRepository')
    if not folder:
        print("We can't search file in this location.")
        return
    else:
        print(folder)

    all_files = ["_bvp_data_", "_gsr_data_", "_temp_data_", "_bvp_time_", "_gsr_time_", "_temp_time_"]
    # Get user input: subject name
    subject = input('Please enter subject initials.')
    # Get user input: segment label
    s_label = input('Please label the segment.')
    # Get user input: segment times
    segment_starts_at: str = input('Please enter the starting time of the segment in seconds from the start of the '
                                   'measurement.')
    segment_ends_at: str = input('Please enter the ending time of the segment in seconds from the start of the '
                                 'measurement.')
    for f in all_files:
        file_name = f + subject

        if 'bvp' in file_name:
            fs = 64
            print('Data type = bvp, sampling frequency set to ' + str(fs))
        elif 'gsr' in file_name:
            fs = 4
            print('Data type = gsr, sampling frequency set to ' + str(fs))
        elif 'temp' in file_name:
            fs = 4
            print('Data type = temp, sampling frequency set to ' + str(fs))
        elif 'tag' in file_name:
            fs = 0
            print('Data type = tag, sampling frequency set to ' + str(fs))
        else:
            print('Invalid data type. Please try again')
            fs = 0

        full_name = file_name + '.txt'
        file_path = os.path.abspath(os.path.join(folder, full_name))
        stream = read_list_from_text_file(file_path=file_path)

        total_length = len(stream) / fs
        if 0 <= int(segment_starts_at) <= total_length:
            start_sample = int(int(segment_starts_at) * fs)

            if 0 <= int(segment_ends_at) <= total_length:
                end_sample = int(int(segment_ends_at) * fs)
                segment = stream[start_sample:end_sample]
            else:
                print('Invalid end sample.')
                segment = []
        else:
            print('Invalid start sample.')
            segment = []

        # enter segment label
        label_segment = '_' + s_label + '_' + segment_starts_at + '_' + segment_ends_at
        write_to_text_file(file_name=file_name, file_index=label_segment, folder=folder, data_list=segment)


if __name__ == '__main__':
    main()
