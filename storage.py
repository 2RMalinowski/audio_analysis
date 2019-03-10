from scipy.io import wavfile
import matplotlib.pyplot as plt
import os


def open_wav_files_from(path):
    file_type_list = []
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith('.wav'):
            file_type_list.append(file)
    return file_type_list


print(open_wav_files_from('/home/robb/Code/audio_analysis/'))


(fs, x) = wavfile.read('nan-ai-file-1.wav')
(fs, y) = wavfile.read('nan-ai-file-2.wav')
(fs, z) = wavfile.read('nan-ai-file-3.wav')

plt.subplot(311)
plt.plot(x)
plt.title('nan-ai-file-1.wav')
plt.subplot(312)
plt.plot(y)
plt.title('nan-ai-file-2.wav')
plt.subplot(313)
plt.plot(z)
plt.title('nan-ai-file-3.wav')
plt.savefig('waveforms.png')
