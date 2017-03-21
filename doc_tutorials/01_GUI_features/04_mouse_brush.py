'''
2. Using the mouse as a paintbrush
'''
import cv2
import numpy as np

# Setup
drawing = False  # true if mouse is pressed
mode = True  # Draws rectangles, press 'm' to draw circles
ix, iy = -1, 1  # Inital coordinates

# Creating a mouse callback function, that gets executed when an event happens
def draw_circle(event, x, y, flags, param):
    global drawing, mode, ix, iy

    # Event bindings
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse-button down
        drawing = True  # Start drawing
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:  # Moving the mouse
        if drawing:
            if mode:
                cv2.rectangle(img,  (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (ix, iy), abs(x - ix), (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:  # Left mouse-button up
        drawing = False
        if mode:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)


# Creating a black image, a window and binding t he function to the window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # 27 == 'ESC'
        break
    elif k == ord('m'):
        mode = not mode

cv2.destroyAllWindows()
