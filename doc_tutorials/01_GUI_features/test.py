import cv2

im = cv2.imread("/home/nils/Pictures/Selection_008.bmp")

cv2.imshow("test", im)
k = cv2.waitKey(0)
if k == ord('q'):
    cv2.destroyAllWindows()
