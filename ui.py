import streamlit as st
import pandas as pd
from excel import make_certificates  # Make sure `excel.py` is in the same directory or adjust the import

st.title('Certificate Generator')

# Upload Excel file
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file, sheet_name=None)
    sheet_names = df.keys()

    st.write("Sheet names:", sheet_names)

    selected_sheet = st.selectbox("Select a sheet", sheet_names)
    df = df[selected_sheet]

    columns = df.columns.tolist()
    st.write("Available columns:", columns)

    name_column = st.selectbox("Select the column with names", columns)

    if st.button("Generate Certificates"):
        if name_column:
            with st.spinner("Generating certificates..."):
                make_certificates(df, name_column)
            st.success("Certificates generated successfully.")
        else:
            st.error("Please select a column.")
