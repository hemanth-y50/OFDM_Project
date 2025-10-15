import numpy as np

def alamouti_encode(symbols):
    """
    Encodes a stream of complex symbols using the Alamouti 2x1 STBC.

    Input:
    - symbols: 1D array of complex symbols (length must be even)

    Output:
    - tx1: symbols for antenna 1
    - tx2: symbols for antenna 2
    """
    assert len(symbols) % 2 == 0, "Symbol length must be even for Alamouti encoding"

    tx1 = []
    tx2 = []

    for i in range(0, len(symbols), 2):
        s1 = symbols[i]
        s2 = symbols[i+1]

        # Time slot 1
        tx1.append(s1)
        tx2.append(s2)

        # Time slot 2
        tx1.append(-np.conj(s2))
        tx2.append(np.conj(s1))

    return np.array(tx1), np.array(tx2)

def alamouti_decode(rx1, rx2, H1, H2):
    """
    Decodes received signals using Alamouti 2x1 STBC.

    Inputs:
    - rx1, rx2: received signals at time t and t+1
    - H1, H2: channel gains from Tx1 and Tx2 to Rx

    Output:
    - s1_hat, s2_hat: estimated transmitted symbols
    """
    H1_conj = np.conj(H1)
    H2_conj = np.conj(H2)

    s1_hat = H1_conj * rx1 + H2 * np.conj(rx2)
    s2_hat = H2_conj * rx1 - H1 * np.conj(rx2)

    norm = np.abs(H1)**2 + np.abs(H2)**2
    return s1_hat / norm, s2_hat / norm
