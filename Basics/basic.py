import cv2 as cv

img = cv.imread("Images/OIP (2).jpg")
cv.imshow("Image",img)

# Converting to grayscale
greyScale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grey Scale", greyScale)

# blur
blurImg = cv.GaussianBlur(img, (7,7),cv.BORDER_DEFAULT)
cv.imshow("Blur", blurImg)

# Edge cascade
edgeCas = cv.Canny(img,170,150)
cv.imshow("Canny Edges", edgeCas)

# Dilating
imgDilate = cv.dilate(edgeCas, (7,7), iterations=2)
cv.imshow("Dilated", imgDilate)

# eroding
imgErode = cv.erode(imgDilate, (7,7), iterations=2)
cv.imshow("Eroded", imgErode)

# Resizing
imgResize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",imgResize)

# Cropping
imgCrop = img[0:250,100:400]
cv.imshow("Cropped", imgCrop)

cv.waitKey(0)