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
    label = 'CUT SEGMENT'
    print_header(program_label=label)

    # Get user input
    folder = get_folder_from_user(default_folder_name='ProcessingRepository')
    if not folder:
        print("We can't search file in this location.")
        return
    else:
        print(folder)

    # Get user input: subject name
    subject = input('Please enter subject initials.')

    while True:
        # Get user input: file name
        file_name = input('Please enter file name.')
        if subject in file_name:
            if 'bvp' in file_name:
                fs = 64
                print('Data type = bvp, sampling frequency set to ' + str(fs))
                break
            elif 'gsr' in file_name:
                fs = 4
                print('Data type = gsr, sampling frequency set to ' + str(fs))
                break
            elif 'temp' in file_name:
                fs = 4
                print('Data type = temp, sampling frequency set to ' + str(fs))
                break
            elif 'tag' in file_name:
                fs = 0
                print('Data type = tag, sampling frequency set to ' + str(fs))
                break
            else:
                print('Invalid data type. Please try again')
        else:
            print('Mismatch error: file_name and subject ID do not match.')

    full_name = file_name + '.txt'
    file_path = os.path.abspath(os.path.join(folder, full_name))
    stream = read_list_from_text_file(file_path=file_path)

    segment_starts_at: str = input('Please enter the starting time of the segment in seconds from the start of the '
                              'measurement.')
    segment_ends_at: str = input('Please enter the ending time of the segment in seconds from the start of the '
                            'measurement.')

    total_length = len(stream)/fs
    if 0 <= int(segment_starts_at) <= total_length:
        start_sample = int(int(segment_starts_at) * fs)

        if 0 <= int(segment_ends_at) <= total_length:
            end_sample = int(int(segment_ends_at) * fs)
            segment = stream[start_sample:end_sample]
        else:
            print('Invalid end sample.')
    else:
        print('Invalid start sample.')

    # enter segment label
    label_segment = '_' + input('Please label the segment.') + '_' + segment_starts_at + '_' + segment_ends_at
    write_to_text_file(file_name=file_name, file_index=label_segment, folder=folder, data_list=segment)


if __name__ == '__main__':
    main()
