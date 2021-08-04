import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
#here 3 is no of channels like in image...RGB
print(img.shape)
#if we want to add the color
# img[:]=150,150,150
#here img[:] is for cropped size of image
cv2.line(img,(0,0),(512,512),(0,255,0),3)
#cv2.line(image_name,starting,endining_point,color,thicknes(optional))
cv2.rectangle(img,(0,0),(300,250),(255,0,0),3)
#if you want to fill that rectangle
#cv2.rectangle(img,(0,0),(400,300),(255,0,0),cv2.FILLED)
cv2.circle(img,(400,50),30,(0,0,255))
cv2.putText(img,"open CV text function",(100,200),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),3)
cv2.imshow("color",img)
cv2.waitKey(0)