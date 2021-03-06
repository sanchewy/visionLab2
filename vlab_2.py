# Vision Lab 2	   Keinan Balsam

#Define imports
import cv2
import numpy as np

#Define numpy arrays for min/max 
aMin = np.array([0,0,0])
aMax = np.array([255,255,255])

#This value will be automatically inserted between the min/max values.
threshold = 30

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
cv2.createTrackbar('red_min', 'Sliders', 0, 255, change_red_min)
cv2.createTrackbar('red_max', 'Sliders', 0, 255, change_red_max)
cv2.createTrackbar('green_min', 'Sliders', 0, 255, change_green_min)
cv2.createTrackbar('green_max', 'Sliders', 0, 255, change_green_max)
cv2.createTrackbar('blue_min', 'Sliders', 0, 255, change_blue_min)
cv2.createTrackbar('blue_max', 'Sliders', 0, 255, change_blue_max)

#Function sets sliders to left click location
def get_mouse(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		px = hsv[y ,x]
		print(px)
		cv2.setTrackbarPos('red_min','Sliders',px[0]-30 if (px[0]-30)>0 else 0)
		cv2.setTrackbarPos('red_max','Sliders',px[0]+30 if (px[0]+30)<255 else 255)
		cv2.setTrackbarPos('green_min','Sliders',px[1]-30 if (px[1]-30)>0 else 0)
		cv2.setTrackbarPos('green_max','Sliders',px[1]+30 if (px[1]+30)<255 else 255)
		cv2.setTrackbarPos('blue_min','Sliders',px[2]-30 if (px[2]-30)>0 else 0)
		cv2.setTrackbarPos('blue_max','Sliders',px[2]+30 if (px[2]+30)<255 else 255)
		
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

	#Erode bw
	kernel = np.ones((3,3),np.uint8)
	bw = cv2.erode(bw,kernel,iterations =1)

	#Dialate bw
	dilation = cv2.dilate(img,kernel,iterations =1)
	cv2.imshow('Tracker', bw)
	
	#Exit on keyboard 'q' press
	k = cv2.waitKey(33)
	if k == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
