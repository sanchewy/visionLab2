# Computer Vision Lab 2 Part 2 Keinan Balsam

#Define imports
import cv2
import numpy as np

#Define video capture
cap = cv2.VideoCapture(0)

#Define windows
cv2.namedWindow('Video', cv2.WINDOW_AUTOSIZE)

#Define main funciton runloop
while True:
    #Set up BRG live video
	status, img = cap.read()
	cv2.imshow('Video', img)
    
    #Exit on keyboard 'q' press
	k = cv2.waitKey(33)
	if k == ord('q'):
		break
        
#Define exit strategy
cap.release()
cv2.destroyAllWindows()