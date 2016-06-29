'''
Created on 15 mai 2016

@author: Emmanuel
'''
import numpy as np
import time
import cv2
import likeness_algorithm as la

def associate(blobs_t,objs_prev):
    mat = []

    for blob in blobs_t:
        line = []
        for obj in objs_prev:
            line.append([la.frame_size(blob, obj),blob])
        mat.append(line)
    return mat

def findMax(associations):
    max = -1
    cell_max = 0
    for line in associations:
        for cell in line:
            if cell[0] > max: 
                max, cell_max = cell
                
    return max, cell_max
                
                
def track(blobs_t,objs_prev,names):
    max_threshold = 0.7
    min_threshold = 0.3
    
    objs_t = []
    associations = associate(blobs_t,objs_prev)
    max, obj = findMax(associations)
    
    objs_t.append(obj)

    return objs_t, names

def getBackground(cap):
    for i in range(1,6):
        print("capturing the background in ", i)
        ret, frame2 = cap.read()
    ret, background = cap.read()
    background_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
    return background, background_gray

def scan(background_gray,cap):
    for i in range(0,3) :
        ret, frame2 = cap.read()
          
    tracking = frame2
    tracking = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    cv2.absdiff(background_gray, tracking, tracking)
    ret,tracking = cv2.threshold(tracking,35,255,cv2.THRESH_BINARY)
    
    #post treatment
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    erosion = cv2.erode(tracking,kernel, iterations=3)
    dilatation = cv2.dilate(erosion,kernel, iterations=10)
    
    tracking = dilatation
    #blob detection 
    tracking_c =tracking
    tracking_c, contours, hierarchy = cv2.findContours(tracking_c,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(frame2,(x,y),(x+w,y+h),(255,255,0),5)
    frameBlobs = frame2
    return tracking, contours,frameBlobs

