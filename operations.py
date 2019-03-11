from scipy.io import wavfile
import matplotlib.pyplot as plt

import storage


# def detect_broken_record_from(file_list):
#     for file in file_list:

#     pass


def save_waveforms_from(file_list):
    nrows = len(file_list)
    ncols = 1
    index = 1
    data = f'data{index}'
    for file in file_list:
        fs, data = wavfile.read(file)
        plt.subplot(f'{nrows}{ncols}{index}')
        plt.plot(data)
        plt.title(file)
        index += 1
    plt.savefig('waveforms.png')
