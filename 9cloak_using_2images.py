import cv2
import numpy as np

# top image is fruit basket
img=cv2.imread("fruit_basket",1)
upr=np.array([55,56,237])
lwr=np.array([24,13,112])

# taking underlying layer to be a red coloured image...ie the part in the range of pixel values will be swapped by this red image
# red_layer=np.zeros((img.shape[0],img.shape[1],3),dtype='uint8')
# red_layer[:,:]=(0,0,255)


# underlying image ie the part in the range of pixel values in the original image will be swapped by this image
under_img=cv2.imread('lenna.png',1)
under_img=cv2.resize(under_img,(img.shape[1],img.shape[0]))
# print(under_img.shape)
# print(img.shape)
# print(under_img.dtype)


# mask for seperating out the area of given colour in the top image which is to be replaced by bottom image
mask=cv2.inRange(img,lwr,upr)

# apply mask on underlying layer(lenna here) so we have the part of this layer that will be required
underlap=cv2.bitwise_and(under_img,under_img,mask=mask)

# getting the part of top image which wont be replaced
# first apply mask on top image nd then subtract from original form of it to get the required area
segmented=cv2.bitwise_and(img,img,mask=mask)
rest=img-segmented

# just add the 2 images to get the result
rslt=cv2.add(rest,underlap)



# rslt=cv2.bitwise_and(img,img,mask=mask)
# cv2.imshow('mask',mask)
# cv2.imshow('underlap',underlap)
# cv2.imshow('rest',rest)
# cv2.imshow('segmented',segmented)
cv2.imshow('rslt',rslt)
# cv2.imshow('top_img',img)
# cv2.imshow('under_img',under_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(type(mask))

# print(mask.shape)
# print(img.dtype)
# print(mask.dtype)
# print(rest.dtype)
# print(underlap.dtype)
# print(red_layer.dtype)
