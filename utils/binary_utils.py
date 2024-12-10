import numpy as np

def sbox_to_binary_table(sbox):
    table = []
    for value in sbox:
        table.append([int(bit) for bit in f"{value:08b}"])
    return np.array(table)

def binary_representation(num, width):
    """
    Mengubah bilangan integer menjadi representasi biner dengan panjang tetap.

    Args:
        num (int): Bilangan yang akan dikonversi.
        width (int): Panjang representasi biner.

    Returns:
        list: List bilangan biner dengan panjang tetap.
    """
    return [int(x) for x in f"{num:0{width}b}"]
