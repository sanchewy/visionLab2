# Computer Vision Lab 2 Part 2 Keinan Balsam

#Define imports
import cv2
import numpy as np

#Define video capture
cap = cv2.VideoCapture(0)

#Define windows
cv2.namedWindow('Video', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('Equalize/Blur/32Bit', cv2.WINDOW_AUTOSIZE)

#Define main funciton runloop
while True:
	#Set up BRG live video
	status, img = cap.read()
	img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
	cv2.imshow('Video', img)
	
	#Create new frame and brighten
	imgyuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
	imgyuv[:,:,0] = cv2.equalizeHist(imgyuv[:,:,0])
	equalize = cv2.cvtColor(imgyuv, cv2.COLOR_YUV2BGR)
	
	#Now blur equalize and turn 32 bit
	kernel = np.ones((5,5),np.float32)/25
	equalize = cv2.filter2D(equalize,-1,kernel)
	cv2.imshow('Equalize', equalize)
	
	#Exit on keyboard 'q' press
	k = cv2.waitKey(33)
	if k == ord('q'):
		break
		
#Define exit strategy
cap.release()
cv2.destroyAllWindows()