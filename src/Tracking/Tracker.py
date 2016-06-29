'''
Created on 15 mai 2016

@author: Emmanuel
'''

import cv2

class Tracker(object):
    '''
    classdocs
    '''


    def __init__(self, name, number, contour):
        '''
        Constructor
        '''
        self.name = name
        self.number = number
        self.contour = contour
        
    def boudings(self):
        return cv2.boundingRect(self.contour)