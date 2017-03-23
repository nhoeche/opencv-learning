'''
2. Performing arithmetic operations on images.
'''
import cv2
import numpy as np

# This resembles matrix operations in numpy. The difference is that numpy uses
# modulo-addition and cv2 uses saturated addition. You should have a basic un-
# derstanding of matrix operations for this tutorial.

# Image addition
x = np.uint8([250])
y = np.uint8([10])

print(x + y)  # 255 + 10 = 260 % 256 = 4
print(cv2.add(x, y))  # 255 + 10 = 260 >= 255

# Image blending
# This is also image addition but with differently weighted values.
# g(x) = (1 - α)f_0(x) + αf_1(x)
# α is 0 to 1
img1 = cv2.imread('icon1.png')  # same resolution
img2 = cv2.imread('icon2.png')

dst = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Bitwise operations:
# These are useful when handling non-rectangular regions
icon = img1
image = cv2.imread('test_image.png')

# Lets put the icon in te top-right corner:
# Selecting the region of interest
rows, cols, chans = icon.shape
roi = image[0:rows, 0:cols]

# Creating a mask and inverse mask of the icon
img2gray = cv2.cvtColor(icon, cv2.COLOR_BGR2GRAY)  # Converting to gray
# Creating a mask from threshold
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)  # inverted mask with bitwise not

# Black-out the icon-region
image_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Take only the icon region
icon_fg = cv2.bitwise_and(icon, icon, mask=mask)

# Put the logo in ROI and modify the main image
dst = cv2.add(image_bg, icon_fg)
image[0:rows, 0:cols] = dst

cv2.imshow('inserted', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
