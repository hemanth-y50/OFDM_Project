import numpy as np

def qpsk_modulate(bits):
    """
    Maps bits to QPSK symbols.
    Input: bits (1D array of 0s and 1s)
    Output: complex QPSK symbols
    """
    symbols = []
    for i in range(0, len(bits), 2):
        b1, b2 = bits[i], bits[i+1]
        real = 1 if b1 == 0 else -1
        imag = 1 if b2 == 0 else -1
        symbols.append((real + 1j * imag) / np.sqrt(2))
    return np.array(symbols)

def ofdm_modulate(symbols, num_subcarriers, cp_len):
    """
    Applies IFFT and adds cyclic prefix.
    Input: symbols (1D array), num_subcarriers, cp_len
    Output: time-domain OFDM signal
    """
    # Reshape symbols into OFDM blocks
    num_blocks = len(symbols) // num_subcarriers
    symbols = symbols[:num_blocks * num_subcarriers].reshape((num_blocks, num_subcarriers))

    time_domain = []
    for block in symbols:
        ifft_block = np.fft.ifft(block)
        cp = ifft_block[-cp_len:]
        ofdm_block = np.concatenate([cp, ifft_block])
        time_domain.append(ofdm_block)
    
    return np.array(time_domain)

def mimo_ofdm_transmit(bits_tx1, bits_tx2, num_subcarriers=64, cp_len=16):
    """
    Generates OFDM signals for 2 transmit antennas.
    Input: bitstreams for tx1 and tx2
    Output: time-domain OFDM signals for tx1 and tx2
    """
    symbols_tx1 = qpsk_modulate(bits_tx1)
    symbols_tx2 = qpsk_modulate(bits_tx2)

    ofdm_tx1 = ofdm_modulate(symbols_tx1, num_subcarriers, cp_len)
    ofdm_tx2 = ofdm_modulate(symbols_tx2, num_subcarriers, cp_len)

    return ofdm_tx1, ofdm_tx2
