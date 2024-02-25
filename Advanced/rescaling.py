import cv2 as cv

# img = cv.imread('Images/OIP.jpg')

# cv.imshow('Image',img)

def rescaleFrame(frame,scale=0.75):
    # works for images, videos and live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dimentions = (width,height)
    
    return (cv.resize(frame,dimentions,interpolation=cv.INTER_AREA))    


def changeRes(width,height):
    # Live video
    capture.set(3,width)
    capture.set(4,height) 


capture = cv.VideoCapture('Video/v1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    
    rescaled_frame = rescaleFrame(frame,scale=0.5)
    cv.imshow('Resized_video',rescaled_frame)

    if cv.waitKey(20) & 0xFF == ord('s'):
        break

capture.release()
cv.destroyAllWindows()