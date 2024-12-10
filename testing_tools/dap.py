def calculate_dap(sbox):
    n = 8  # Input and output bit length
    num_inputs = len(sbox)

    # Initialize the differential distribution table (DDT)
    ddt = [[0 for _ in range(num_inputs)] for _ in range(num_inputs)]

    # Calculate the DDT
    for x1 in range(num_inputs):
        for delta_x in range(num_inputs):
            x2 = x1 ^ delta_x  # Calculate the second input
            delta_y = sbox[x1] ^ sbox[x2]  # Calculate the output difference
            ddt[delta_x][delta_y] += 1

    # Calculate the maximum DAP (excluding delta_x = 0)
    max_dap = 0
    for delta_x in range(1, num_inputs):  # delta_x = 0 is excluded
        for delta_y in range(num_inputs):
            probability = ddt[delta_x][delta_y] / num_inputs
            max_dap = max(max_dap, probability)

    return max_dap

