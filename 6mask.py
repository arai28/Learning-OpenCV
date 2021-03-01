import cv2
import numpy as np

img=cv2.imread('fruit_basket',1)
# img2=cv2.imread('fruit_basket',1)

cv2.namedWindow('window')
def empty_function(x):
	return None

lower_yellow=np.array([0,0,255])
upper_yellow=np.array([255,255,255])

mask=cv2.inRange(img,lower_yellow,upper_yellow)
sep_yellow=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("window",sep_yellow)
cv2.waitKey(0)
cv2.destroyAllWindows()
