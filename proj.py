import wave 
import numpy as np
import matplotlib.pyplot as plt  # Corrected import
from scipy.io.wavfile import write
# Open the WAV file
obj = wave.open("Newrec.wav", "rb")

# Extract audio properties
sample_freq = obj.getframerate()
n_sample = obj.getnframes()
n_channels = obj.getnchannels()
signal_wave = obj.readframes(n_sample)
obj.close()

# Duration in seconds
t_audio = n_sample / sample_freq
print("Audio duration (seconds):", sample_freq)

# Convert buffer to numpy array
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

# Handle stereo by selecting one channel
if n_channels == 2:
    signal_array = signal_array[::2]  # Take only the left channel

# Time array for plotting
time_array = np.linspace(0, t_audio, num=len(signal_array))


n = len(signal_array)
signal_fft = np.fft.fft(signal_array)
PSD = np.imag(signal_fft)*signal_fft/n
freq = (1/(sample_freq*n))*np.arange(n)
threshold = np.max(PSD)*0.4
indicies = PSD > threshold
PSD_clean = PSD * indicies
signal_fft = indicies*PSD_clean
ffit = np.fft.ifft(signal_fft)
print(n)
ffit_int16 = np.int16(ffit/np.max(np.abs(ffit)) * 32767)
# Save filtered audio
write("filtered_output.wav", sample_freq, ffit_int16)
# Plot waveform
plt.subplot(1,2,1)
plt.plot(time_array, ffit)
plt.subplot(1,2,2)
plt.plot(freq, PSD_clean)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Waveform of Audio")
plt.show()  # Required to display the plot
