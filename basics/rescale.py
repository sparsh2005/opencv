import cv2 as cv

#img= cv.imread('Photos/cat.jpg')
#cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75): #frame to be resized and scale default value
    #rescale will work for images, video, and live video
    width= int (frame.shape[1] * scale) #shape[1] refers to the width of the image
    height= int (frame.shape[0] * scale) #shape[0] refers to the height of the image
    dimensions= (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    #Interpolation is a method of estimating values between two known values. In image processing, it’s used when resizing images to estimate pixel values for the resized image.
    #cv.INTER_AREA is one of the interpolation methods provided by OpenCV. It is recommended for shrinking images because it uses pixel area relation. It’s a resampling technique that can handle resizing by averaging pixel values, leading to a smoother and more accurate resized image.
    
#resized_image = rescaleFrame(img)
#cv.imshow('Image', resized_image)

def changeRes(width, height):
    #will work only for live video
    capture.set(3, width)
    capture.set(4, height)


#reading videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): #shuts down when u press d key
        break

capture.release()
cv.destroyAllWindows()