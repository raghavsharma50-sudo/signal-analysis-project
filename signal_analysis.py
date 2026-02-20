import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000        # sampling frequency (Hz)
t = np.linspace(0, 1, fs)

# Signal components
dc = 0.5
f1 = 10
f2 = 20
f3 = 30

# Generate signal with harmonics
signal = dc + np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t) + 0.2*np.sin(2*np.pi*f3*t)

# FFT analysis
fft = np.fft.fft(signal)
freq = np.fft.fftfreq(len(signal), 1/fs)

# Plot time-domain signal
plt.figure()
plt.plot(t, signal)
plt.title("Time Domain Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot frequency spectrum
plt.figure()
plt.plot(freq[:fs//2], np.abs(fft[:fs//2]))
plt.title("FFT Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.show()
