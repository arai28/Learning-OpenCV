import cv2
import numpy as np
vid=cv2.VideoCapture(0)
flag=0

# set hsv range for required cloak colour
# get the range by taking the help of the sep_color_video.py file
upr=np.array([27,255,169])
lwr=np.array([0,205,49])

while(True):
	gbg,frame=vid.read()
	# grab background initially
	if flag==0:
		bg_img=frame
		flag=1
	else:
		# create mask using hsv for better results
		frame_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		mask=cv2.inRange(frame_hsv,lwr,upr)

		# using the mask created on video feed with the given range create the background covering of that area
		underlap=cv2.bitwise_and(bg_img,bg_img,mask=mask)

		# apply mask on frame to segment the area that is to be removed and then subtract from original frame to get rest of the image
		segmented_top=cv2.bitwise_and(frame,frame,mask=mask)
		rest=frame-segmented_top

		rslt=cv2.add(rest,underlap)
		cv2.imshow('window',rslt)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
# cv2.imshow('background',bg_img)
print(bg_img.shape)
vid.release()
cv2.destroyAllWindows()
