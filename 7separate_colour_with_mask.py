import cv2
import numpy as np

img=cv2.imread('fruit_basket',1)

cv2.namedWindow('window')
def empty_function(x):
	return None
cv2.createTrackbar('R_low','window',0,255,empty_function)
cv2.createTrackbar('R_high','window',0,255,empty_function)
cv2.createTrackbar('G_low','window',0,255,empty_function)
cv2.createTrackbar('G_high','window',0,255,empty_function)
cv2.createTrackbar('B_low','window',0,255,empty_function)
cv2.createTrackbar('B_high','window',0,255,empty_function)
while(1):

	
	r_l=cv2.getTrackbarPos('R_low','window')
	r_h=cv2.getTrackbarPos('R_high','window')
	g_l=cv2.getTrackbarPos('G_low','window')
	g_h=cv2.getTrackbarPos('G_high','window')
	b_l=cv2.getTrackbarPos('B_low','window')
	b_h=cv2.getTrackbarPos('B_high','window')

	lwr=np.array([b_l,g_l,r_l])
	upr=np.array([b_h,g_h,r_h])

	mask=cv2.inRange(img,lwr,upr)
	img2=cv2.bitwise_and(img,img,mask=mask)

	cv2.imshow('window',img2)
	k=cv2.waitKey(1) & 0xFF
	if k==ord('q'):
		break
cv2.destroyAllWindows()
