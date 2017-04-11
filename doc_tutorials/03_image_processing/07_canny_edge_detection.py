'''
7. The Canny-Edge-Detection Algorithm

It is a multistage algorithm to detect edges. First it will reduce noise in the
image with a 5x5 gaussian filter. Then it will find the intensity gradient of
the image. Then it applies a horizontal and vertical sobel-kernel to the image.
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Callback-function for trackbars
def nothing():
    pass

# Image loading
img = cv2.imread('example.jpg')

# Windows
cv2.namedWindow('image')
cv2.namedWindow('canny-edges')

# Create trackbars
cv2.createTrackbar('thres_bot', 'canny-edges', 0, 255, nothing)
cv2.createTrackbar('thresh_top', 'canny-edges', 0, 255, nothing)

# Display original image
cv2.imshow('image', img)

# Displaying the image
while True:
    k = cv2.waitKey(1) & 0xFF

    # Get current positions of four trackbars
    thresh_bot = cv2.getTrackbarPos('thres_bot', 'canny-edges')
    thresh_top = cv2.getTrackbarPos('thres_top', 'canny-edges')

    # The Canny-edges
    edges = cv2.Canny(img, thresh_bot, thresh_top)

    # Display Canny-edges
    cv2.imshow('canny-edges', edges)

    if k == ord('q'):
        break

# Close windows
cv2.destroyAllWindows()
