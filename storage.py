import os


def open_wav_files_from(path='/home/robb/Code/audio_analysis/'):
    wav_file_list = []
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith('.wav'):
            wav_file_list.append(file)
    return wav_file_list
