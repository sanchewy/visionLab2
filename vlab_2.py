# Vision Lab 2	   Keinan Balsam
def change_slider(value):
    pass
	#print("do something")

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
cv2.namedWindow("Sliders", cv2.WINDOW_NORMAL)
cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
#cap.set(cap, cv2.CV_CAP_PROP_FRAME_WIDTH, 480)
#cap.set(cap, cv2.CV_CAP_PROP_FRAME_HEIGHT, 640)

cv2.createTrackbar("change", "Sliders", 255, 255, change_slider)
while True:
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	cv2.imshow("Frame", hsv)
	
	status, img = cap.read()
	cv2.imshow("Video", img)
	cv2.resizeWindow("Video", 600, 600)
	cv2.resizeWindow("Frame", 600, 600)
	cv2.resizeWindow("Sliders", 600, 600)
	k = cv2.waitKey(33)
	if k == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
