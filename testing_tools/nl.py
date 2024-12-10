import numpy as np
from utils.binary_utils import sbox_to_binary_table

def hamming_distance(fx, gx):
    return sum(f != g for f, g in zip(fx, gx))

def generate_linear_functions(input_bits):
    functions = []
    for a in range(1, 1 << input_bits):
        for b in range(2):
            functions.append((a, b))
    return functions

def compute_gx(a, b, num_inputs, input_bits):
    gx = []
    for x in range(num_inputs):
        linear_sum = bin(a & x).count("1") % 2
        gx.append(linear_sum ^ b)
    return gx

def compute_nl_min(fx):
    num_inputs = len(fx)
    input_bits = int(np.log2(num_inputs))
    linear_functions = generate_linear_functions(input_bits)

    min_distance = num_inputs
    for a, b in linear_functions:
        gx = compute_gx(a, b, num_inputs, input_bits)
        distance = hamming_distance(fx, gx)
        min_distance = min(min_distance, distance)

    return min_distance

def perform_nl_test(sbox):
    binary_table = sbox_to_binary_table(sbox)
    output_bits = 8
    nl_values = []

    for output_bit in range(output_bits):
        fx = binary_table[:, output_bit]
        nl = compute_nl_min(fx)
        nl_values.append(nl)

    return nl_values, min(nl_values)
