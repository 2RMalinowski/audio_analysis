import os


def open_files_from(path, file_type):
    file_type_list = []
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(file_type):
            file_type_list.append(file)
    return file_type_list
