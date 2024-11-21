# Import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
from pyzbar.pyzbar import decode
import serial

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout = 0.1)

#initializes 
def init():
    #establishes serial connection
    ser = serial.Serial("/dev/ttyUSB0", 9600, timeout = 0.1)
    
    #Dictonary for product information
    data_dict = {
        "1234567890128": ["Orange", "1.99$"],
        "1001001001002": ["Apple", "1.99$"],
        "689375836755": ["Pasta","0.99$"]
    }
    
    # Initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (400,400)
    camera.rotation = 180
    rawCapture = PiRGBArray(camera)

    # Allow the camera to warmup
    time.sleep(0.1)
    
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

init()

#take product name/identity from JSON
input = ''
for i in data_dict.values():
    if(i[0] == input):
        product = data_dict.keys()[data_dict.values().index(input)]

def scan_barcode():
# Grab an image from the camera using arduino serial input
    camera.start_preview()
    while True:
        data = ser.readline().decode().strip()
        if data:
            break
        camera.capture('test.jpg')

        barcode = read_barcode('test.jpg')
    
        if barcode == product:
            print(data_dict[barcode])
            time.sleep(1)
            return True
        
        time.sleep(0.25)
    camera.stop_preview()


read_barcode()
# Example usage


'''image_path = "test.jpg"  # Replace with the path to your image
barcode_data = read_barcode(image_path)
barcode_data_list = []
barcode_data_list.append(barcode_data)
for i in range(len(barcode_data_list)):
    if barcode_data_list[i] in data_dict:
        print(data_dict[barcode_data_list[i]])

# Store the data (e.g., in a text file)
if barcode_data:
    with open("barcode_data.txt", "w") as f:
        f.write(barcode_data)'''

cv2.waitKey(0)
exit()