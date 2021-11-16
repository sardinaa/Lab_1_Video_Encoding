import numpy as np


# https://www.pythonpool.com/run-length-encoding-python/

def run_length_encoding(seq_array):
    compressed_seq = ''
    change = (seq_array[1:] != seq_array[:-1])
    x = np.append(np.where(change), len(seq_array) - 1)
    counter = np.diff(np.append(-1, x))

    for i in range(0, len(counter)):
        compressed_seq = compressed_seq + str(seq_array[x][i]) + str(counter[i])

    return compressed_seq


def run_length_decoding(compressed_seq):
    seq = ''
    for i in range(0, len(compressed_seq)):
        if compressed_seq[i].isalpha():
            for j in range(int(compressed_seq[i + 1])):
                seq += compressed_seq[i]

    return seq
