from scipy.io import wavfile
import matplotlib.pyplot as plt

import storage


def detect_broken_record_from(file_list):
    pass


def save_waveforms_from(file_list):
    n = 1
    data = f'data{n}'
    for file in file_list:
        fs, data = wavfile.read(file)
        plt.subplot(f'{len(file_list)}1{n}')
        plt.plot(data)
        plt.title(file)
        n += 1
    plt.savefig('waveforms.png')
