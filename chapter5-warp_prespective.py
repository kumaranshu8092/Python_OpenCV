import cv2
import numpy as np

img=cv2.imread("Resources/card.jpg")
imgResize=cv2.resize(img,(640,480))
width,height=250,350
pts1=np.float32([[22,258],[382,215],[76,766],[446,715]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgoutput=cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("cards",imgResize)
cv2.imshow("onecard",imgoutput)


cv2.waitKey(0)