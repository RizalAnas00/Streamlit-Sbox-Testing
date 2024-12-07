import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

# Fungsi Pendukung
def binary_representation(num, width):
    return [int(x) for x in f"{num:0{width}b}"]

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

def sbox_to_binary_table(sbox):
    table = []
    for value in sbox:
        table.append([int(bit) for bit in f"{value:08b}"])
    return np.array(table)

# Fungsi Ekspor Data ke Excel
def export_to_excel(data, filename):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        data.to_excel(writer, index=False, sheet_name="S-Box Results")
    processed_data = output.getvalue()
    return processed_data

# Streamlit GUI
st.title("S-Box Testing Tool")
st.write("Aplikasi ini mendukung pengujian *Non-Linearity (NL)* dan *Strict Avalanche Criterion (SAC)* serta import/export data.")

# Pilih Input Data
data_input_method = st.radio(
    "Pilih metode input data:",
    ["Manual Input", "Upload File (Excel)"]
)

if data_input_method == "Manual Input":
    # Input Manual
    sbox_input = st.text_area(
        "Masukkan S-Box (256 nilai integer, pisahkan dengan koma):",
        height=150,
    )
elif data_input_method == "Upload File (Excel)":
    uploaded_file = st.file_uploader("Upload file Excel berisi S-Box:", type=["xlsx"])
    if uploaded_file:
        try:
            df = pd.read_excel(uploaded_file)
            st.write("Data S-Box yang diimport:")
            st.dataframe(df)
            sbox_input = ",".join(map(str, df.iloc[:, 0].tolist()))
        except Exception as e:
            st.error(f"Terjadi kesalahan dalam membaca file: {str(e)}")

# Pilih jenis pengujian
test_type = st.radio(
    "Pilih jenis pengujian:",
    ["Non-Linearity (NL)", "Strict Avalanche Criterion (SAC)"]
)

if st.button("Jalankan Pengujian"):
    try:
        if not sbox_input:
            st.error("Input S-Box tidak boleh kosong!")
        else:
            sbox = list(map(int, sbox_input.split(",")))
            if len(sbox) != 256:
                st.error("S-Box harus memiliki panjang 256!")
            else:
                if test_type == "Non-Linearity (NL)":
                    binary_table = sbox_to_binary_table(sbox)
                    output_bits = 8
                    nl_values = []

                    for output_bit in range(output_bits):
                        fx = binary_table[:, output_bit]
                        nl = compute_nl_min(fx)
                        nl_values.append(nl)

                    overall_nl = min(nl_values)
                    st.success(f"Non-Linearity (NL): *{overall_nl}*")
                    result_df = pd.DataFrame({"Output Bit": list(range(8)), "NL Values": nl_values})
                elif test_type == "Strict Avalanche Criterion (SAC)":
                    sac_value = strict_avalanche_criterion(sbox)
                    st.success(f"Strict Avalanche Criterion (SAC): *{sac_value:.5f}*")
                    result_df = pd.DataFrame({"Metric": ["SAC"], "Value": [sac_value]})

                # Menampilkan hasil dalam tabel
                st.write("Hasil pengujian:")
                st.dataframe(result_df)

                # Menyediakan opsi untuk mengunduh hasil
                excel_data = export_to_excel(result_df, "sbox_results.xlsx")
                st.download_button(
                    label="Unduh Hasil sebagai Excel",
                    data=excel_data,
                    file_name="sbox_results.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
    except Exception as e:
        st.error(f"Terjadi kesalahan: {str(e)}")