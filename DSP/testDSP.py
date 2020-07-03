import os
import librosa
import IPython.display as ipd 
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile #for audio processing
import warnings
warnings.filterwarnings("ignore")
audio_path = './audio/'
samples, sample_rate = librosa.load(audio_path+'yes/test_audio.wav')
# print("sample rate:",sample_rate,"samples:", len(samples))
# fig = plt.figure(figsize=(14, 8))
# plt.title('Raw wave ')
# plt.xlabel('time')
# plt.ylabel('Amplitude')
# plt.plot(np.linspace(0, len(samples)/sample_rate, len(samples)), samples)
# plt.show()
# Sampling rate
ipd.Audio(samples, rate=sample_rate)
print(sample_rate)
# Resampling
samples = librosa.resample(samples, sample_rate, 8000)
ipd.Audio(samples, rate=8000)


labels=os.listdir(audio_path)

#find count of each label and plot bar graph
no_of_recordings=[]
for label in labels:
    waves = [f for f in os.listdir(audio_path + label) if f.endswith('.wav')]
    no_of_recordings.append(len(waves))
    
#plot
plt.figure(figsize=(30,5))
index = np.arange(len(labels))
plt.bar(index, no_of_recordings)
plt.xlabel('Commands', fontsize=12)
plt.ylabel('No of recordings', fontsize=12)
plt.xticks(index, labels, fontsize=15, rotation=60)
plt.title('No. of recordings for each command')
plt.show()

labels=["yes", "no", "up", "down", "left", "right", "on", "off", "stop", "go"]