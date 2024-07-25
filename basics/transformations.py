import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')

cv.imshow('Group', img)

#translation
def translate(img, x, y):
    transMat= np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, 100, 100) #shifts by x and y pixels
cv.imshow('Translated', translated)

#rotation
def rotate(img, angle, rotPoint=None):
    (height,width)= img.shape[:2]#shape of first 2 values

    if rotPoint is None:
        rotPoint = (width//2, height//2) #if rotation point is not given then assume rotation point is the center of the image

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, 45) #black triangles created by default during previous rotation
cv.imshow('Rotated rotated', rotated_rotated)

#resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

#cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)