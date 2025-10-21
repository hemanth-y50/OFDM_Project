import numpy as np

def zero_forcing_equalizer(H, y):
    """
    Applies Zero-Forcing equalization.
    
    Parameters:
    - H: Channel matrix (shape: [2, 2])
    - y: Received signal vector (shape: [2,])

    Returns:
    - x_hat: Estimated transmitted symbols (shape: [2,])
    """
    H_inv = np.linalg.pinv(H)
    x_hat = H_inv @ y
    return x_hat

def mmse_equalizer(H, y, noise_var):
    """
    Applies MMSE equalization.
    
    Parameters:
    - H: Channel matrix (shape: [2, 2])
    - y: Received signal vector (shape: [2,])
    - noise_var: Noise variance

    Returns:
    - x_hat: Estimated transmitted symbols (shape: [2,])
    """
    num_tx = H.shape[1]
    I = np.eye(num_tx)
    H_H = H.conj().T
    W_mmse = np.linalg.inv(H_H @ H + noise_var * I) @ H_H
    x_hat = W_mmse @ y
    return x_hat
