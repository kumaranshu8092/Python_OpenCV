import cv2
img=cv2.imread("Resources/heading_logo.png")
#resizing of image
imgResize=cv2.resize(img,(300,300))
print(imgResize.shape)
#cropping the image
#in this 1st parameter is height and 2nd is width& both are inn range
imgCrop=img[0:200,200:500]
cv2.imshow("Img",img)
#cv2.imshow("Resized_Img",imgResize)
cv2.imshow("Cropped_image",imgCrop)

cv2.waitKey(0)