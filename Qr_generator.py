import qrcode  # Import the qrcode library for generating QR codes

def generate_qr_code(data, file_name):
    # Create a QRCode object with specific parameters
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add the input data to the QR code
    qr.add_data(data)
    
    # Generate the QR code image and save it with the specified file name
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

if __name__ == "__main__":
    # Prompt the user to input the data for the QR code
    data = input("Enter data to encode: ")
    
    # Prompt the user to input the file name for the QR code image
    file_name = input("Enter file name (with extension): ")

    # Call the generate_qr_code function with the input data and file name provided by the user
    generate_qr_code(data, file_name)
