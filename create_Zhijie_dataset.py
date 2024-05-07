import os

def get_files_with_prefix_and_suffix(directory, prefix, suffix):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(suffix):
                file_path = os.path.join(root, file)

                file_list.append(os.path.join(prefix, file_path))
    return file_list


# directory_path = '..\\2023_SNS_data/20231211/Zhijie _form'
# file_prefix = ''
# file_suffix = '0PSD'

# result_list = get_files_with_prefix_and_suffix(directory_path, file_prefix, file_suffix)


# print(result_list)
