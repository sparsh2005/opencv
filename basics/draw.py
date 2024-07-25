import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') #uint8 is the datatype of an image, shape is height,width and number of color channels
cv.imshow('Blank', blank)

#1. paint the image a certain color
blank[200:300 , 300:400] = 0,0,255 
cv.imshow('Green', blank)

#2. draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2 , blank.shape[0]//2), (0,250,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank) 

#3. draw a circle
cv.circle(blank, (blank.shape[1]//2 , blank.shape[0]//2), 40 ,(0,0,255), thickness=-1)
cv.imshow('Circle', blank)

#4. draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

#5. write text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)