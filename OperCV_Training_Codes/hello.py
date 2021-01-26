#import numpy as np
import cv2

img = cv2.imread('shot.jpg',0)

cv2.imshow('window',img)
cv2.waitKey(6000)

cv2.imwrite('shot_copy.jpg',img)