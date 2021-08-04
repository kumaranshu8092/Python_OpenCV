import cv2
# print("Package Imported")
#
# #for reading images
#
# img=cv2.imread("Resources/heading_logo.png")
#
# #to display the image(i.e. output)
# # cv2.imshow("output window name",image variable name)
# cv2.imshow("Image",img)
#
# #now the output screen will be closed immedietly
#
# #to hold the output screen
# cv2.waitKey(0)
# #it takes value in milisecond for infinite time we use )
#
# #importing video
#
# vid=cv2.VideoCapture("Resources/data.mp4")
# #we will run loop as video is sequence of image
# while(True):
#     """here we stored video as image and
#     show the image in sequential manner"""
#     success,vimg=vid.read()
#
#     cv2.imshow("Video_Output",vimg)
# """here we are closing the window if
# user enters q or the video once played"""
#     if cv2.waitKey(1) & 0xFF ==ord("q"):
#         break

# here we are reading the camera

cap=cv2.VideoCapture(0)# 0 is camera id
frameWidth=640
frameHeight=480
#cap.set(valueid,px)
cap.set(3,frameWidth)  #3 is id for width
cap.set(4,frameHeight) #4 is id for height
cap.set(10,50) #10 is id for brightness
while(True):
    """here we stored video as image and
    show the image in sequential manner"""
    success,vimg=cap.read()

    cv2.imshow("Video_Output",vimg)
    """here we are closing the window if
    user enters q or the video once played"""
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break

