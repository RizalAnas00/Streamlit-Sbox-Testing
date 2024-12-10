import pandas as pd

def read_excel_file(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file, header=None)
        return ",".join(map(str, df.to_numpy().flatten())), df
    except Exception as e:
        raise ValueError(f"Error reading Excel file: {e}")
