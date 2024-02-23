import cv2 as cv

# #  Reading images
# img = cv.imread('Images\OIP (1).jpg')

# cv.imshow("Shinchan",img)

# cv.waitKey(0)

#  Reading Videos
capture = cv.VideoCapture('Video/v3.mp4')

while True:
    isTrue, frame = capture.read()
    
    cv.imshow("Video",frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()         
    