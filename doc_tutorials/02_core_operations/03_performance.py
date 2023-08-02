'''
3. Performance-measurement and -improvement
'''
# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt
# The modules time and profile from python are assisting well on this behalf

# %%

# cv2.getTickCount() is like tic() toc() in other languages
e1 = cv2.getTickCount()  # Is the same as time.time()
img = cv2.imread('test_image.png')
plt.imshow(img[:,:,::1])
plt.show()
e2 = cv2.getTickCount()

# %%

# cv2.getTickFrequency = numbers of clock-cycles per second
t = (e2 - e1) / cv2.getTickFrequency()
print("e2 - e1 = {}\n".format(e2 - e1))
print("t = {}".format(t))

# %%

# OpenCV has much optimized code by default:
cv2.setUseOptimized(True)
cv2.useOptimized()
%timeit res = cv2.medianBlur(img,49)

# %%

# With disabled optimization
cv2.setUseOptimized(False)
cv2.useOptimized()
%timeit res = cv2.medianBlur(img,49)

# %%

# Measuring performance with IPython / Jupyter:
x = 5
# %timeit is a Jupyter magic command:
%timeit y = x**2
%timeit y = x * x

# %%

z = np.uint8([5])

%timeit y = z * z
%timeit y = np.square(z)
# Conclusion: Python scalar operations are faster than numpy scalar operations.
#             (Numpy is better on arrays)

# %%

%timeit z = cv2.countNonZero(img)
%timeit z = np.count_nonzero(img)
# Conclusion: OpenCV functions are usually faster than numpy functions. Keep in
#             mind that numpy works with views and openCV with copies.
# %%

# Performance "rules":
# 1. Avoid loops
# 2. Vectorize
# 3. Avoid array-copies and use views
