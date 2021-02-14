import numpy as np
import cv2

cap=cv2.VideoCapture(0)


while (True):
    ret, frame = cap.read()

    #g_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    B=cv2.split(frame)
    zeros=np.zeros(frame.shape[:2],dtype="uint8")

    cv2.imshow('123',cv2.merge([B,zeros,zeros]))


    cv2.imshow('window',frame)
    #cv2.imshow('window2',g_frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()