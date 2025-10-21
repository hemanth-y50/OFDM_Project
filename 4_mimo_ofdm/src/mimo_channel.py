import numpy as np

def generate_rayleigh_mimo_channel(num_subcarriers, num_tx=2, num_rx=2, doppler_freq=0, sampling_rate=1e6):
    """
    Generates a Rayleigh fading MIMO channel matrix H for each subcarrier.

    Parameters:
    - num_subcarriers: Number of OFDM subcarriers
    - num_tx: Number of transmit antennas
    - num_rx: Number of receive antennas
    - doppler_freq: Doppler frequency in Hz
    - sampling_rate: Sampling rate in Hz

    Returns:
    - H: ndarray of shape (num_subcarriers, num_rx, num_tx)
    """
    H = np.zeros((num_subcarriers, num_rx, num_tx), dtype=complex)

    for sc in range(num_subcarriers):
        time = sc / sampling_rate
        for rx in range(num_rx):
            for tx in range(num_tx):
                # Rayleigh fading: complex Gaussian
                real = np.random.normal(0, 1)
                imag = np.random.normal(0, 1)
                fading = (real + 1j * imag) / np.sqrt(2)

                # Doppler phase rotation (optional)
                if doppler_freq > 0:
                    doppler_phase = np.exp(1j * 2 * np.pi * doppler_freq * time)
                    fading *= doppler_phase

                H[sc, rx, tx] = fading

    return H
