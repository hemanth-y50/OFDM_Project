# OFDM_Project
- OFDM simulations and documentation for wireless communication systems — includes Python, MATLAB, C, and C++ implementations.
# OFDM Simulation Lab – Day 1

This repository contains annotated simulations and visualizations for Orthogonal Frequency-Division Multiplexing (OFDM), a core modulation technique used in modern wireless communication systems such as LTE, 5G, Wi-Fi, and Bluetooth.

## 📘 Overview

Day 1 focuses on building a minimal OFDM system using Python and visualizing its behavior under an AWGN channel. The simulation includes:
- QAM symbol mapping
- IFFT-based OFDM modulation
- Cyclic Prefix addition
- AWGN channel modeling
- FFT-based demodulation
- Symbol error analysis
- Six key plots saved for documentation

## 🧠 Concepts Covered

- Orthogonality of subcarriers
- FFT/IFFT modulation and demodulation
- Cyclic Prefix and ISI mitigation
- 16-QAM modulation
- AWGN channel effects
- Symbol error visualization

## 📊 Plots Included

All plots are saved in the `plots/` folder:
- `constellation.png`: Transmitted vs received symbols
- `time_domain_before_cp.png`: OFDM symbol before CP
- `time_domain_with_cp.png`: OFDM signal with CP
- `spectrum.png`: Frequency-domain subcarrier spectrum
- `noise.png`: AWGN noise visualization
- `error_magnitude.png`: Symbol error per subcarrier

## 📂 Folder Structure

## 🧭 What’s Next (Day 2 Preview)

- Rayleigh fading channel simulation
- Pilot symbol insertion
- Frequency-domain equalization
- BER vs SNR analysis

## 🛠️ Technologies Used

- Python (NumPy, Matplotlib)
- Jupyter Notebook
- MATLAB, C, and C++ planned for future modules

---

📌 This project is part of a structured learning roadmap for mastering wireless communication systems and preparing for advanced simulation work in SDR, 5G, and embedded DSP environments.
