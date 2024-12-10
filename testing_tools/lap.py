# LAP

import numpy as np
from itertools import product

def calculate_lap(sbox):
    n = 8  # Input and output bit length
    num_inputs = len(sbox)
    
    max_lap = 0  # Maximum LAP value

    # Iterate over all non-zero input and output masks
    for input_mask in range(1, num_inputs):
        for output_mask in range(1, num_inputs):
            count = 0

            # Check all input-output pairs
            for x in range(num_inputs):
                input_parity = bin(x & input_mask).count('1') % 2
                output_parity = bin(sbox[x] & output_mask).count('1') % 2

                if input_parity == output_parity:
                    count += 1

            # Calculate the probability and normalize it
            lap = abs(count - (num_inputs // 2)) / (num_inputs // 2)
            max_lap = max(max_lap, lap)

    return max_lap / 2  # LAP normalized to 0.5 for cryptographic analysis
