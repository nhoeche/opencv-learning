'''
1. Learning to change between colorspaces (e.g. BGR <-> Gray <-> HSV)
'''
import cv2
import numpy as np

# There are more than 150 color-conversion methods in opencv. You generally use
# cv2.cvtColor(input_image, flag) to do it. The flag determines the conversion
# method.
# flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
# print(flags)

# In the HSV colorspace it's easier to extract objeccts of a certain color.
# So let's convert a video stream to HSV and extract blue objects.

cap = cv2.VideoCapture(0)

while(1):
    # Capture the frame:
    _, frame = cap.read()

    # Convert BGR to HSV:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range for blueu colors:
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Apply threshold to the hsv image:
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply mask to t he original image:
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the frame
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('blue object', res)
    k = cv2.waitKey(5) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
