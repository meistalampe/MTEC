import os
import csv
import collections
from empatica_data_extraction import *
# Initialize named tuple Sample
Sample = collections.namedtuple('Sample',
                                'tag, time, value')


def main():

    verbose = False
    # print header
    label = 'MERGE CSV'
    print_header(program_label=label)

    # ----------------- DATA EXTRACTION ----------------- #

    # # Get user input: folder name
    # folder = input('Where is your data file located? [Press <enter> to use default path]: ')
    # # check if input is empty, if so return default path
    # folder_path = ''
    # if not folder or not folder.strip():
    #     print('Using default path.')
    #     print()
    #     default_folder = 'MergeRepository'
    #     folder_path = os.path.abspath(os.path.join('.', 'MTEC', default_folder))
    #
    # # check if input path is a directory
    # elif not os.path.isdir(folder):
    #     print('Input is not a valid folder path.')
    #     pass
    # # if input path is a directory return it
    # else:
    #     folder_path = os.path.abspath(folder)

    # Get user input
    folder = get_folder_from_user(default_folder_name='MergeRepository')
    if not folder:
        print("We can't search file in this location.")
        return
    else:
        print(folder)

    # Get user input: subject name
    subject = input('Please enter subject initials.')

    # create merge file
    file_name = 'merged_raw_data_' + subject + '.txt'
    file_path = os.path.abspath(os.path.join(folder, file_name))
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

    # find all raw data files
    # list holding all filenames in folder
    all_files = []
    # search folder for files with names matching search_text
    search_text = 'recording'
    for entry in os.scandir(folder):
        if entry.name.startswith(search_text) and entry.is_file():
            # file_size = str(os.path.getsize(entry))
            # print(entry.name + '    size: ' + file_size + 'Bytes ')
            all_files.append(entry)

    # merge all files
    stream = []
    for f in all_files:
        raw_data_file = os.path.abspath(os.path.join(folder, f))
        print(raw_data_file)
        with open(raw_data_file, 'r', encoding='utf-8') as fin:
            all_samples = [Sample(*(line.split(' '))) for line in fin]

            for s in all_samples:
                stream.append(s)

            all_samples.clear()

    with open(file_path, 'w') as fout:
        for i in stream:
            fout.write(i.tag + ' ' + i.time + ' ' + i.value)

    print('Files merged! Data stored to ' + file_name)
    # ----------------- Info Segment ----------------- #
    if verbose:
        print(folder)
        print(file_name)
        print(file_path)
        print(all_files)


if __name__ == '__main__':
    main()
