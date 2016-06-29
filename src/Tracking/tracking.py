'''
Created on 4 mai 2016

@author: Emmanuel
'''

import numpy as np
import time
import cv2
import likeness_algorithm as la
import functions as f



def main():
    cap = cv2.VideoCapture(0)
    contours = []
    names = dict()
    
    background,background_gray = f.getBackground(cap)
    
    while(len(contours) <= 0):
        tracking, contours, frame2 = f.scan(background_gray,cap) # get the contours of the moving objects
        
    objs = contours
    
    while(True):            
        tracking, contours, frame2 = f.scan(background_gray,cap) # get the contours of the moving objects
        objs,names= f.track(contours,objs,names)
        print objs
        cv2.imshow('blobs',frame2)
        for i in range(1,3):
            ret, frame_t = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
            cv2.destroyAllWindows()
            break
    

if __name__ == "__main__":
    main()
