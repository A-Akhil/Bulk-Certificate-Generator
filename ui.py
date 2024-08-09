import os
import streamlit as st
import pandas as pd
import matplotlib.font_manager as fm  # For cross-platform font management
from excel import make_certificates, preview_certificate

st.title('Certificate Generator')

# Upload Excel file
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

# Upload template file
uploaded_template = st.file_uploader("Choose a template image", type=["png", "jpg", "jpeg"])

# Input for custom output directory
output_dir = st.text_input("Enter the output directory", "out")

# Input for vertical offset
vertical_offset = st.slider("Adjust the vertical position of the name", -200, 200, 0)

# Input for font size
font_size = st.slider("Select the font size for the name", 20, 200, 80)

# Get all system fonts
fonts = fm.findSystemFonts(fontext='ttf')
font_names = {os.path.basename(font).split('.')[0]: font for font in fonts}
font_choice = st.selectbox("Select a font", list(font_names.keys()))

# Name for preview
preview_name = st.text_input("Enter a name to preview the certificate", "A Akhil")

if uploaded_template and preview_name:
    # Save the uploaded template to a temporary file
    with open("temp_template.png", "wb") as f:
        f.write(uploaded_template.read())

    # Display preview
    preview_image = preview_certificate("temp_template.png", preview_name, vertical_offset, font_size, font_names[font_choice])
    st.image(preview_image, caption="Certificate Preview", use_column_width=True)

if uploaded_file and uploaded_template:
    df = pd.read_excel(uploaded_file, sheet_name=None)
    sheet_names = df.keys()

    st.write("Sheet names:", sheet_names)

    selected_sheet = st.selectbox("Select a sheet", sheet_names)
    df = df[selected_sheet]

    columns = df.columns.tolist()
    st.write("Available columns:", columns)

    name_column = st.selectbox("Select the column with names", columns)

    if st.button("Generate Certificates"):
        if name_column and uploaded_template:
            with st.spinner("Generating certificates..."):
                # Call the function with the template file and custom output directory
                make_certificates(df, name_column, "temp_template.png", output_dir, vertical_offset, font_size, font_names[font_choice])

                st.success("Certificates generated successfully.")
        else:
            st.error("Please select a column and upload a template.")
else:
    st.info("Please upload both an Excel file and a template image.")
