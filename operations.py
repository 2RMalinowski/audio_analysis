from scipy.io import wavfile
import matplotlib.pyplot as plt

import ui


def detect_broken_record_from(file_list):
    # variable for exemplary condition
    difference = abs(previous_sample_value - next_sample_value)
    for file in file_list:
        fs, data = wavfile.read(file)
        if round(difference) == previous_sample_value:  # exemplary condition
            ui.display_message(
                f'{file} invalid {index_of_first_dropped_sample}')
        else:
            ui.display_message(f'{file} valid')


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
