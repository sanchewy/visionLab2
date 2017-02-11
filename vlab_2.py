# Vision Lab 2	   Keinan Balsam
def change_slider(value):
    pass
	#print(do something)

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow('Video', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('Sliders', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
#cv2.resizeWindow('Video', 600, 600)
#cv2.resizeWindow('Frame', 600, 600)
#cv2.resizeWindow('Sliders', 600, 600)
cv2.createTrackbar('Red', 'Sliders', 255, 255, change_slider)
cv2.createTrackbar('Green', 'Sliders', 255, 255, change_slider)
cv2.createTrackbar('Blue', 'Sliders', 255, 255, change_slider)

def get_mouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        px = frame[y ,x]
        print(px)
        
cv2.setMouseCallback('Frame',get_mouse)

while True:
	ret, frame = cap.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	cv2.imshow('Frame', frame)
	status, img = cap.read()
	cv2.imshow('Video', img)
	k = cv2.waitKey(33)
	if k == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
