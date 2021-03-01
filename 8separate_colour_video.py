import cv2
import numpy as np

vid=cv2.VideoCapture(0)
cv2.namedWindow('window')
def empty_function(x):
	return None
cv2.createTrackbar('H_low','window',0,179,empty_function)
cv2.createTrackbar('H_high','window',0,179,empty_function)
cv2.createTrackbar('S_low','window',0,255,empty_function)
cv2.createTrackbar('S_high','window',0,255,empty_function)
cv2.createTrackbar('V_low','window',0,255,empty_function)
cv2.createTrackbar('V_high','window',0,255,empty_function)
while(True):
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
	gbg,frame=vid.read()
	frame_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	h_l=cv2.getTrackbarPos('H_low','window')
	h_h=cv2.getTrackbarPos('H_high','window')
	s_l=cv2.getTrackbarPos('S_low','window')
	s_h=cv2.getTrackbarPos('S_high','window')
	v_l=cv2.getTrackbarPos('V_low','window')
	v_h=cv2.getTrackbarPos('V_high','window')

	lwr=np.array([h_l,s_l,v_l])
	upr=np.array([h_h,s_h,v_h])

	mask=cv2.inRange(frame_hsv,lwr,upr)
	frame=cv2.bitwise_and(frame,frame,mask=mask)
	cv2.imshow('window',frame)

vid.release()
cv2.destroyAllWindows()