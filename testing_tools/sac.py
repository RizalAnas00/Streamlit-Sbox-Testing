from utils.binary_utils import binary_representation

def strict_avalanche_criterion(sbox):
    n = 8
    num_inputs = len(sbox)
    total_flips = 0
    total_bits = 0

    for input_val in range(num_inputs):
        original_output = binary_representation(sbox[input_val], n)

        for bit_to_flip in range(n):
            flipped_input = input_val ^ (1 << bit_to_flip)
            flipped_output = binary_representation(sbox[flipped_input], n)

            bit_flips = sum(
                1 for orig_bit, flip_bit in zip(original_output, flipped_output)
                if orig_bit != flip_bit
            )

            total_flips += bit_flips
            total_bits += n

    return total_flips / total_bits
