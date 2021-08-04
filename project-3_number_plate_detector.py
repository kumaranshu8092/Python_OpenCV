import cv2
import numpy as np

cap=cv2.VideoCapture(1)# 0 is camera id
#######################################################
frameWidth=640
frameHeight=480
minarea=500
count=0
#######################################################
#cap.set(valueid,px)
cap.set(3,frameWidth)  #3 is id for width
cap.set(4,frameHeight) #4 is id for height
cap.set(10,50) #10 is id for brightness
num_plate_Cascade=cv2.CascadeClassifier("Resources/haarcascades/haarcascade_russian_plate_number.xml")

while(True):
    success,img=cap.read()
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberplates=num_plate_Cascade.detectMultiScale(imgGray,1.1,4)
    for(x,y,w,h) in numberplates:
        area=w*h
        if area>minarea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0,255), 2)
            cv2.putText(img,"Number Plate", (x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),2)
            imgnumber=img[y:y+h,x:x+w]
            cv2.imshow("Number_Plate",imgnumber)

    cv2.imshow("Video_Output",img)
    if cv2.waitKey(1) & 0xFF ==ord("s"):
        cv2.imwrite("Resources/Scanned/No_plate_"+str(count)+".jpg",imgnumber)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_PLAIN,
                    2,(0, 0, 255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count += 1
    elif cv2.waitKey(1) & 0xFF==ord("q"):
        break