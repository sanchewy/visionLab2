# Computer Vision Lab 2 Part 2 Keinan Balsam

#Define imports
import cv2
import numpy as np
import time

#Define video capture
cap = cv2.VideoCapture(0)
_,img = cap.read()
avg = np.float32(img)

#Define main funciton runloop
while True:

	#Set up BRG live video
	_,img = cap.read()
	while img is None:
		print("No input is being received from your webcam")
		time.sleep(1)
	cv2.imshow('Origional', img)
	
	#Now take accumulateWeighted running average .1 = refresh rate
	res = cv2.accumulateWeighted(img, avg, .5)
	
	#ConvertScaleAbs back to 8 bit
	res = cv2.convertScaleAbs(res)
	
	#Take absolute difference
	res = cv2.absdiff(res, img)
	cv2.imshow('ABSDifference', res)
	
	#Turn grayscale
	res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
	
	#Threshold low
	_,thresh1 = cv2.threshold(res.copy(),20, 255, cv2.THRESH_BINARY)
	#cv2.imshow('Threshold low', thresh1)
	
	#Now blur
	thresh1 = cv2.GaussianBlur(thresh1, (21, 21), 0)
	
	#Threshold high
	_,thresh2 = cv2.threshold(thresh1, 100, 255, cv2.THRESH_BINARY)
	#cv2.imshow('Threshold high', thresh2)
	
	#Erode the bw threshold image
	kernel = np.ones((10,10),np.uint8)
	thresh2 = cv2.erode(thresh2,kernel,iterations =1)
	cv2.imshow('Erode', thresh2)
	
	#Dilate the bw threhold image
	kernel = np.ones((50,50),np.uint8)
	thresh2 = cv2.dilate(thresh2,kernel,iterations =1)
	cv2.imshow('Dilate', thresh2)
	
	#Find contours
	_,cnts,_ = cv2.findContours(thresh2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	#cnts = sorted(cnts, key = cv2.contourArea, reverse = False)[0]
	imgcont = img.copy()
	#Draw rectangles around any existing contours
	if len(cnts) > 0:
		for cnts1 in cnts:
				rect = cv2.boundingRect(cnts1)
				p1 = (rect[0], rect[1])
				p2 = (rect[0] + rect[2], rect[1] + rect[3])
				if((rect[2]*rect[3]) > 9000):
					cv2.rectangle(imgcont, p1, p2, (0,255,0),1)
	cv2.imshow("Contours", imgcont)
	
	#Create new frame and brighten
	imgyuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
	imgyuv[:,:,0] = cv2.equalizeHist(imgyuv[:,:,0])
	equalize = cv2.cvtColor(imgyuv, cv2.COLOR_YUV2BGR)
	
	#Exit on keyboard 'q' press
	k = cv2.waitKey(33)
	if k == ord('q'):
		break
		
#Define exit strategy
cap.release()
cv2.destroyAllWindows()