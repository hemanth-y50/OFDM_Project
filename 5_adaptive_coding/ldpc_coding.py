import numpy as np

# Example: (7,4) Hamming-like LDPC generator matrix
G = np.array([
    [1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1]
])

def ldpc_encode(bits):
    if len(bits) != 4:
        raise ValueError("Input must be 4 bits for this example.")
    return np.dot(bits, G) % 2

# Example usage
if __name__ == "__main__":
    data = np.array([1, 0, 1, 1])
    encoded = ldpc_encode(data)
    print("Encoded bits:", encoded)
