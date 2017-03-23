'''
2.1 Performing arithmetic operations on images.
    Adding and blending
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
