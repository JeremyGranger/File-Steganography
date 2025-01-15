from PIL import Image
import numpy as np

OUTPUT_PATH = './Images/output.png'
DECODED_ZIP_PATH = './Files/decoded.zip'

def decode_zip_from_image(encoded_image_path, decoded_zip_path):
    # Open the encoded image
    encoded_image = Image.open(encoded_image_path)
    encoded_image_data = np.array(encoded_image)

    # Flatten the image data
    flat_image_data = encoded_image_data.flatten()

    # Extract the binary data from the image
    zip_len_bin = ''.join(str(flat_image_data[i] & 1) for i in range(32))
    zip_len = int(zip_len_bin, 2)
    zip_bin = ''.join(str(flat_image_data[i] & 1) for i in range(32, 32 + zip_len))

    # Convert the binary string to bytes
    zip_bytes = bytearray()
    for i in range(0, len(zip_bin), 8):
        byte = zip_bin[i:i+8]
        if len(byte) == 8:
            zip_bytes.append(int(byte, 2))

    # Write the bytes to the decoded zip file
    with open(decoded_zip_path, 'wb') as decoded_zip_file:
        decoded_zip_file.write(zip_bytes)

decode_zip_from_image(OUTPUT_PATH, DECODED_ZIP_PATH)