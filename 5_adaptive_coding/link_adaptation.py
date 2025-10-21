def get_mcs(snr_db):
    if snr_db < 5:
        return {'mod': 'BPSK', 'code_rate': 0.5}
    elif snr_db < 10:
        return {'mod': 'QPSK', 'code_rate': 0.5}
    elif snr_db < 20:
        return {'mod': '16QAM', 'code_rate': 0.75}
    else:
        return {'mod': '64QAM', 'code_rate': 0.83}
