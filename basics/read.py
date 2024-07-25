import cv2 as cv

img = cv.imread('Photos/cat.jpg')#reading image

cv.imshow('Cat', img)#diplaying image with name and its matrices (img)

#reading videos
capture=cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'): #shuts down when u press d key
        break

capture.release()
cv.destroyAllWindows()