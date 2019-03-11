from scipy.io import wavfile
import matplotlib.pyplot as plt

import storage
import ui


def save_waveforms_from(file_list):
    number_rows = len(file_list)
    number_cols = 1
    index = 1
    data = f'data{index}'
    for file in file_list:
        fs, data = wavfile.read(file)
        plt.subplot(f'{number_rows}{number_cols}{index}')
        plt.plot(data)
        plt.title(file)
        index += 1
    plt.savefig('waveforms.png')
