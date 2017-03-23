'''
1. Accessing pixel values and image properties. Splitting and merging images.
   (Aka numpy for noobs)
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_image(img):
    plt.close()
    plt.imshow(img, cmap='hot', interpolation='bicubic')
    plt.yticks([])
    plt.xticks([])
    plt.show()


img = cv2. imread('test_image.png')
show_image(img)


# Accessing pixel values is just basic numpy:

# Accessing the blue value of a pixel:
blue = img[100, 100,  0]
print("Blue = {}".format(blue))

# Single pixels should be indexed with np.item() though:
img.itemset((150, 150, 2), 100)
red = img.item((150, 150, 2))
print("Red = {}".format(red))


# Accessing image properties
print(img.shape)  # array shape
print(img.size)  # number of pixels
print(img.dtype)  # type should be np.uint8


# Accessing image regions

# Getting the tile with the bomb on it
bomb_tile = img[120:210, 20:100]
show_image(bomb_tile)

# Pasting it anywhere (dimensions must match)
img[300:390, 300:380] = bomb_tile
show_image(img)


# Splitting and merging image channels

# Useful for reordering b,g,r or working on channels seperately:
b, g, r = cv2.split(img)  # splitting
img = cv2.merge((b, g, r))  # merging
blue = img[:, :, 0]
# Keep in mind that numpy indexing is faster


# Image padding (making borders)
# cv2.copyMakeBorder(source, top, bottom, left, right, type-flag, value)
img1 = bomb_tile

# Making different border types
replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(255, 0, 0))

# Showing them
plt.subplot(231)
plt.imshow(img1, 'gray')
plt.title('ORIGINAL')

plt.subplot(232)
plt.imshow(replicate, 'gray')
plt.title('REPLICATE')

plt.subplot(233)
plt.imshow(reflect, 'gray')
plt.title('REFLECT')

plt.subplot(234)
plt.imshow(reflect101, 'gray')
plt.title('REFLECT_101')

plt.subplot(235)
plt.imshow(wrap, 'gray')
plt.title('WRAP')

plt.subplot(236)
plt.imshow(constant, 'gray')
plt.title('CONSTANT')

plt.show()
