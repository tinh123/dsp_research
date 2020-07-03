
import os
import librosa   #for audio processing
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile #for audio processing
import warnings
from ssp import *
warnings.filterwarnings("ignore")

source_audio = "audio/yes/227.wav"
filter_audio = "audio/yes/test_audio.wav"

# Windown 
# Load and process
pcm = PulseCodeModulation()
a = pcm.WavSource(source_audio)
# Default to 8k
fs = 512
fp = 256 #Frame period
if pcm.rate == 16000:
    fs = 1024
    fp = 128
if pcm.rate == 22050:
    fs = 2048
    fp = 256
elif pcm.rate == 96000:
    fs = 8192
    fp = 160
w = gaussian(fs)
f = Frame(a, size=fs, period=fp)
f = ZeroMean(f)
wf = Window(f, w)
print("num of windows",len(wf))
samples, sampling_rate = librosa.load(source_audio) # return list of samples and sampling rate
# samples, sample_rate = librosa.load(source_audio)
ipd.Audio(samples, rate=sample_rate)
# print("Samples rate:",sample_rate, "Samples: ", samples)