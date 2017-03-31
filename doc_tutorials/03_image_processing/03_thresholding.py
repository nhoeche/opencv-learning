'''
3. Learning different methods of image thresholding
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

# SIMPLE THRESHOLDING
# If the pixel is greater than a certain value it gets assigned white. If it is
# smaller it is black. The source should be grayscale.
img = cv2.imread('gradient.jpg', 0)  # 0 to read in as grayscale

# cv2.threshold(Sourve, threshold, max_value, FLAG)
# Black/White
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Inverted Black/White
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# Only white, below threshold untouched
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# Only black, above threshold untouched
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# Black for above threshold
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Source', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()


# ADAPTIVE THRESHOLDING
# Uses different thresholds for different regions of the image, for an adaptive
# result. It needs three arguments for the method, the block size of regions
# and a constant to be subtracted off the threshold. It has only 1 return value
img = cv2.imread('example.jpg', 0)
img = cv2.medianBlur(img, 5)

# Simple threshold to compare difference
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Adaptive thresholding (with means of neighborhood)
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 11, 2)
# Adaptive thresholding (with gaussian weighted means)
thresh3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                              cv2.THRESH_BINARY, 11, 2)

titles = ['Source', 'BINARY', 'MEAN_C', 'MEAN_GAUSSIAN_C']
images = [img, thresh1, thresh2, thresh3]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()


# OTSU'S BINARIZATION
# This calculates a threshold between to histogram peaks in bimodal images.
# It isn't accurate for images that aren't bimodal. You can use the normal
# cv2.threshold() for this and pass an extra flag cv2.THRESH_OTSU
