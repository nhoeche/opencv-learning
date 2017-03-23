'''
2.1 Performing arithmetic operations on images.
    Bitwise operations
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Bitwise operations:
# These are useful when handling non-rectangular regions
icon = cv2.imread('icon1.png')
image = cv2.imread('test_image.png')

# Lets put the icon in te top-right corner:
# Selecting the region of interest
rows, cols, chans = icon.shape
roi = image[0:rows, 0:cols]

# Creating a mask:
# Converting to gray
icon_gray = cv2.cvtColor(icon, cv2.COLOR_BGR2GRAY)

# Creating a mask from threshold
ret, mask = cv2.threshold(icon_gray, 250, 255, cv2.THRESH_BINARY)
# Inverting the mask
mask_inv = cv2.bitwise_not(mask)  # inverted mask with bitwise not

# Black-out the icon-region
image_bg = cv2.bitwise_and(roi, roi, mask=mask)

# Take only the icon region
icon_fg = cv2.bitwise_and(icon, icon, mask=mask_inv)

# Put the logo in ROI and modify the main image
dst = cv2.add(image_bg, icon_fg)
image[0:rows, 0:cols] = dst

cv2.imshow('inserted', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
