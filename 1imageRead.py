import cv2

img=cv2.imread('fruit_basket',1)
cv2.imshow('basket',img)
cv2.waitKey(0)
cv2.destroyAllWindows()