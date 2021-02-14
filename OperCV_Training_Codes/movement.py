import numpy as np
import cv2


img = cv2.imread('T.jpg',1)

rows,cols,ch=img.shape

mat2=np.float32([[1,0,30],[0,1,-100]])
mat3=np.float32([[1,0,140],[0,1,30]])
mat4=np.float32([[1,0,-90],[0,1,-220]])
mat5=np.float32([[1,0,-230],[0,1,-260]])
mat6=np.float32([[1,0,110],[0,1,120]])


simg=cv2.resize(img,None,fx=2,fy=2)

timg2=cv2.warpAffine(img, mat2, (cols,rows))
timg3=cv2.warpAffine(img, mat3, (cols,rows))
timg4=cv2.warpAffine(img, mat4, (cols,rows))
timg5=cv2.warpAffine(timg3, mat5, (cols,rows))
timg6=cv2.warpAffine(timg5, mat6, (cols,rows))





cv2.imshow('window',img)
#cv2.imshow('window1',simg)

cv2.imshow('window2',timg2)
cv2.imshow('window3',timg3)
cv2.imshow('window4',timg4)
cv2.imshow('window5',timg5)
cv2.imshow('window6',timg6)




cv2.waitKey(32000)

cv2.destroyAllWindows()
