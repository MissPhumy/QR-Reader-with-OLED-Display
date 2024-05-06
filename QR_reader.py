from pyzbar.pyzbar import decode  # Import the decode function from pyzbar.pyzbar module for decoding QR codes
from PIL import Image  # Import the Image module from the PIL library for working with images

def read_qr_code(file_name):
    # Open the image file in binary mode
    with open(file_name, 'rb') as image_file:
        # Open the image using the Image module
        image = Image.open(image_file)
        
        # Decode the QR code(s) present in the image
        decoded_objects = decode(image)
        
        # Iterate over each decoded object
        for obj in decoded_objects:
            # Print the decoded data
            print(f"Data: {obj.data.decode('utf-8')}")

if __name__ == "__main__":
    # Prompt the user to input the file name containing the QR code image
    file_name = input("Enter the file name containing the QR code image: ")

    # Call the read_qr_code function with the file name provided by the user
    read_qr_code(file_name)
