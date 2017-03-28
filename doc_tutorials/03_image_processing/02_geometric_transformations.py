'''
3. Learn how to do geometric transformations with openCV
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test_image.png')

# SCALING
# is just resizing images. Different interpolation methods can be used.
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# Second method:
height, width = img.shape[:2]
res = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(res)
plt.show()

# TRANSLATION
# Shifting an objects location. You need a transformation matrix for that.
img = cv2.imread('test_image.png', 0)
rows, cols = img.shape
# Creating the transformation matrix
M = np.float32([[1, 0, 100], [0, 1, 50]])
# Translating the image
dst = cv2.warpAffine(img, M, (cols, rows))  # !Columns first!

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.subplot(122)
plt.imshow(dst, cmap='gray')
plt.show()

# ROTATION
# Rotation by angle Θ is achieved by a transformation-matrix of [[cosΘ, -sinΘ],
#                                                                [sinΘ, cosΘ]]
# OpenCV makes it possibkle to adjust the rotation center and has a method for
# finding the transformation-matrix.
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)  # !Columns first!
# Transforming
dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.subplot(122)
plt.imshow(dst, cmap='gray')
plt.show()

# AFFINE TRANSFORM
# Afine transformation means, that all parallel lines in the original image are
# still parallel after transformation. To get the matrix you need three points
# in the image.
img = cv2.imread('lines.png')
rows, cols, ch = img.shape
# Points for the matrix
pts1 = np.float32([[100, 230], [200, 210], [120, 300]])
pts2 = np.float32([[100, 230],[250, 230],[100, 350]])
# Getting the matrix
M = cv2.getAffineTransform(pts1,pts2)
# Transforming
dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(dst)
plt.show()

# PERSPECTIVE TRANSFORMATION
# After transformation straight lines will remain straight.
# This needs a 3x3 transformation matrix and 4 corresponding points. Three of
# the points should not be colinear.
# Points for the matrix
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
# Getting the matrix
M = cv2.getPerspectiveTransform(pts1,pts2)
# Transforming
dst = cv2.warpPerspective(img,M,(300,300))
# (The example on the website is more clear)
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(dst)
plt.show()
