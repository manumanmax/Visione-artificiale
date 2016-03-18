'''
Created on 18 march 2016

@author: Emmanuel
'''

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    #get the images
    ret, frame = cap.read()
    for i in range(0,2) :
        ret, frame2 = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,gray = cv2.threshold(gray,170,255,cv2.THRESH_BINARY_INV)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    ret,gray2 = cv2.threshold(gray2,127,255,cv2.THRESH_BINARY)
    #substract the images
    sub = gray - gray2
    #applying sobel
    sobel = cv2.Sobel(sub,cv2.CV_64F,1,0,ksize=5)
    cv2.imshow('sobel',sobel)
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.destroyAllWindows()
        break


# Display the resulting frame
#cv2.imshow('frame1 without thresh',frame)
#cv2.imshow('frame1',gray)
#cv2.imshow('frame2',gray2)
#cv2.imshow('sub',sub)
# When everything done, release the capture
