# Streamlit-Sbox-Testing
Streamlit-Sbox-Testing is a Streamlit-based application for analyzing S-Boxes in cryptography. It provides tests for Non-Linearity (NL), Strict Avalanche Criterion (SAC), Bit Independence Criterion-Nonlinearity (BIC-NL), Bit Independence Criterion-Strict Avalanche Criterion (BIC-SAC), Linear Approximation Probability (LAP), and Differential Approximation Probability (DAP).

S-Box AES Example as an input : 
    99, 205, 85, 71, 25, 127, 113, 219, 63, 244, 109, 159, 11, 228, 94, 214,
    77, 177, 201, 78, 5, 48, 29, 30, 87, 96, 193, 80, 156, 200, 216, 86,
    116, 143, 10, 14, 54, 169, 148, 68, 49, 75, 171, 157, 92, 114, 188, 194,
    121, 220, 131, 210, 83, 135, 250, 149, 253, 72, 182, 33, 190, 141, 249, 82,
    232, 50, 21, 84, 215, 242, 180, 198, 168, 167, 103, 122, 152, 162, 145, 184,
    43, 237, 119, 183, 7, 12, 125, 55, 252, 206, 235, 160, 140, 133, 179, 192,
    110, 176, 221, 134, 19, 6, 187, 59, 26, 129, 112, 73, 175, 45, 24, 218,
    44, 66, 151, 32, 137, 31, 35, 147, 236, 247, 117, 132, 79, 136, 154, 105,
    199, 101, 203, 52, 57, 4, 153, 197, 88, 76, 202, 174, 233, 62, 208, 91,
    231, 53, 1, 124, 0, 28, 142, 170, 158, 51, 226, 65, 123, 186, 239, 246,
    38, 56, 36, 108, 8, 126, 9, 189, 81, 234, 212, 224, 13, 3, 40, 64,
    172, 74, 181, 118, 39, 227, 130, 89, 245, 166, 16, 61, 106, 196, 211, 107,
    229, 195, 138, 18, 93, 207, 240, 95, 58, 255, 209, 217, 15, 111, 46, 173,
    223, 42, 115, 238, 139, 243, 23, 98, 100, 178, 37, 97, 191, 213, 222, 155,
    165, 2, 146, 204, 120, 241, 163, 128, 22, 90, 60, 185, 67, 34, 27, 248,
    164, 69, 41, 230, 104, 47, 144, 251, 20, 17, 150, 225, 254, 161, 102, 70

dokumentasi setup dan instalasi streamlit lengkapnya ada disini: https://docs.streamlit.io/get-started/installation/command-line
TL;DR :
# 1. Pergi ke folder yang ingin digunakan untuk clone repo github ini
# 2. Buka terminal/cmd dengan direktori folder tsb
# 3. Buat environment dengan command :
   folder .venv akan terinstall di folder tsb.

    python -m venv .venv

# 4. Aktivasi environment yang sudah ada dengan command berikut :
   *disarankan menggunakan cmd/command prompt bagi windows karena untuk terminal biasanya terkena restriction sistem, walaupun ada caranya, namun lebih baik dilewati dengan menggunakan cmd saja*
   
    _Windows command prompt_
    .venv\Scripts\activate.bat
    
    _Windows PowerShell_
    .venv\Scripts\Activate.ps1
    
    _macOS and Linux_
    source .venv/bin/activate

# 6. Clone repo di folder yang sama
# 7. Arahkan termimal/cmd ke folder yang sama dengan environment
# 8. Install streamlit :
   
    pip install streamlit

# 9. Running Server / Jalankan script utama program :

    streamlit run app.py

    atau jika tidak berhasil, maka coba ini :

    python -m streamlit run app.py

# 10. Otomatis diarahkan ke web localhost
# 11. Untuk mematikan server, tekan CTRL + C dan untuk kembali ke terminal/cmd normal, ketik :

    deactivate

*Setiap kali menjalankan server selalu mengaktifkan environment terlebih dahulu*
