import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, iirnotch, find_peaks

# --- Generate sample ECG-like signal ---
fs = 128
t = np.linspace(0, 10, fs*10)
signal = 1000*np.sin(2*np.pi*1.2*t) + 200*np.random.randn(len(t))

# --- Filtering ---
def bandpass_filter(sig, lowcut=0.5, highcut=35, fs=128):
    nyq = 0.5 * fs
    b, a = butter(2, [lowcut/nyq, highcut/nyq], btype='band')
    return filtfilt(b, a, sig)

def notch_filter(sig, freq=50, fs=128):
    b, a = iirnotch(freq/(0.5*fs), 30)
    return filtfilt(b, a, sig)

filtered = bandpass_filter(signal)
filtered = notch_filter(filtered)

# --- Peak Detection ---
peaks, _ = find_peaks(filtered, distance=fs*0.5)

# --- Plot ---
plt.plot(filtered)
plt.scatter(peaks, filtered[peaks], color='red')
plt.title("ECG Signal Processing Demo")
plt.show()
