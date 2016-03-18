'''
Created on 13 march 2016

@author: Emmanuel
'''
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../resources/equalization.jpg',cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img],[0],None,[256],[0,256])

# getting started with the thresholding base
fig1 = plt.figure()
plt.subplot(222)
plt.hist(img.ravel(),256,[0,256]);
plt.subplot(221)
plt.imshow(img, 'gray')

# equalization of the image
img = cv2.equalizeHist(img)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.subplot(224)
plt.plot(hist, 'black');
plt.subplot(223)
plt.imshow(img, 'gray')


plt.show()