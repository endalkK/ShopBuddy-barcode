from flask import Flask, render_template, request 
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
from pyzbar.pyzbar import decode
import serial

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html') 

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout = 0.1)

@app.route('/process_data', methods=['POST']) 
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

#Dictonary for product information
data_dict = {
    "1234567890128": ["Orange", "1.99$"],
    "1001001001002": ["Apple", "1.99$"],
    "689375836755": ["Pasta","0.99$"]
}
data_list={
}

# Initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (400,400)
camera.rotation = 180
rawCapture = PiRGBArray(camera)

# Allow the camera to warmup
time.sleep(0.1)

# Grab an image from the camera using arduino serial input
while True:
    data = ser.readline().decode().strip()
    if data:
        print(data)
        camera.capture('test.jpg')

        barcode = read_barcode('test.jpg')
        if barcode in data_dict:
            print(data_dict[barcode])
            if barcode in data_list:
                data_list[barcode]+= 1
            else:
                data_list[barcode] = 1
            print(data_list)
    return 'Success'