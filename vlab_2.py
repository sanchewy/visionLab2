# Vision Lab 2	   Keinan Balsam

#Define imports
import cv2
import numpy as np

#Define numpy arrays for min/max 
aMin = np.array([0,0,0])
aMax = np.array([255,255,255])

#Define slider action listeners
def change_red_min(value):
	aMin[0] = value
def change_red_max(value):
	aMax[0] = value
def change_green_min(value):
	aMin[1] = value
def change_green_max(value):
	aMax[1] = value
def change_blue_min(value):
	aMin[2] = value
def change_blue_max(value):
	aMax[2] = value

#Define video capture
cap = cv2.VideoCapture(0)

#Define windows
cv2.namedWindow('Video', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('Sliders', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('HSV', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('Tracker', cv2.WINDOW_AUTOSIZE)

#Define sliders
cv2.createTrackbar('red_min', 'Sliders', 255, 255, change_red_min)
cv2.createTrackbar('red_max', 'Sliders', 255, 255, change_red_max)
cv2.createTrackbar('green_min', 'Sliders', 255, 255, change_green_min)
cv2.createTrackbar('green_max', 'Sliders', 255, 255, change_green_max)
cv2.createTrackbar('blue_min', 'Sliders', 255, 255, change_blue_min)
cv2.createTrackbar('blue_max', 'Sliders', 255, 255, change_blue_max)

#Function sets sliders to left click location
def get_mouse(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		px = hsv[y ,x]
		cv2.setTrackbarPos('red_min','Sliders',px[0])
		cv2.setTrackbarPos('red_max','Sliders',px[0])
		cv2.setTrackbarPos('green_min','Sliders',px[1])
		cv2.setTrackbarPos('green_max','Sliders',px[1])
		cv2.setTrackbarPos('blue_min','Sliders',px[2])
		cv2.setTrackbarPos('blue_max','Sliders',px[2])
		
#Define mouse click callback method
cv2.setMouseCallback('HSV',get_mouse)

#Define main run loop
while True:
	#Set up hsv and start live video
	ret1, hsv = cap.read()
	hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
	cv2.imshow('HSV', hsv)
	
	#Set up BRG live video
	status, img = cap.read()
	cv2.imshow('Video', img)
	
	#Use inRange to find values between aMin and aMax, print to grayscale
	bw = cv2.inRange(hsv, aMin, aMax)
	cv2.imshow('Tracker', bw)
	
	#Exit on 'q' press
	k = cv2.waitKey(33)
	if k == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
