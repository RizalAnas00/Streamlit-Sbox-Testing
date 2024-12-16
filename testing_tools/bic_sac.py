import numpy as np

def calculate_bic_sac(sbox):
   return calculate_bic_sac_value(sbox), calculate_bic_sac_matrix(sbox)

def calculate_bic_sac_value(sbox):
    n = len(sbox)  # Jumlah input dalam S-Box
    bit_length = 8  # Panjang bit output
    total_pairs = 0
    total_independence = 0

    # Loop untuk pasangan bit output yang akan dibandingkan
    for i in range(bit_length):
        for j in range(i + 1, bit_length):
            independence_sum = 0
            for x in range(n):
                for bit_to_flip in range(bit_length):  # Flip setiap bit input
                    flipped_x = x ^ (1 << bit_to_flip)  # Input flipped
                    y1 = sbox[x]  # Output untuk input asli
                    y2 = sbox[flipped_x]  # Output untuk input flipped

                    # Hitung independensi antara bit i dan bit j
                    independence_sum += ((y1 >> i) & 1 ^ (y2 >> i) & 1) ^ ((y1 >> j) & 1 ^ (y2 >> j) & 1)

            # Normalisasi dan update total independensi
            total_independence += independence_sum / (n * bit_length)
            total_pairs += 1

    # Hitung nilai BIC-SAC rata-rata
    bic_sac_value = total_independence / total_pairs
    return bic_sac_value

def calculate_bic_sac_matrix(sbox):
    n = len(sbox)  # Number of inputs in the S-Box
    bit_length = 8  # Bit length of output
    bic_sac_matrix = np.zeros((bit_length, bit_length))  # Initialize BIC-SAC matrix (8x8)

    # Loop through all output bit pairs to be compared
    for i in range(bit_length):
        for j in range(i + 1, bit_length):
            independence_sum = 0
            # Loop over all input values
            for x in range(n):
                for bit_to_flip in range(bit_length):  # Flip each bit of the input
                    flipped_x = x ^ (1 << bit_to_flip)  # Flip input bit
                    y1 = sbox[x]  # Output for original input
                    y2 = sbox[flipped_x]  # Output for flipped input

                    # Calculate the independence between bit i and bit j
                    bit_i1 = (y1 >> i) & 1
                    bit_i2 = (y2 >> i) & 1
                    bit_j1 = (y1 >> j) & 1
                    bit_j2 = (y2 >> j) & 1

                    # XOR the bit pairs to check how the output bits differ
                    independence_sum += ((bit_i1 ^ bit_j1) ^ (bit_i2 ^ bit_j2))

            # Normalize and fill the matrix
            bic_sac_matrix[i, j] = independence_sum / (n * bit_length)
            bic_sac_matrix[j, i] = bic_sac_matrix[i, j]  # Ensure the matrix is symmetric

    return bic_sac_matrix
