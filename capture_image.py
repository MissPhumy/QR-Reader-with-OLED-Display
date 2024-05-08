import time  # Import the time module for sleep function
import picamera  # Import the picamera module for working with Raspberry Pi camera

def capture_image(file_path):
    # Initialize PiCamera object as 'camera'
    with picamera.PiCamera() as camera:
        # Set the resolution of the camera
        camera.resolution = (1024, 768)  # You can adjust this resolution as needed
        # Start the camera preview
        camera.start_preview()
        # Wait for the camera to warm up (optional but recommended)
        time.sleep(2)
        # Capture an image and save it to the specified file path
        camera.capture(file_path)

if __name__ == "__main__":
    # Specify the file path where you want to save the captured image
    file_path = "/path/to/save/image.jpg"  # Change this to your desired file path
    # Call the capture_image function with the specified file path
    capture_image(file_path)
    # Print a message indicating successful image capture
    print("Image captured successfully!")
