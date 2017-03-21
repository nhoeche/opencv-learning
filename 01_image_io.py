'''
1. Importing the module, loadin images and displaying them in a gui window
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Loading an image
im = cv2.imread("test_image.png")

# Showing the image with gtk2+
cv2.imshow("test", im)
k = cv2.waitKey(0) & 0xFF  # & 0xFF if on 64-bit machine
if k == ord('q'):
    cv2.destroyAllWindows()

# Showing the imge with matplotlib
plt.imshow(im, cmap='viridis', interpolation='bicubic')
plt.yticks([])
plt.xticks([])
plt.show()

# Saving an image
cv2.imwrite('image_new.jpg', im)
