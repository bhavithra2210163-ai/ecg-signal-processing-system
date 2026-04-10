import matplotlib.pyplot as plt

def plot_signal(signal, peaks=None):
    plt.plot(signal)
    if peaks:
        plt.scatter(peaks, [signal[i] for i in peaks], color='red')
    plt.title("ECG Signal")
    plt.show()
