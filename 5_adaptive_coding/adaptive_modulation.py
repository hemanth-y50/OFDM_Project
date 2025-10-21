import numpy as np

def select_modulation(snr_db):
    if snr_db < 5:
        return 'BPSK'
    elif snr_db < 10:
        return 'QPSK'
    elif snr_db < 20:
        return '16QAM'
    else:
        return '64QAM'

def modulate(bits, scheme):
    import numpy as np

    if scheme == 'BPSK':
        return 2 * bits - 1

    elif scheme == 'QPSK':
        if len(bits) % 2 != 0:
            bits = np.append(bits, 0)
        return (1 - 2 * bits[::2]) + 1j * (1 - 2 * bits[1::2])

    elif scheme == '16QAM':
        if len(bits) % 4 != 0:
            bits = np.append(bits, [0] * (4 - len(bits) % 4))
        symbols = []
        for i in range(0, len(bits), 4):
            real = (1 - 2 * bits[i]) * (2 - bits[i+2])
            imag = (1 - 2 * bits[i+1]) * (2 - bits[i+3])
            symbols.append(real + 1j * imag)
        return np.array(symbols)

    elif scheme == '64QAM':
        if len(bits) % 6 != 0:
            bits = np.append(bits, [0] * (6 - len(bits) % 6))
        symbols = []
        for i in range(0, len(bits), 6):
            real_level = 4 * (1 - 2 * bits[i]) + 2 * (1 - 2 * bits[i+2]) + (1 - 2 * bits[i+4])
            imag_level = 4 * (1 - 2 * bits[i+1]) + 2 * (1 - 2 * bits[i+3]) + (1 - 2 * bits[i+5])
            symbols.append(real_level + 1j * imag_level)
        return np.array(symbols)

def demodulate(received, scheme):
    import numpy as np

    if scheme == 'BPSK':
        return (received.real > 0).astype(int)

    elif scheme == 'QPSK':
        bits = []
        for r in received:
            bits.append(int(r.real < 0))
            bits.append(int(r.imag < 0))
        return np.array(bits)

    elif scheme == '16QAM':
        bits = []
        for r in received:
            real = r.real
            imag = r.imag
            bits.append(int(real < 0))
            bits.append(int(imag < 0))
            bits.append(int(abs(real) < 2))
            bits.append(int(abs(imag) < 2))
        return np.array(bits)

    elif scheme == '64QAM':
        bits = []
        for r in received:
            real = r.real
            imag = r.imag
            bits.append(int(real < 0))
            bits.append(int(imag < 0))
            bits.append(int(abs(real) < 4))
            bits.append(int(abs(imag) < 4))
            bits.append(int(abs(real) % 4 < 2))
            bits.append(int(abs(imag) % 4 < 2))
        return np.array(bits)



