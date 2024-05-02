from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import ImageFont
import time
import logging
import sys

# Initialize OLED display
oled = i2c(port=1, address=0x3C)
device = sh1106(oled, rotate=0)

# Load a large font
font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
font_size = 18
font = ImageFont.truetype(font_path, font_size)

# width and height
width = device.width
height =  device.height

# Function to display text on OLED with dynamic font size
def display_on_oled(text):

    with canvas(device) as draw:
        # Clear display
        draw.rectangle(device.bounding_box, outline="white", fill="black")


        font_size = 12

        # Decrease font size until the text fits within the screen width
        while True:
            font = ImageFont.truetype(font_path, font_size)
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]

            if text_width < width:
                break

            font_size -= 1
            if font_size <= 0:
                # Font size too small, text cannot fit
                return

        # Calculate the position to center the text vertically(y) and horizontally(x)
        text_height = text_bbox[3] - text_bbox[1]
        y = (device.height - text_height) // 2
        x = (device.width - text_width) // 2


        # Display the text
        draw.text((x, y), text, font=font, fill="white")
    
