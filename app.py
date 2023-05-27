import streamlit as st

import streamlit_qrcode_scanner as st_qrcode

# Rest of the code

# Use the file uploader to select a QR code image from the gallery

uploaded_file = st.file_uploader("Upload a QR code image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:

    # Read the uploaded image file

    img_bytes = uploaded_file.read()

    # Use the st_qrcode.scan function to decode the QR code image

    qr_code = st_qrcode.scan(img_bytes)

    if qr_code is not None:

        st.write(qr_code)

    else:

        st.write("No QR code found in the uploaded image.")

