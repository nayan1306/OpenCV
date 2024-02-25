import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Images\OIP (2).jpg")

cv.imshow("Image", img)

# BGR to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to L*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# using matplotlib
plt.imshow(rgb)
plt.show()



cv.waitKey(0)