import numpy as np

def walsh_hadamard_transform(f):
    n = len(f)
    hadamard = np.copy(f)
    step = 1
    while step < n:
        for i in range(0, n, step * 2):
            for j in range(i, i + step):
                x = hadamard[j]
                y = hadamard[j + step]
                hadamard[j] = x + y
                hadamard[j + step] = x - y
        step *= 2
    return hadamard

def calc_bic_nl(sbox):
    non_linearities = []
    for bit in range(8):  # Setiap output bit
        # Iterasi pada setiap elemen sbox dan lakukan operasi bitwise
        outputs = np.array([((x >> bit) & 1) * 2 - 1 for x in sbox])  # Konversi output bit ke {-1, 1}
        spectrum = walsh_hadamard_transform(outputs)  # Hitung Walsh-Hadamard Transform
        nl = (256 - np.max(np.abs(spectrum))) // 2  # Hitung Non-Linearity
        non_linearities.append(nl)
        
    return min(non_linearities)