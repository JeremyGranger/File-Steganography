from PIL import Image
import numpy as np
import zipfile

IMAGE_PATH = './Images/input.png'
ZIP_PATH = './Files/input.zip'
OUTPUT_PATH = './Images/output.png'

def encode_zip_in_image(image_path, zip_path, output_path):
    # Open the image
    image = Image.open(image_path)
    image_data = np.array(image)

    # Read the zip file
    with open(zip_path, 'rb') as zip_file:
        zip_data = zip_file.read()

    # Convert zip data to binary string
    zip_bin = ''.join(format(byte, '08b') for byte in zip_data)

    # Check if the image can hold the zip data
    if len(zip_bin) > image_data.size:
        raise ValueError("The image is too small to hold the zip file data.")

    # Embed the zip data into the image
    flat_image_data = image_data.flatten()
    for i in range(len(zip_bin)):
        flat_image_data[i] = (flat_image_data[i] & ~1) | int(zip_bin[i])

    # Reshape the modified flat data back to the original image shape
    encoded_image_data = flat_image_data.reshape(image_data.shape)
    encoded_image = Image.fromarray(encoded_image_data)

    # Save the encoded image
    encoded_image.save(output_path)

# Example usage
encode_zip_in_image(IMAGE_PATH, ZIP_PATH, OUTPUT_PATH)
