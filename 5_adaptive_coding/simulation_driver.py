import numpy as np
import matplotlib.pyplot as plt
from adaptive_modulation import modulate, demodulate
from ldpc_coding import ldpc_encode
from link_adaptation import get_mcs

# SNR range in dB
snr_range = np.arange(0, 25, 5)
ber_results = []

for snr_db in snr_range:
    print(f"Simulating for SNR = {snr_db} dB")
    
    # Get modulation and coding scheme
    mcs = get_mcs(snr_db)
    
    # Generate random bits (4 bits for LDPC (7,4) block)
    bits = np.random.randint(0, 2, 4)
    
    # Encode using LDPC
    coded_bits = ldpc_encode(bits)
    
    # Modulate
    symbols = modulate(coded_bits, mcs['mod'])
    
    # Simulate AWGN channel
    noise_power = 10 ** (-snr_db / 10)
    noise = np.sqrt(noise_power / 2) * (np.random.randn(len(symbols)) + 1j * np.random.randn(len(symbols)))
    received = symbols + noise
    
    # Demodulate
    decoded_bits = demodulate(received, mcs['mod'])
    
    # Truncate to original bit length
    decoded_bits = decoded_bits[:len(bits)]
    
    # Calculate BER
    ber = np.mean(decoded_bits != bits)
    ber_results.append(ber)

# Print results
print("BER vs SNR:", ber_results)

# Plot BER vs SNR
plt.figure(figsize=(8, 5))
plt.plot(snr_range, ber_results, marker='o', linestyle='-', color='blue')
plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("BER vs SNR for Adaptive OFDM with LDPC")
plt.grid(True)
plt.savefig("ber_vs_snr.png")
plt.show()
