import numpy as np
import cv2

cap=cv2.VideoCapture(0)


while (True):
    ret, frame = cap.read()

    lap=cv2.Laplacian(frame,cv2.CV_64F,ksize=3)
    lap=np.uint8(np.absolute(lap))

    #g_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('window',frame)
    #cv2.imshow('window2',g_frame)
    cv2.imshow('window3',lap)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()