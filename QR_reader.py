from pyzbar.pyzbar import decode
from PIL import Image

def read_qr_code(file_name):
    with open(file_name, 'rb') as image_file:
        image = Image.open(image_file)
        decoded_objects = decode(image)
        for obj in decoded_objects:
            print(f"Data: {obj.data.decode('utf-8')}")

if __name__ == "__main__":
    file_name = input("samples.png ")

    read_qr_code(file_name)
