from utils.binary_utils import binary_representation

def strict_avalanche_criterion(sbox):
    return calculate_sac_value(sbox), calculate_sac_matrix(sbox)

def calculate_sac_value(sbox):
    n = 8  # Panjang bit output S-Box
    num_inputs = len(sbox)
    total_flips = 0
    total_bits = 0

    for input_val in range(num_inputs):  # Loop semua input S-Box (0-255)
        original_output = binary_representation(sbox[input_val], n)

        for bit_to_flip in range(n):  # Flip setiap bit input (0-7)
            flipped_input = input_val ^ (1 << bit_to_flip)
            flipped_output = binary_representation(sbox[flipped_input], n)

            # Bandingkan output bit-by-bit
            bit_flips = sum(
                1 for orig_bit, flip_bit in zip(original_output, flipped_output)
                if orig_bit != flip_bit
            )

            total_flips += bit_flips
            total_bits += n  # Total bit yang dibandingkan adalah n (8) untuk setiap input

    # Hitung nilai SAC (rata-rata)
    sac_value = total_flips / total_bits
    return sac_value

def calculate_sac_matrix(sbox):
    n = 8  # Panjang bit output S-Box
    num_inputs = len(sbox)
    sac_matrix = [[0] * n for _ in range(n)]  # Matriks SAC 8x8

    for input_val in range(num_inputs):  # Loop semua input S-Box (0-255)
        original_output = binary_representation(sbox[input_val], n)

        for bit_to_flip in range(n):  # Flip setiap bit input (0-7)
            flipped_input = input_val ^ (1 << bit_to_flip)
            flipped_output = binary_representation(sbox[flipped_input], n)

            # Bandingkan output bit-by-bit
            for output_bit_index in range(n):
                if original_output[output_bit_index] != flipped_output[output_bit_index]:
                    sac_matrix[bit_to_flip][output_bit_index] += 1

    # Normalisasi matriks SAC (bagi total input 256 agar hasil probabilitas)
    for i in range(n):
        for j in range(n):
            sac_matrix[i][j] /= num_inputs

    return sac_matrix

