import cv2 as cv
import numpy as np

img = cv.imread("Images\OIP (2).jpg")

cv.imshow("Image", img)

# Translation
def translate(img,x,y):
    
    # Define a 2x3 transformation matrix for translation
    transMat = np.float32([[1,0,x],[0,1,y]])
    
     # Get the dimensions of the input image
    dimentions = (img.shape[1], img.shape[0])
    
    return cv.warpAffine(img,transMat,dimentions)

# -x : Left
# -y : up
# x : right
# y : Down

imgTrans = translate(img,50,20)
cv.imshow("Translated", imgTrans)


# Rotation
def rotate(img, angle, rotpoint=None):
    (height,width) = img.shape[:2]
    
    if rotpoint is None:
        rotpoint = (width//2, height//2)
        
    rotmatrix = cv.getRotationMatrix2D(rotpoint,angle,scale=1.0)
    dimentions = (width,height)
    
    return cv.warpAffine(img, rotmatrix, dimentions)

imgRot = rotate(img,45)
imgRot = rotate(img,75,(100,140))

cv.imshow("Rotated", imgRot)    

# resizing
imgRes = cv.resize(img, (300,300), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", imgRes)

# Flipping
imgFlip = cv.flip(img, -1)
cv.imshow("Flipped", imgFlip)




cv.waitKey(0)
cv.destroyAllWindows()