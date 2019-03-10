from scipy.io import wavfile
import matplotlib.pyplot as plt


def detect_broken_record(files_list):
    pass


def save_waveforms_from(files_list):
    pass
    

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