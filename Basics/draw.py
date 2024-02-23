import cv2 as cv
import numpy as np

# Creating an image
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow("Blank",blank) 

# painting an image a particular color
blank[:] = 10,160,0
cv.imshow("Color",blank)

# For a  particular region 
blank[100:400,350:500] = 0,160,250
cv.imshow("Patch",blank)

#  rectangle 
cv.rectangle(blank,(0,0),(255,255),(255,120,10),thickness=30)
cv.imshow("Rectangle",blank)
# Filled rectangle
cv.rectangle(blank,(0,0),(255,255),(155,120,10),thickness=cv.FILLED)
cv.imshow("Filled Rectangle",blank)


# Draw a filled circle
center_coordinates = (200, 200)
radius = 50
color = (10, 50, 155)
cv.circle(blank, center_coordinates, radius, color, thickness=cv.FILLED)

# Draw a line
start_point = (50, 50)
end_point = (350, 350)
line_color = (255, 255, 255)
line_thickness = 3
cv.line(blank, start_point, end_point, line_color, thickness=line_thickness)

# Add text
text = "Sample Text"
org = (100, 30)
font = cv.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 255, 255)
cv.putText(blank, text, org, font, font_scale, font_color, thickness=2)

# Display the image with the shapes and text
cv.imshow("Shapes and Text Example", blank)
cv.waitKey(0)
cv.destroyAllWindows()