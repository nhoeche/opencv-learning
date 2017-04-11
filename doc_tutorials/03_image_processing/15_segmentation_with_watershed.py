'''
15. Learn how to segment an image using the watershed algorithm.

A grayscale image can be viewed as a morphological maps, with pixels of high intensity as peaks and pixels with low intensity as valleys. The watershed algorithm starts filling every isolated valley (local minima) with differently colored water (labels). The waters then rise among the peaks (gradients) until they merge, building barriers. These barrierrs are the result of the segmentation.
'''
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load the image to be segmented
img = cv2.imread('water_coins.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# First we want to approximately identify the coins. We can use Otsu's binari-
# zation for this.
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)


# Now we have to remove the remaining noise using erosion and dilation.
# Erosion removes the boundary pixels of an object, dilation extends the
# boundary pixels into the background. That way we can determine areas that
# certainly belong to either back- or foreground.

# Noise removal
kernel = np.ones((3, 3), np.uint8)
# Determintes the center of the coins
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Finding the sure background area
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Finding the sure foreground area
# The distance transform calculates the distance from the center of the coins
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)

# Finding the unknown region
unknown = cv2.subtract(sure_bg, sure_fg)

# Now we create a marker (Array of same shape as the image with int32 datatype)
# and label the regions inside it. Sure fore- or background get labeled with
# positive integers, unsure regions get left at 0. cv2.connectedComponents does
# that, leaving the background at 0 and labelling regions starting from 1.

# Marker labelling
_, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers += 1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0


# Now we can finally apply the watershed algorithm to the marker image.
water = cv2.watershed(img, markers)
img_final = img
img_final[water == -1] = [255,0,0]


# Displaying teh result:
plt.subplot(331)
plt.imshow(img)
plt.title('Original image')
plt.xticks([]), plt.yticks([])

plt.subplot(332)
plt.imshow(thresh, cmap='gray')
plt.title('Otsu threshold')
plt.xticks([]), plt.yticks([])

plt.subplot(333)
plt.imshow(opening, cmap='gray')
plt.title('Morphological opening')
plt.xticks([]), plt.yticks([])

plt.subplot(334)
plt.imshow(sure_fg, cmap='gray')
plt.title('Sure foreground')
plt.xticks([]), plt.yticks([])

plt.subplot(335)
plt.imshow(sure_bg, cmap='gray')
plt.title('Sure background')
plt.xticks([]), plt.yticks([])

plt.subplot(336)
plt.imshow(unknown, cmap='gray')
plt.title('Unknown region')
plt.xticks([]), plt.yticks([])

plt.subplot(337)
plt.imshow(markers)
plt.title('Marker image')
plt.xticks([]), plt.yticks([])

plt.subplot(338)
plt.imshow(water)
plt.title('Watershed result')
plt.xticks([]), plt.yticks([])

plt.subplot(339)
plt.imshow(img_final)
plt.title('Segmented image')
plt.xticks([]), plt.yticks([])

plt.show()

plt.savefig('watershed_workflow.svg')
