import numpy as np

def transmit_through_mimo_channel(ofdm_tx1, ofdm_tx2, H, snr_db):
    """
    Simulates transmission of OFDM signals through a 2x2 MIMO channel with AWGN.

    Parameters:
    - ofdm_tx1, ofdm_tx2: OFDM signals from Tx1 and Tx2 (shape: [num_blocks, block_len])
    - H: Channel matrix per subcarrier (shape: [num_subcarriers, 2, 2])
    - snr_db: Signal-to-noise ratio in dB

    Returns:
    - received_signal: shape [num_blocks, block_len, 2] — signals at Rx1 and Rx2
    """
    num_blocks, block_len = ofdm_tx1.shape
    num_subcarriers = block_len - (block_len // 5)  # assuming CP is ~20%
    received_signal = np.zeros((num_blocks, block_len, 2), dtype=complex)

    for blk in range(num_blocks):
        rx1 = np.zeros(block_len, dtype=complex)
        rx2 = np.zeros(block_len, dtype=complex)

        # Remove CP before channel
        tx1_block = ofdm_tx1[blk][block_len // 5:]
        tx2_block = ofdm_tx2[blk][block_len // 5:]

        # Apply channel per subcarrier
        tx1_freq = np.fft.fft(tx1_block)
        tx2_freq = np.fft.fft(tx2_block)

        rx1_freq = np.zeros(num_subcarriers, dtype=complex)
        rx2_freq = np.zeros(num_subcarriers, dtype=complex)

        for sc in range(num_subcarriers):
            h = H[sc]  # shape (2, 2)
            tx_vec = np.array([tx1_freq[sc], tx2_freq[sc]])
            rx_vec = h @ tx_vec
            rx1_freq[sc], rx2_freq[sc] = rx_vec

        # IFFT to get time-domain signal
        rx1_block = np.fft.ifft(rx1_freq)
        rx2_block = np.fft.ifft(rx2_freq)

        # Add CP
        cp_len = block_len - num_subcarriers
        rx1_cp = rx1_block[-cp_len:]
        rx2_cp = rx2_block[-cp_len:]
        rx1_full = np.concatenate([rx1_cp, rx1_block])
        rx2_full = np.concatenate([rx2_cp, rx2_block])

        # Add AWGN
        snr_linear = 10 ** (snr_db / 10)
        noise_power = np.mean(np.abs(rx1_full)**2) / snr_linear
        noise = np.sqrt(noise_power / 2) * (np.random.randn(*rx1_full.shape) + 1j * np.random.randn(*rx1_full.shape))
        rx1 += rx1_full + noise

        noise = np.sqrt(noise_power / 2) * (np.random.randn(*rx2_full.shape) + 1j * np.random.randn(*rx2_full.shape))
        rx2 += rx2_full + noise

        received_signal[blk, :, 0] = rx1
        received_signal[blk, :, 1] = rx2

    return received_signal
