'''
2.2 Viewing videos from files and saving
'''
import cv2

# Capturing video from a file
cap = cv2.VideoCapture('test_video.avi')

# Creating a VideoWriter object for saving
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')  # code for video-codec
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # fps and res

while cap.isOpened():
    ret, frame = cap.read()  # ret = return value (True, False) (If capturing)
    if ret:
        # Flip frame vertically if captured
        frame = cv2.flip(frame, 0)  # axis == 0

        # Write flipped frame to out files
        out.write(frame)

        # Show the flipped video
        cv2.imshow('video frame', frame)
        if cv2.waitKey ==  ord('q'):
            break

cap.release()
# End writing to output files
out.release()
cv2.destroyAllWindows()
