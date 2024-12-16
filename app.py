import streamlit as st
import pandas as pd

from utils.data_utils import read_excel_file
from utils.excel_utils import export_to_excel

from testing_tools.nl import perform_nl_test
from testing_tools.sac import strict_avalanche_criterion
from testing_tools.bic_nl import calc_bic_nl
from testing_tools.bic_sac import calculate_bic_sac
from testing_tools.lap import calculate_lap
from testing_tools.dap import calculate_dap

# Styling
st.set_page_config(page_title="S-Box Testing Tool", page_icon="🔬", layout="wide")

st.title("S-Box Testing Tool")
st.markdown("*Streamlit-Sbox-Testing adalah aplikasi berbasis Streamlit untuk menganalisis S-Box dalam kriptografi. Aplikasi ini menyediakan pengujian untuk Non-Linearity (NL), Strict Avalanche Criterion (SAC), Bit Independence Criterion-Nonlinearity (BIC-NL), Bit Independence Criterion-Strict Avalanche Criterion (BIC-SAC), Linear Approximation Probability (LAP), dan Differential Approximation Probability (DAP).*")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    data_input_method = st.radio("Pilih metode input data:", ["Manual Input", "Upload File (Excel)"])

    sbox_input = ""
    if data_input_method == "Manual Input":
        sbox_input = st.text_area("Masukkan S-Box (256 nilai integer, pisahkan dengan koma, tanpa kurung siku):", height=150)
    elif data_input_method == "Upload File (Excel)":
        uploaded_file = st.file_uploader("Upload file Excel berisi S-Box:", type=["xlsx"])
        if uploaded_file:
            try:
                sbox_input, df = read_excel_file(uploaded_file)
                st.write("Data S-Box yang diimport:")
                st.dataframe(df)
            except Exception as e:
                st.error(f"Terjadi kesalahan: {str(e)}")

    # Pilih jenis pengujian
    st.write("Note: Belum semua tersedia untuk semua jenis pengujian.")
    precision = st.slider("Pilih keakuratan (jumlah angka di belakang desimal):", min_value=1, max_value=10, value=5)
    test_type = st.radio("Pilih jenis pengujian:", ["Non-Linearity (NL)", 
                                                    "Strict Avalanche Criterion (SAC)",
                                                    "BIC-NL",
                                                    "BIC-SAC",
                                                    "Linear Approximation Probability (LAP)",
                                                    "Differential Approximation Probability (DAP)"])

    run_test_button = st.button("Jalankan Pengujian")

with col2:
    st.markdown("## **Hasil pengujian akan tampil di sini:**")

    if run_test_button:
        try:
            if not sbox_input:
                st.error("Input S-Box tidak boleh kosong!")
            else:
                sbox = list(map(int, sbox_input.split(",")))
                if len(sbox) != 256:
                    st.error("S-Box harus memiliki panjang 256!")
                else:
                    if test_type == "Non-Linearity (NL)":
                        nl_values, overall_nl = perform_nl_test(sbox)
                        st.success(f"Non-Linearity (NL): *{overall_nl:.{precision}f}*")
                        formatted_nl_values = [f"{nl:.{precision}f}" for nl in nl_values]
                        result_df = pd.DataFrame({"Output Bit": list(range(8)), "NL Values": formatted_nl_values})

                    elif test_type == "Strict Avalanche Criterion (SAC)":
                        sac_value, sac_matrix  = strict_avalanche_criterion(sbox)                   
                        st.success(f"Strict Avalanche Criterion (SAC): *{sac_value:.{precision}f}*")

                        # Menampilkan matriks SAC 8x8
                        sac_value_str = "\n".join(
                            [" ".join(f"{value:.{precision}f}" for value in row) for row in sac_matrix]
                        )
                        result_df = pd.DataFrame(sac_matrix)

                    elif test_type == "BIC-NL":
                        nl_value = calc_bic_nl(sbox)
                        st.success(f"BIC-NL: *{nl_value:.{precision}f}*")
                        result_df = pd.DataFrame({"Metric": ["BIC-NL"], "Value": [f"{nl_value:.{precision}f}"]})

                    elif test_type == "BIC-SAC":
                        bic_sac_value, bic_sac_matrix  = calculate_bic_sac(sbox)  # Menghitung nilai BIC-SAC
                        
                        st.success(f"BIC-SAC: *{bic_sac_value:.{precision}f}*")

                        bic_sac_str = "\n".join(
                            [" ".join(f"{value:.{precision}f}" for value in row) for row in bic_sac_matrix]
                        )

                        result_df = pd.DataFrame(bic_sac_matrix)

                    elif test_type == "Linear Approximation Probability (LAP)":
                        lap_value = calculate_lap(sbox)
                        st.success(f"Linear Approximation Probability (LAP): *{lap_value:.{precision}f}*")
                        result_df = pd.DataFrame({"Metric": ["LAP"], "Value": [f"{lap_value:.{precision}f}"]})

                    elif test_type == "Differential Approximation Probability (DAP)":
                        dap_value = calculate_dap(sbox)
                        st.success(f"Differential Approximation Probability (DAP): *{dap_value:.{precision}f}*")
                        result_df = pd.DataFrame({"Metric": ["DAP"], "Value": [f"{dap_value:.{precision}f}"]})

                    # Menampilkan hasil dalam tabel dengan angka yang sesuai presisi
                    st.write("Hasil pengujian:")
                    st.dataframe(result_df, use_container_width=True) 

                    # Unduh hasil
                    excel_data = export_to_excel(result_df, "sbox_results.xlsx")
                    st.download_button(
                        label="Unduh Hasil sebagai Excel",
                        data=excel_data,
                        file_name="sbox_results.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    )
        except Exception as e:
            st.error(f"Terjadi kesalahan: {str(e)}")
