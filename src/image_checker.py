from PIL import Image
import numpy as np

INPUT_IMAGE_PATH = './Images/input.png'
OUTPUT_IMAGE_PATH = './Images/output.png'
DIFFERENCE_IMAGE_PATH = './Images/difference.png'

def create_difference_image(input_image_path, output_image_path, difference_image_path):
    # Open the images
    input_image = Image.open(input_image_path)
    output_image = Image.open(output_image_path)

    # Convert images to numpy arrays
    input_image_data = np.array(input_image)
    output_image_data = np.array(output_image)

    # Ensure the images have the same shape
    if input_image_data.shape != output_image_data.shape:
        raise ValueError("Input and output images must have the same dimensions.")

    # Calculate the difference and amplify it
    difference_data = np.abs(input_image_data - output_image_data)

    # Convert the difference data back to an image
    difference_image = Image.fromarray(difference_data.astype(np.uint8))

    # Save the difference image
    difference_image.save(difference_image_path)

# Example usage
create_difference_image(INPUT_IMAGE_PATH, OUTPUT_IMAGE_PATH, DIFFERENCE_IMAGE_PATH)