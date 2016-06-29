'''
Created on 15 mai 2016

@author: Emmanuel
'''
import cv2
import time
import Tracker
import likeness_algorithm as la
import numpy as np

def load_all():
    back = cv2.imread("Resources/background.png", cv2.IMREAD_ANYCOLOR)
    f1 = cv2.imread("Resources/frame1.png", cv2.IMREAD_ANYCOLOR)
    f2 = cv2.imread("Resources/frame2.png", cv2.IMREAD_ANYCOLOR)
    return back,f1,f2

def suppress_background(background, frame_t):
    background_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
    frame_t_gray = cv2.cvtColor(frame_t, cv2.COLOR_BGR2GRAY) 
    frame_t_gray = frame_t
    frame_t_gray = cv2.cvtColor(frame_t, cv2.COLOR_BGR2GRAY)
    
    cv2.absdiff(background_gray, frame_t_gray, frame_t_gray)
    ret,frame_t_gray = cv2.threshold(frame_t_gray,35,255,cv2.THRESH_BINARY)
    
    #post treatment
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    erosion = cv2.erode(frame_t_gray,kernel, iterations=3)
    dilatation = cv2.dilate(erosion,kernel, iterations=10)
    
    return dilatation   

def get_array(objs, contours):
    cols = len(objs)
    rows = len(contours)
    
    array = np.zeros(cols*rows).reshape(rows, cols)
    i = 0
    j = 0
    imax = 0
    jmax = 0
    max = 0

    for obj in objs:
        for cnt in contours:
            val = la.frame_size(cnt, obj.contour)
            array[i][j] = val
            if val > max:
                imax = i
                jmax = j
                max = val
            j = j+1
        i = i+1
        j = 0
    
    return array, imax, jmax


def findMax(associations):
    max = -1
    imax = 0
    jmax = 0
    i = 0
    j = 0 
    for line in associations:
        for cell in line:
            if cell > max: 
                max = cell
                jmax = j
                imax = i
            j = j+1
        i = i+1
                
    return jmax,imax
def drawTrack(img, obj):
    x,y,w,h = cv2.boundingRect(obj.contour)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),5)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,obj.name + " " + str(obj.number),(x,y), font, 1,(0,0,0),2)
    
    
def main():
    objs_precedent = []
    objs_now = []
    i = 0
    
    background, frame1, frame2 = load_all();
    image_without_background = suppress_background(background, frame1) # frame 2 corresponds to the last frame

    imgC_t_minus_1, contours, hierarchy = cv2.findContours(image_without_background,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        objs_precedent.append(Tracker.Tracker("nameuh", i, c))
        i = i+1 
        
    image_without_background = suppress_background(background, frame2)
    imgC_t, contours, hierarchy = cv2.findContours(image_without_background,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow("without back j+1", image_without_background)
    association_array, index_obj, index_contour = get_array(objs_precedent, contours)
    
    if(association_array[index_obj][index_contour] > 0.7): #if it's a valid match
        track = Tracker.Tracker("manu",objs_precedent[index_obj].number,contours[index_contour])
        drawTrack(frame2,track)
        objs_now.append(track)

    #suppression of the values in the table and the lists
    association_array = np.delete(association_array,index_obj,0)
    association_array = np.delete(association_array,index_contour,1)
    objs_precedent.remove(objs_precedent[index_obj])
    contours.remove(contours[index_contour])
    
    
    index_obj, index_contour = findMax(association_array)
    print index_obj, index_contour, association_array[index_obj][index_contour]
    if(association_array[index_obj][index_contour] > 0.7): #if it's a valid match
        track = Tracker.Tracker("manu",objs_precedent[index_obj].number,contours[index_contour])
        drawTrack(frame2,track)
        
    cv2.imshow("rect", frame2)
        
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    
if __name__ == "__main__":
    main()
