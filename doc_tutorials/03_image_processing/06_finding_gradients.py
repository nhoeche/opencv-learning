'''
6. Finding gradients and edges in images. Learn filters like
   Sobel, Laplace and Scharr
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('test_image2.png')

# SOBEL-kernel
# This applies a gaussian smoothing and then finds edges in the image. It is
# resistant to noise. You can influence the kernel size and the direction of
# derivatives. The SCHARR-kernel is better at 3x3 kernels.

laplacian = cv2.Laplacian(img, cv2.CV_64F)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,2)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y')
plt.xticks([])
plt.yticks([])

plt.show()
