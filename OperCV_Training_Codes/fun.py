import numpy as np
#'capture.mp4'
import cv2

cap=cv2.VideoCapture(0)
#fourcc=cv2.VideoWriter_fourcc(*'XVID')
#out=cv2.VideoWriter('output.avi',fourcc,30.0,(640,480))

while (True):
    ret ,frame = cap.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _,th=cv2.threshold(frame,60,255,cv2.THRESH_BINARY_INV)
    _,th1=cv2.threshold(gray,60,255,cv2.THRESH_BINARY_INV)
    _,th2=cv2.threshold(frame,160,255,cv2.THRESH_TOZERO_INV)

    #out.write(frame)
    cv2.imshow('window',frame)
    #cv2.imshow('window2',gray)
    cv2.imshow('window3',th)
    cv2.imshow('window4',th1)
    cv2.imshow('window5',th2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

cap.release()
out.release()
cv2.destroyAllWindows()