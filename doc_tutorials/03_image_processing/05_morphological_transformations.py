'''
5.  Learn how to apply morphological transformations on imges.

These are highly relevant, and needed for the watershed-segmentation for example.
'''
import numpy as np
import cv2
import matplotlib.pyplot as plt

# The main morphological transformations are: Erosion, dilation, opening and
# closing. They are based on the image shape and normally performed on binary
# images (thresholds).

# Generally a kernel is needed as input for the transformation

img = cv2.imread('j.png', 0)
kernel = np.ones((5, 5), dtype=np.uint8)

# 1. Erosion -> Erodes away the edges of the foreground object
erosion = cv2.erode(img, kernel, iterations=1)
plt.imshow(erosion, cmap='gray'), plt.show()

# 2. Dilation -> This is the opposite of Erosion and extends the foreground
dilation = cv2.dilate(img, kernel, iterations=1)
plt.imshow(dilation, cmap='gray'), plt.show()

# 3. Opening -> Erosion, followed by dilation. this is useful for noise reduct.
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
plt.imshow(opening, cmap='gray'), plt.show()

# 4. Closing -> Dilation followed by erosion, useful for closing small holes in
#               the foreground object
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
plt.imshow(closing, cmap='gray'), plt.show()

# 5. Morphological Gradient -> Substracting an erosion from a dilation. The
#                              result is an outline of the object
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.imshow(gradient, cmap='gray'), plt.show()

# 6. Tophat -> Difference between input and closing
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
plt.imshow(tophat, cmap='gray'), plt.show()

# 7- Blackhat -> Difference between input and opening
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
plt.imshow(blackhat, cmap='gray'), plt.show()
