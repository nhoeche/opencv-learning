'''
3. Drawing objects
'''

import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Drawing a diagonal blue line with 5 px thickness
start = (0, 0)
stop = (511, 511)
col = (255, 0, 0)
cv2.line(img, start, stop, col, 5)  # 5 = thickness

# Drawing a green rectangle
top_left = (384, 0)
btm_right = (510, 128)
col = (0, 255, 0)
cv2.rectangle(img, top_left, btm_right, col, 3)

# Drawing a circle
center = (447, 63)
radius = 63
col = (0, 0, 255)
cv2.circle(img, center, radius, col, -1)  # center and radius

# Drawing an ellipse
center = (256, 256)
major_minor = (100, 50)
cv2.ellipse(img, center, major_minor, 0, 0, 180, 255, -1)
# center, major axis length, minor axis length, angle, start and end angle

# Drawing a polygon
# 1. Array of vertices, should be int32
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
# 2. Drawing the polygon
cv2.polylines(img,[pts],True,(0,255,255))  # image, coords, closed?, color

# Adding text
# 1. specify font
font = cv2.FONT_HERSHEY_COMPLEX
color = (255, 255, 255)
cv2.putText(img, 'OpenCV-Test', (10, 500), font, 4, color, 2, cv2.LINE_AA)
# image, text, coords, font, font-scale, color, thickness, line-type


#Viewing the result
cv2.imshow('result', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('q'):
    cv2.destroyAllWindows
