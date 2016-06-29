'''
Created on 10 mai 2016

@author: Emmanuel
'''
import cv2

def frame_size(obj1,obj2): 
    # get the indice of likeness of between two contours object with respect to the frame size
    x1,y1,w1,h1 = cv2.boundingRect(obj1)
    x2,y2,w2,h2 = cv2.boundingRect(obj2)
    
    area1 = w1*h1
    area2 = w2*h2
    
    if(area1 > area2):
        return float(area2)/float(area1)
    else:
        return float(area1)/float(area2)
    
    