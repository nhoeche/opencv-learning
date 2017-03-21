'''
5. Creating ntrackbars to control certain parameters
'''
import cv2
import numpy as np

# We will create a black image with three sliders for RGB. the image will
# display the selected color.


def nothing(x):
    # Empty callback-function, cause a trackbar always has a function attached
    pass


# Creating a black image and a window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
# arguments: name, window, start, stop, callback-function
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

# Trackbars from 0 to 1 can function as switches:
# Creating an ON / OFF switch
switch = '0: OFF \n1: ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

# Displaying the image
while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # Get current positions of four trackbars
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]  # Always keep in mind openCV uses BGR

cv2.destroyAllWindows()
