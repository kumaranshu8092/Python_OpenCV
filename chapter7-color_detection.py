import cv2
import numpy as np

# cap=cv2.VideoCapture(0)# 0 is camera id
# frameWidth=640
# frameHeight=480
# #cap.set(valueid,px)
# cap.set(3,frameWidth)  #3 is id for width
# cap.set(4,frameHeight) #4 is id for height
# cap.set(10,50) #10 is id for brightness

def empty(a):
    pass


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

path="Resources/lambo.png"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrachBars",640,240)
cv2.createTrackbar("Hue_min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue_max","TrackBars",19,179,empty)
cv2.createTrackbar("Sat_min","TrackBars",118,255,empty)
cv2.createTrackbar("Sat_max","TrackBars",246,255,empty)
cv2.createTrackbar("Val_min","TrackBars",153,255,empty)
cv2.createTrackbar("Val_max","TrackBars",255,255,empty)



while True:

    img=cv2.imread(path)
    # success, img = cap.read()
    #to get the hue-Saturation- value(HSV)
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue_min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue_max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat_min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat_max", "TrackBars")
    V_min = cv2.getTrackbarPos("Val_min", "TrackBars")
    V_max = cv2.getTrackbarPos("Val_max", "TrackBars")
    print(h_min,h_max,s_min,s_max,V_min,V_max)
    lower=np.array([h_min,s_min,V_min])
    upper=np.array([h_max,s_max,V_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imgResult= cv2.bitwise_and(img,img,mask=mask)


    imgStack=stackImages(0.6,([img,imgHSV],[mask,imgResult]))

    cv2.imshow("Stack Image",imgStack)
    cv2.waitKey(1)

    # cv2.imshow("Video_Output", img)
    # cv2.imshow("mask",mask)
    # if cv2.waitKey(1) & 0xFF == ord("q"):
    #     break