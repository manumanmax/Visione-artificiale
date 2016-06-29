# import the necessary packages
import cv2
 
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False
objects = []
image_number = 1
lineFormat = 'img/img'
currentImage = 'img1.jpg'
 
def click_and_crop(event, x, y, flags, param):
    global image_number
    global objects
    # grab references to the global variables
    global refPt, cropping
 
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
 
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False
        
        x,y = refPt[0]
        x1,y1 = refPt[1]
        w = x1 - x
        h = y1 - y
        objects.append([x,y,w,h])
        print objects
        # draw a rectangle around the region of interest
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)

 
# load the image, clone it, and setup the mouse callback function
image = cv2.imread('images/training_set/img' + str(image_number) + '.jpg',1)
file = open('info.dat','a')
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
 
# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF
 
    # if the 'r' key is pressed, reset the cropping region
    if key == ord("n"):
        line =  lineFormat + str(image_number) + '.jpg ' + str(len(objects))
        for bound in objects:
            line = line  + ' ' + str(bound[0]) + ' ' + str(bound[1]) + ' ' + str(bound[2]) + ' ' + str(bound[3])
        
        line = line + '\n'
        file.write(line)
        image_number = image_number + 1
        
        
        objects = []
        image = cv2.imread('images/training_set/img' + str(image_number) + '.jpg',1)
        
    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break
    elif key == ord("r"):
        objects = []
        image = cv2.imread('images/training_set/img' + str(image_number) + '.jpg',1)
 
 
 
# close all open windows
cv2.destroyAllWindows()