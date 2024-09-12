import cv2
import numpy as np
from pyzbar.pyzbar import decode

book = cv2.imread("book.png", 0)
#Image is too large to show fully on screen
book = cv2.resize(book, (0, 0), fx = 0.4, fy = 0.4)
cv2.imshow("original", book)

# Binary inverse because we're making the black lines white and the white lines black
adaptedBook = cv2.adaptiveThreshold(book, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 135, 17)
#cv2.imshow("threshold", adaptedBook)

output = cv2.connectedComponentsWithStats(adaptedBook, 4, cv2.CV_32S)
(numLabels, labels, stats, centroids) = output

for i in range(numLabels):
    if i > 0:   # 0th label is the background
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        area = stats[i, cv2.CC_STAT_AREA]
        #cv2.rectangle(adaptedBook, (x, y), (x+w, y+h), 128, 2) #Puts a box around every line

        if (h/w) < 1.4:
            cv2.rectangle(adaptedBook, (x, y), (x+w, y+h), 0, -1) #Removes everything that isn't (h/w) < 2.1
        if h < 100:
            cv2.rectangle(adaptedBook, (x, y), (x+w, y+h), 0, -1)
        if h > 1000:
            cv2.rectangle(adaptedBook, (x, y), (x+w, y+h), 0, -1)
        
adaptedBook = cv2.bitwise_not(adaptedBook)
adaptedBook = cv2.cvtColor(adaptedBook, cv2.COLOR_GRAY2BGR)
adaptedBook = cv2.resize(adaptedBook, (0, 0), fx = 0.4, fy = 0.4)
cv2.imshow("boxes", adaptedBook)

cv2.waitKey(0)