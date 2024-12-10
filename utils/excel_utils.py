from io import BytesIO
import pandas as pd

def export_to_excel(data, filename):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        data.to_excel(writer, index=False, sheet_name="S-Box Results")
    return output.getvalue()
