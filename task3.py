import PIL as image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2HLS_FULL)

    cv2.imshow("frame",gray)
    if cv2.waitKey(30)==27:
        break
cv2.destroyAllWindows()
cap.release()