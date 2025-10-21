# 📡 OFDM_Project

OFDM simulations and documentation for wireless communication systems using Python implementations. This project is part of a structured learning roadmap for mastering wireless communication systems and preparing for advanced simulation work in SDR, 5G, and embedded DSP environments.

---

## 📘 Overview

This repository contains annotated simulations and visualizations for **Orthogonal Frequency-Division Multiplexing (OFDM)**, a core modulation technique used in modern wireless communication systems such as LTE, 5G, Wi-Fi, and Bluetooth. Each day explores a new concept, building toward a full adaptive OFDM receiver chain.

---

## 🧪 Simulation Modules

### 🔹1: Minimal OFDM under AWGN
Folder: `1_OFDM_basics/`

- QAM symbol mapping
- IFFT-based OFDM modulation
- Cyclic Prefix addition
- AWGN channel modeling
- FFT-based demodulation
- Symbol error analysis

📊 Plots saved in `plots_1/`:
- `constellation.png`
- `time_domain_before_cp.png`
- `time_domain_with_cp.png`
- `spectrum.png`
- `noise.png`
- `error_magnitude.png`

---

### 🔹2: Channel Estimation, Equalization & BER Analysis
Folder: `2_channel_estimation/`

- Rayleigh fading channel simulation
- Comb-type pilot insertion
- Linear vs spline interpolation
- LS and MMSE channel estimation
- ZF vs MMSE equalization
- BER vs SNR analysis

📊 Plots saved in `plots_2/`:
- `Block1_channel_magnitude.png`
- `Block1_rayleigh_pdf.png`
- `Block2_channel_interpolation.png`
- `Block3_ls_mmse_comparison.png`
- `Block4_constellation_zf.png`
- `Block4_constellation_mmse.png`
- `Block5_ber_vs_snr.png`

---

### 🔹3: Doppler-Aware OFDM Receiver
Folder: `3_doppler_mobility/`

- Rayleigh fading simulation for multiple Doppler frequencies
- Doppler spectrum analysis via FFT
- LMS-based channel tracking and MSE plots
- Constellation recovery under mobility
- BER vs Doppler sweep (semilog plot)

---

### 🔹4: MIMO OFDM with Diversity
Folder: `day4_mimo_ofdm/`

- 2×2 MIMO OFDM system
- Alamouti STBC and spatial multiplexing
- QPSK modulation
- BER vs SNR and constellation recovery

---

### 🔹5: Adaptive Modulation & LDPC Coding
Folder: `5_adaptive_coding/`

- Adaptive modulation: BPSK, QPSK, 16QAM, 64QAM
- Custom LDPC encoder (Hamming-like)
- AWGN channel simulation
- Demodulation and BER computation

📊 Output saved in `results/`:
- `ber_vs_snr.png`

---

## 🧠 Concepts Covered

- Subcarrier orthogonality
- FFT/IFFT modulation and demodulation
- Cyclic Prefix and ISI mitigation
- Rayleigh fading and Doppler effects
- Channel estimation and equalization
- MIMO diversity and spatial multiplexing
- Adaptive modulation and coding
- BER and performance analysis

---

## 🛠 Technologies Used

- Python (NumPy, Matplotlib)
- Jupyter Notebook
- git for version control
- MATLAB, C, and C++ (planned to be added soon)

---

## 🎓 Research Potential

This simulation suite supports:
- SDR prototyping and embedded DSP
- Disaster-resilient IoT and rural wireless systems
- Academic benchmarking for IEEE/Springer publications

📄 Suggested Paper Title:
**“Adaptive Modulation and Channel Coding for OFDM Systems under Mobility and Fading”**

---

## 📬 Contact

Developed by [Hemanth Kumar Yenuganti](https://github.com/hemanth-y50)  
For collaboration, benchmarking, or publication support, feel free to reach out via GitHub.
