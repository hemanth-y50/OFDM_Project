import numpy as np
from src.mimo_channel import generate_rayleigh_mimo_channel
from src.mimo_modulator import mimo_ofdm_transmit
from src.mimo_transmission import transmit_through_mimo_channel
from src.mimo_equalization import zero_forcing_equalizer, mmse_equalizer

def qpsk_demodulate(symbols):
    bits = []
    for s in symbols:
        bits.append(0 if s.real >= 0 else 1)
        bits.append(0 if s.imag >= 0 else 1)
    return np.array(bits)

def compute_ber(original_bits, recovered_symbols):
    recovered_bits = qpsk_demodulate(recovered_symbols)
    return np.mean(original_bits != recovered_bits[:len(original_bits)])

def ber_vs_snr(num_subcarriers=64, cp_len=16, snr_range=range(0, 21, 2), scheme='zf'):
    ber_list = []

    for snr_db in snr_range:
        bits_tx1 = np.random.randint(0, 2, 128)
        bits_tx2 = np.random.randint(0, 2, 128)
        tx1_signal, tx2_signal = mimo_ofdm_transmit(bits_tx1, bits_tx2, num_subcarriers, cp_len)

        H = generate_rayleigh_mimo_channel(num_subcarriers)
        received = transmit_through_mimo_channel(tx1_signal, tx2_signal, H, snr_db)

        recovered_symbols = []
        for blk in range(received.shape[0]):
            for sc in range(num_subcarriers):
                y = np.array([received[blk, cp_len + sc, 0], received[blk, cp_len + sc, 1]])
                h = H[sc]
                if scheme == 'zf':
                    x_hat = zero_forcing_equalizer(h, y)
                else:
                    noise_var = 10 ** (-snr_db / 10)
                    x_hat = mmse_equalizer(h, y, noise_var)
                recovered_symbols.extend(x_hat)

        ber = compute_ber(bits_tx1, recovered_symbols[::2])
        ber_list.append(ber)

    return snr_range, ber_list
import numpy as np
from src.mimo_channel import generate_rayleigh_mimo_channel
from src.mimo_modulator import mimo_ofdm_transmit
from src.mimo_transmission import transmit_through_mimo_channel
from src.mimo_equalization import zero_forcing_equalizer, mmse_equalizer

def qpsk_demodulate(symbols):
    bits = []
    for s in symbols:
        bits.append(0 if s.real >= 0 else 1)
        bits.append(0 if s.imag >= 0 else 1)
    return np.array(bits)

def compute_ber(original_bits, recovered_symbols):
    recovered_bits = qpsk_demodulate(recovered_symbols)
    return np.mean(original_bits != recovered_bits[:len(original_bits)])

def ber_vs_snr(num_subcarriers=64, cp_len=16, snr_range=range(0, 21, 2), scheme='zf'):
    ber_list = []

    for snr_db in snr_range:
        bits_tx1 = np.random.randint(0, 2, 128)
        bits_tx2 = np.random.randint(0, 2, 128)
        tx1_signal, tx2_signal = mimo_ofdm_transmit(bits_tx1, bits_tx2, num_subcarriers, cp_len)

        H = generate_rayleigh_mimo_channel(num_subcarriers)
        received = transmit_through_mimo_channel(tx1_signal, tx2_signal, H, snr_db)

        recovered_symbols = []
        for blk in range(received.shape[0]):
            for sc in range(num_subcarriers):
                y = np.array([received[blk, cp_len + sc, 0], received[blk, cp_len + sc, 1]])
                h = H[sc]
                if scheme == 'zf':
                    x_hat = zero_forcing_equalizer(h, y)
                else:
                    noise_var = 10 ** (-snr_db / 10)
                    x_hat = mmse_equalizer(h, y, noise_var)
                recovered_symbols.extend(x_hat)

        ber = compute_ber(bits_tx1, recovered_symbols[::2])
        ber_list.append(ber)

    return snr_range, ber_list
def ber_vs_snr_alamouti(num_symbols=128, snr_range=range(0, 21, 2)):
    from src.alamouti_encoder import alamouti_encode, alamouti_decode

    def qpsk_modulate(bits):
        symbols = []
        for i in range(0, len(bits), 2):
            b1, b2 = bits[i], bits[i+1]
            s = (1 - 2*b1) + 1j*(1 - 2*b2)
            symbols.append(s / np.sqrt(2))
        return np.array(symbols)

    def qpsk_demodulate(symbols):
        bits = []
        for s in symbols:
            bits.append(0 if s.real >= 0 else 1)
            bits.append(0 if s.imag >= 0 else 1)
        return np.array(bits)

    ber_list = []

    for snr_db in snr_range:
        bits = np.random.randint(0, 2, num_symbols)
        symbols = qpsk_modulate(bits)
        tx1, tx2 = alamouti_encode(symbols)

        # Rayleigh channel
        H1 = (np.random.randn(len(tx1)) + 1j*np.random.randn(len(tx1))) / np.sqrt(2)
        H2 = (np.random.randn(len(tx2)) + 1j*np.random.randn(len(tx2))) / np.sqrt(2)

        # Noise
        snr_linear = 10 ** (snr_db / 10)
        noise_power = 1 / snr_linear
        noise = np.sqrt(noise_power/2) * (np.random.randn(len(tx1)) + 1j*np.random.randn(len(tx1)))

        # Received signals
        rx1 = H1 * tx1 + H2 * tx2 + noise
        rx2 = -np.conj(H1) * tx2 + np.conj(H2) * tx1 + noise

        # Decode
        s1_hat, s2_hat = alamouti_decode(rx1, rx2, H1, H2)
        recovered = np.concatenate([s1_hat, s2_hat])
        recovered_bits = qpsk_demodulate(recovered)

        ber = np.mean(bits != recovered_bits[:len(bits)])
        ber_list.append(ber)

    return snr_range, ber_list