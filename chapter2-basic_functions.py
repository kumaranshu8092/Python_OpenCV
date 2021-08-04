# some basic functions of opencv
import cv2
import numpy as np
img=cv2.imread("Resources/heading_logo.png")
kernel=np.ones((5,5),np.uint8)
#here we are converting the image to gray color
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(5,5),0)
imgCanny=cv2.Canny(img,200,150)
#function for  thick
imgDialation=cv2.dilate(imgCanny,kernel,iterations=2)
#function for thinner ness
imgEroded=cv2.erode(imgDialation,kernel,iterations=2)

# cv2.imshow("Gray_image",imgGray)
# cv2.imshow("Blur_image",imgBlur)
cv2.imshow("Canny_image",imgCanny)
cv2.imshow("Dilated_image",imgDialation)
cv2.imshow("Ereded_image",imgEroded)

cv2.waitKey(0)
