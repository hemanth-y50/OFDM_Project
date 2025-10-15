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



# Day 2: Channel Estimation, Equalization & BER Analysis in OFDM
This notebook (day2_ofdm_channel_estimation_equalization.ipynb) simulates a full OFDM receiver chain under Rayleigh fading and AWGN. It demonstrates key recovery techniques and performance metrics using:
## Simulation Blocks
- Rayleigh Fading Channel
- Visualizes channel magnitude and envelope distribution
- Highlights multipath fading effects
- Pilot Design & Interpolation
- Inserts comb-type pilots
- Compares linear vs spline interpolation for channel estimation
- Channel Estimation Techniques
- Implements LS and MMSE estimation
- Compares accuracy across pilot samples
- Equalization Methods
- Applies ZF and MMSE equalization
- Visualizes constellation recovery under fading
- BER Analysis
- Sweeps SNR from 0–20 dB
- Plots BER curves for ZF vs MMSE equalization
  ## Saved Plots
All plots are stored in plots_day_2/ and include:
- Block1_channel_magnitude.png
- Block1_rayleigh_pdf.png
- Block2_channel_interpolation.png
- Block3_ls_mmse_comparison.png
- Block4_constellation_zf.png
- Block4_constellation_mmse.png
- Block5_ber_vs_snr.png
  ## Skills Demonstrated
- Channel modeling and fading statistics
- Pilot-aided estimation and interpolation
- LS vs MMSE trade-offs
- ZF vs MMSE equalization under noise
- BER performance analysis


## 📡 Day 3: Doppler-Aware OFDM Receiver

Folder: `day3_doppler_mobility/`

Includes:
- Rayleigh fading simulation for multiple Doppler frequencies
- Doppler spectrum analysis via FFT
- LMS-based channel tracking and MSE plots
- Constellation recovery under mobility
- BER vs Doppler sweep (semilog plot)

## 📅 Day 4: MIMO OFDM Simulation — Equalization & Diversity

This module simulates a 2×2 MIMO OFDM system with QPSK modulation over Rayleigh fading channels. It benchmarks linear equalization techniques and space-time coding schemes using BER and constellation analysis.

### 🔧 Modules Used
- `mimo_channel.py`: Rayleigh channel generation
- `mimo_modulation.py`: QPSK + OFDM modulation
- `mimo_transmission.py`: Channel + noise simulation
- `mimo_equalization.py`: ZF and MMSE equalizers
- `alamouti_encoder.py`: Alamouti STBC encoder/decoder
- `ber_analysis.py`: BER simulation for equalization and diversity

### 📊 Results

#### 1. BER vs SNR: ZF vs MMSE Equalization
Compares Zero Forcing and MMSE equalizers under identical channel conditions.


#### 2. Recovered QPSK Constellation at 10 dB SNR
Visualizes symbol recovery using ZF equalization.


#### 3. BER vs SNR: Alamouti STBC vs Spatial Multiplexing
Highlights diversity gain vs throughput tradeoff.


### 🎓 Author
**Hemanth Kumar Yenuganti**  
B.Tech ECE, RGUKT Nuzvid  
GitHub: [hemanth-y50](https://github.com/hemanth-y50)










