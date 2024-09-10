import cv2
from pyzbar.pyzbar import decode


def read_barcode(image_path):
    """Reads barcode from the given image and returns the data."""

    image = cv2.imread(image_path)
    decoded_objects = decode(image)

    if decoded_objects:
        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            barcode_type = obj.type

            print("Barcode Type:", barcode_type)
            print("Data:", data)
            return data
    else:
        print("No barcode found in the image.")
        return None

# Example usage
image_path = "book.png"  # Replace with the path to your image
barcode_data = read_barcode(image_path)

# Store the data (e.g., in a text file)
if barcode_data:
    with open("barcode_data.txt", "w") as f:
        f.write(barcode_data)