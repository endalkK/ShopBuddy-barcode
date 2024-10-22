import cv2 as cv
import numpy as np
 
cap = cv.VideoCapture(0)
 
while(1):
 
    # Take each frame
    _, frame = cap.read()
 
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
 
    # define range of white color in HSV
    lower_white = np.array([0,0,0])
    upper_white = np.array([247, 241, 188])
 
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_white, upper_white)
 
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
 
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break