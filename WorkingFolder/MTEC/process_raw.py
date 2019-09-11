from empatica_data_extraction import *


def main():
    """
    Program extracts data streams from a merged data file and saves them to separate files
    """
    # set info display
    set_verbose = False

    # ----------------- DATA EXTRACTION ----------------- #
    label = 'PRE-PROCESSING APP'
    print_header(program_label=label)

    # Get user input
    folder = get_folder_from_user(default_folder_name='MergeRepository')
    if not folder:
        print("We can't search file in this location.")
        return
    else:
        print(folder)

    # Get user input: subject name
    subject = input('Please enter subject initials.')

    # # create merge file
    # file_name = 'merged_raw_data_' + subject + '.txt'
    # file_path = os.path.abspath(os.path.join(folder, file_name))
    # if os.path.isfile(file_path):
    #     # clear and then write
    #     print('file found')
    #     file = open(file_path, 'r')
    #     file.truncate()
    #     print('file cleared')
    #     file.close()
    # else:
    #     file = open(file_path, 'r')
    #     print('new file created')
    #     file.close()

    #  Get data folder
    search_text = 'merged_raw_data_' + subject
    stream_data = extract_all(folder=folder, file_label=search_text, verbose=set_verbose)
    # write dictionary to file
    target_folder = get_folder_from_user(default_folder_name='ProcessingRepository')
    # ----------------- BLOOD VOLUME PRESSURE ----------------- #
    write_to_text_file(file_name='_bvp_data_', file_index=subject, folder=target_folder,
                       data_list=stream_data['E4_Bvp_data'])
    write_to_text_file(file_name='_bvp_time_', file_index=subject, folder=target_folder,
                       data_list=stream_data['E4_Bvp_time'])
    # ----------------- GALVANIC SKIN RESPONSE ----------------- #
    write_to_text_file(file_name='_gsr_data_', file_index=subject, folder=target_folder,
                       data_list=stream_data['E4_Gsr_data'])
    write_to_text_file(file_name='_gsr_time_', file_index=subject, folder=target_folder,
                       data_list=stream_data['E4_Gsr_time'])
    # ----------------- TEMPERATURE ----------------- #
    write_to_text_file(file_name='_temp_data_', file_index=subject, folder=target_folder,
                       data_list=stream_data['E4_Temperature_data'])
    write_to_text_file(file_name='_temp_time_', file_index=subject, folder=target_folder,
                       data_list=stream_data['E4_Temperature_time'])
    # ----------------- TAGS ----------------- #
    write_to_text_file(file_name='_tag_data_', file_index=subject, folder=target_folder,
                       data_list=stream_data['E4_Tag_data'])
    write_to_text_file(file_name='_tag_time_', file_index=subject, folder=target_folder,
                       data_list=stream_data['E4_Tag_time'])

    print('Files created! Program closed.')


if __name__ == '__main__':
    main()
