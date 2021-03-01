import cv2
import numpy as np

img=cv2.imread('fruit_basket',1)
img2=cv2.imread('fruit_basket',1)

cv2.namedWindow('window')
def empty_function(x):
	return None

cv2.createTrackbar('R_low','window',0,255,empty_function)
cv2.createTrackbar('R_high','window',0,255,empty_function)
cv2.createTrackbar('G_low','window',0,255,empty_function)
cv2.createTrackbar('G_high','window',0,255,empty_function)
cv2.createTrackbar('B_low','window',0,255,empty_function)
cv2.createTrackbar('B_high','window',0,255,empty_function)


rows,cols,_=img2.shape
while(1):

	cv2.imshow('window',img2)
	k=cv2.waitKey(1) & 0xFF
	if k==ord('q'):
		break
	r_l=cv2.getTrackbarPos('R_low','window')
	r_h=cv2.getTrackbarPos('R_high','window')
	g_l=cv2.getTrackbarPos('G_low','window')
	g_h=cv2.getTrackbarPos('G_high','window')
	b_l=cv2.getTrackbarPos('B_low','window')
	b_h=cv2.getTrackbarPos('B_high','window')

	for i in range(rows):
		for j in range(cols):
			if ((img.item(i,j,0)>b_h) or (img.item(i,j,0)<b_l)):
				img2[i,j]=[0,0,0]

			elif img.item(i,j,1)>g_h or img.item(i,j,1)<g_l:
				img2[i,j]=[0,0,0]
			elif img.item(i,j,2)>r_h or img.item(i,j,2)<r_l:
				img2[i,j]=[0,0,0]
			else:
				img2[i,j]=img[i,j]
	
cv2.destroyAllWindows()


