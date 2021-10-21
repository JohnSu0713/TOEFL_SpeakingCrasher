import threading
import time
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# 子執行緒的工作函數
def recorder(t, topic):
    # Sampling frequency
    freq = 44100
    # Recording duration
    duration = t
    # Start recorder with the given values 
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq), 
                    samplerate=freq, channels=1)
    # Record audio for the given number of seconds
    sd.wait()
    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    write(f"./recording/{topic}.wav", freq, recording)
    return