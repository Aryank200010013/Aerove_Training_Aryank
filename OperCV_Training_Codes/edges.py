#import numpy as np
import cv2

img = cv2.imread('shapes.jpg',0)


_,th1=cv2.threshold(img,240,255,cv2.THRESH_BINARY)


cv2.imshow('window',th1)




cv2.waitKey(32000)

