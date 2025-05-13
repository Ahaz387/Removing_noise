🎧 Audio Signal Processing with FFT in Python

- This repository contains two Python scripts demonstrating the use of Fast Fourier Transform (FFT) for analyzing and filtering signals. It covers both real-world audio data and synthetic signals, offering practical insight into frequency-domain filtering.

📁 Contents

- filter_real_audio.py

- Loads a WAV file (Newrec.wav)

- Converts stereo to mono if necessary

- Computes the Power Spectral Density (PSD) via FFT

- Applies a threshold-based frequency filter

- Reconstructs and saves the cleaned audio signal (filtered_output.wav)

- Plots both the time-domain waveform and frequency-domain spectrum

- fft_filter_synthetic_signal.py

- Creates a synthetic signal using two sine waves and Gaussian noise

- Applies FFT to analyze frequency components

- Filters out noise by thresholding PSD

- Reconstructs and visualizes the cleaned signal

- Compares the noisy and original signals visually

📊 Features

- FFT-based frequency analysis and filtering

- Visualization of signals in both time and frequency domains

- Practical examples using both:

- Real audio recordings (.wav)

- Simulated noisy signals
