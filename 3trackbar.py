import cv2
import numpy as np

def empty_function(x):
	return None
img=np.zeros((256,256,3),np.uint8)
cv2.namedWindow('window')


cv2.createTrackbar('R','window',0,255,empty_function)
cv2.createTrackbar('G','window',0,255,empty_function)
cv2.createTrackbar('B','window',0,255,empty_function)
while(1):
	cv2.imshow('window',img)
	k= cv2.waitKey(1) & 0xFF
	if k==ord('q'):
		break
	r=cv2.getTrackbarPos('R','window')
	g=cv2.getTrackbarPos('G','window')
	b=cv2.getTrackbarPos('B','window')
	img[:,:]=[b,g,r]

cv2.destroyAllWindows()
