'''
Created on 13 mars 2016

@author: Emmanuel
'''

# Standard imports
import cv2
import numpy as np;
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
from pylab import *


# Read image
im = cv2.imread("../resources/cells.jpg", cv2.IMREAD_GRAYSCALE)
ret,im = cv2.threshold(im,180,255,cv2.THRESH_BINARY_INV)
cv2.waitKey(0)
# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200


# Filter by Area. less than treshold pixels
params.filterByArea = True
params.minArea = 200

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.8

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.5

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.5

# Create a detector with the parameters
# Create a detector with the parameters

ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else : 
    detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
fig = plt.figure()
plt.subplot(121)
img_data = plt.imshow(im_with_keypoints,'gray')

#sliders
sColor = 'lightgoldenrodyellow'
sAxes = axes([0.7, 0.7, 0.2, 0.025], axisbg=sColor)
subplots_adjust(left=0.25, bottom=0.25)
minArea = Slider(sAxes, 'minArea', 1, 1500, valinit=200)
sAxes = axes([0.7, 0.6, 0.2, 0.025], axisbg=sColor)
minCingularity = Slider(sAxes, 'minCingular', 0, 1, valinit=0.5)
sAxes = axes([0.7, 0.5, 0.2, 0.025], axisbg=sColor)
minConvexity = Slider(sAxes, 'minConvex', 0, 1, valinit=0.5)
sAxes = axes([0.7, 0.4, 0.2, 0.025], axisbg=sColor)
minInertia = Slider(sAxes, 'minInertia', 0, 1, valinit=0.5)

def update(val):
    global img_data
    global im
    global ver
    params.minArea = minArea.val
    params.minCircularity = minCingularity.val
    params.minConvexity = minConvexity.val
    params.minInertiaRatio = minInertia.val
    if int(ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector(params)
    else : 
        detector = cv2.SimpleBlobDetector_create(params)

    keypoints = detector.detect(im)
    img_data.set_data(cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS))
    draw()
    
    
minArea.on_changed(update)
minCingularity.on_changed(update)
minConvexity.on_changed(update)
minInertia.on_changed(update)
    
plt.show()

