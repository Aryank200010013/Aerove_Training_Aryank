import numpy as np
import cv2

k=np.ones((5,5),np.float32)/25

img = cv2.imread('T.jpg',0)

lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))



sm1=cv2.filter2D(lap,-1,k)

cv2.imshow('window',img)
cv2.imshow('window1',lap)
#cv2.imshow('window2',sm1)

cv2.waitKey(32000)



