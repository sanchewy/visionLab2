# Computer Vision Lab 2 Part 2 Keinan Balsam

#Define imports
import cv2
import numpy as np

#Define video capture
cap = cv2.VideoCapture(0)
_,img = cap.read()
avg = np.float32(img)

#Define main funciton runloop
while True:
	#Set up BRG live video
	_,img = cap.read()
	cv2.imshow('Origional', img)
	
	#Now take accumulateWeighted running average
	res = cv2.accumulateWeighted(img, avg, .1)
	
	#ConvertScaleAbs back to 8 bit
	res = cv2.convertScaleAbs(res)
	
	#Take absolute difference
	res = cv2.absdiff(res, img)
	cv2.imshow('ABSDifference', res)
	
	#Turn grayscale
	res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
	
	#Threshold low
	_,thresh1 = cv2.threshold(res.copy(),20, 255, cv2.THRESH_BINARY)
	cv2.imshow('Threshold low', thresh1)
	
	#Now blur
	thresh1 = cv2.GaussianBlur(thresh1, (21, 21), 0)
	
	#Threshold high
	_,thresh2 = cv2.threshold(thresh1, 100, 255, cv2.THRESH_BINARY)
	cv2.imshow('Threshold high', thresh2)
	
	#Find contours
	_,cnts,_ = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cnts = sorted(cnts, key = cv2.contourArea, reverse = False)
	screenCnt = None
	imgcont = img.copy()
	if len(cnts) > 0:
		cv2.drawContours(imgcont, cnts, -1, (0,255,0),3)
	#for c in cnts:
		#peri = cv2.arcLength(c, True)
		#approx = cv2.approxPolyDP(c, 0.02 * peri, True)
		#cv2.drawContours(imgcont, c, 0, (0,255,0), 3)
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