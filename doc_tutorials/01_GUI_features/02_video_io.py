'''
2.1 Capturing and viewing videos
'''
import numpy as np
import cv2

# Capturing video from webcam
cap = cv2.VideoCapture(0)  # 0 = device 0 = standard

while True:  # While Capturing
    # Capture video frame
    ret, frame = cap.read()  # frame = the frame that was read

    # Edit the frames here, for example convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # (frame, conversion_flag)

    # Display the frame
    cv2.imshow('video_frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        # stop when q is pressed

# Switch off webcam and close window when done
cap.release()
cv2.destroyAllWindows()
