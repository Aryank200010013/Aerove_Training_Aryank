#import numpy as np
import cv2

img = cv2.imread('shot.jpg',0)

_,th1=cv2.threshold(img,40,255,cv2.THRESH_BINARY)

cv2.imshow('window',img)
cv2.imshow('window2',th1)
cv2.waitKey(6000)

cv2.imwrite('shot_copy.jpg',img)