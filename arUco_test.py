import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

# Define arUco dictionary
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# Generate a marker
marker_id = 12
marker_size = 200  # Size in pixels
marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

cv2.imwrite('marker_42.png', marker_image)
plt.imshow(marker_image, cmap='gray', interpolation='nearest')
plt.axis('off')  # Hide axes
plt.title(f'ArUco Marker {marker_id}')
plt.show()

import cv2
import numpy as np

# Load the image
image = cv2.imread('C:/Users/dogma/Documents/ShopBuddy-barcode/Figure_1.png')\

#camera capture
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# Convert the image to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()

# Create the ArUco detector
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
# Detect the markers
count = 0
while count <20:
    count+= 1
    corners, ids, rejected = detector.detectMarkers(gray)
    # Print the detected markers
    print("Detected markers:", ids)
    cv2.imshow('ArUco Detection', frame)
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        cv2.waitKey(0)
    time.sleep(1)
cv2.destroyAllWindows()