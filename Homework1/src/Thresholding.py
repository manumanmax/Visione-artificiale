'''
Created on 12 march 2016

@author: Emmanuel
'''


#import numpy as np
import cv2
from matplotlib import pyplot as plt
from pylab import *
from matplotlib.widgets import Slider

img = cv2.imread('../resources/test.jpg',cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img],[0],None,[256],[0,256])

fig1 = plt.figure()
plt.subplot(122)
plt.hist(img.ravel(),256,[0,256]);
plt.subplot(121)
plt.imshow(img,cmap = cm.Greys_r)


# figure 2
fig2 = plt.figure()
threshold = 127
ret,thresh1 = cv2.threshold(img,threshold,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,threshold,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,threshold,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,threshold,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,threshold,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
imshows = []


sColor = 'lightgoldenrodyellow'
sAxes = axes([0.25, 0.02, 0.5, 0.05], axisbg=sColor)
subplots_adjust(left=0.25, bottom=0.25)
thresholdSliderValue = Slider(sAxes, 'Threshold', 0, 255, valinit=threshold)

for i in xrange(6):
    plt.subplot(2,3,i+1)
    imshows.append(plt.imshow(images[i],'gray'))
    plt.title(titles[i])

def update(val):
    global threshold
    global images
    global imshows
    if abs(thresholdSliderValue.val) != threshold:
        threshold = thresholdSliderValue.val
        ret,images[1] = cv2.threshold(img,threshold,255,cv2.THRESH_BINARY)
        ret,images[2] = cv2.threshold(img,threshold,255,cv2.THRESH_BINARY_INV)
        ret,images[3] = cv2.threshold(img,threshold,255,cv2.THRESH_TRUNC)
        ret,images[4] = cv2.threshold(img,threshold,255,cv2.THRESH_TOZERO)
        ret,images[5] = cv2.threshold(img,threshold,255,cv2.THRESH_TOZERO_INV)
        for i in xrange(5):
            imshows[i+1].set_data(images[i+1])
        draw()
        print threshold
thresholdSliderValue.on_changed(update)


plt.show()

