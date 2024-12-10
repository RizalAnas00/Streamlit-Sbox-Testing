
def calculate_bic_sac(sbox):
    n = len(sbox)
    bit_length = 8
    total_pairs = 0
    total_independence = 0
    for i in range(bit_length):
        for j in range(i + 1, bit_length):
            independence_sum = 0
            for x in range(n):
                for bit_to_flip in range(bit_length):
                    flipped_x = x ^ (1 << bit_to_flip)
                    y1 = sbox[x]
                    y2 = sbox[flipped_x]
                    independence_sum += ((y1 >> i) & 1 ^ (y2 >> i) & 1) ^ ((y1 >> j) & 1 ^ (y2 >> j) & 1)
            total_independence += independence_sum / (n * bit_length)
            total_pairs += 1

    return total_independence / total_pairs