#for this we are going to use method proposed by Viola & Jones
import cv2

cap=cv2.VideoCapture(0)
frameWidth=640
frameHeight=480
#cap.set(valueid,px)
cap.set(3,frameWidth)  #3 is id for width
cap.set(4,frameHeight) #4 is id for height
cap.set(10,50) #10 is id for brightness

faceCascade=cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")
while (True):
# img=cv2.imread("Resources/lena.jpg")
    success,img=cap.read()

    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=faceCascade.detectMultiScale(imgGray,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Video_Output",img)
    # cv2.imshow("Grey",imgGray)

    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break