import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur 

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #kernel size can only be odd
cv.imshow('Blur', blur)

#edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

#dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

#eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)#resizes regardless of aspect ratio
cv.imshow('Resized', resized)

#cropping
cropped= img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)