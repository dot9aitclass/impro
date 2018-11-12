import cv2
import numpy as np
#events=[i for i in dir(cv2) if 'EVENT' in i]
#print events
imo=cv2.imread('task4.png',1)
im=np.array(imo)
def retrgb(event,x,y,flag,param):
    if event==cv2.EVENT_FLAG_LBUTTON:
        for i in xrange(3):
            if i==0:
                print ("Blue",imo[y][x][i])
            elif i==1:
                print ("Green", imo[y][x][i])
            elif i==2:
                print ("Red", imo[y][x][i])
                print ("************* \n")
cv2.imshow('win',imo)
cv2.setMouseCallback("win",retrgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
