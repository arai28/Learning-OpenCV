import cv2

img=cv2.imread('fruit_basket',1)
rows,cols,channels=img.shape

for i in range(rows):
	for j in range(cols):
		if all(img[i,j]==[51, 255, 255]):
			continue
		else:
			img[i,j]=[0, 0, 0]


cv2.imshow('yellow',img)
cv2.waitKey(0)
cv2.destroyAllWindows()