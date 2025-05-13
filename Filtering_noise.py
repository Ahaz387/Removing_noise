import numpy as np
import matplotlib.pyplot as plt, scipy
from IPython.display import Audio

# Time resolution
dt = 0.001

# Create a time vector from 0 to 1 second with step dt
t = np.arange(0, 1, dt)

# Define the amplitude and two frequencies for the signal
amplitude = 10
frequency_1 = 7
frequency_2 = 8

# Create the signal x(t) as a sum of two sine waves
xt = amplitude * (np.sin(2 * np.pi * frequency_1 * t) + np.sin(2 * np.pi * frequency_2 * t))

# Add Gaussian noise to the signal to simulate a noisy measurement
xt_with_noise = xt + 10 * np.random.randn(len(t))

# Length of the signal
n = len(t)

# Compute the FFT (Fast Fourier Transform) of the noisy signal
fhat = np.fft.fft(xt_with_noise, n)

# Compute the Power Spectral Density (PSD)
PSD = np.conj(fhat) * fhat / n

# Frequency axis for plotting
freq = (1 / (dt * n)) * np.arange(n)

# Define a threshold to filter out low-power frequencies (noise)
threshold = np.max(PSD) * 1 / 2

# Find the indices of frequency components above the threshold
indicies = PSD > threshold

# Zero out the PSD below the threshold to "clean" it
PSD_clean = PSD * indicies

# Apply the filter to the frequency domain signal
fhat = fhat * indicies

# Compute the inverse FFT to get the filtered signal back in time domain
ffilt = np.fft.ifft(fhat)

# Plot the original noisy signal
plt.subplot(1, 2, 1)
plt.title("Noisy vs filtered Signal")
plt.plot(t, xt_with_noise, color = 'g')

# Plot the power spectral density with yellow color
plt.subplot(1, 2, 2)
plt.plot(t, xt)

# Plot the original clean signal x(t) for reference
plt.xlabel("Frequency (Hz)")
plt.legend()
plt.tight_layout()
plt.show()
