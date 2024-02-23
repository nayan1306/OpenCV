import cv2 as cv
import numpy as np

img = cv.imread("Images\OIP (2).jpg")

cv.imshow("Image", img)


# convert to greysacle
imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grey", imgGrey)

#  Convert to canny
imgCanny = cv.Canny(img, 175, 200)
cv.imshow('Canny',imgCanny)

# Finding Countours
contours, hirearchies = cv.findContours(imgCanny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

print("Number of contours : ", len(contours))

blank = np.zeros((250,350,3),dtype='uint8')
cv.imshow("Blank",blank) 

cv.drawContours(blank, contours,-1,(0,0,255),1)
cv.imshow('Countours Drawn',blank)



cv.waitKey(0)
cv.destroyAllWindows()