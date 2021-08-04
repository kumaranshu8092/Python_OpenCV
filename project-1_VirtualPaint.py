import cv2
import numpy as np
###############Reading Camera######################
cap=cv2.VideoCapture(0)# 0 is camera id
frameWidth=640
frameHeight=480
#cap.set(valueid,px)
cap.set(3,frameWidth)  #3 is id for width
cap.set(4,frameHeight) #4 is id for height
cap.set(10,50) #10 is id for brightness

myColors=[ [90,48,0,118,255,255],
       [28,87,88,50,255,255]
        #[0,173,92,179,255,255]
           ]

myColorValues = [[235,206,135],## BGR
                 [76,255,192],
                # [0,165,255]
                 ]


myPoints = []           #[x,y, colorID]


def findColor(img,myColors,myColorValues):
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count=0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y=getcontours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
        # cv2.imshow(str(color[0]),mask)
    return newPoints

def getcontours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv2.contourArea(cnt)
        # print(area)
        if area>100:
            # cv2.drawContours(imgResult,cnt,-1,(0,0,255),3)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.03*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for points in myPoints:
        cv2.circle(imgResult,(points[0],points[1]),10, myColorValues[points[2]], cv2.FILLED)

while(True):
    success,img=cap.read()
    imgResult=img.copy()
    newPoints= findColor(img,myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break

