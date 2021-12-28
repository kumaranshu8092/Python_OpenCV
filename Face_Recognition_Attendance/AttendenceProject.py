import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

#importing all the images from the database


path="ImagesAttendance"
#creating the list of images
images=[]
#creating the namelist of name which are in path folder
classNames=[]
mylist=os.listdir(path)
print(mylist)
#adding each name in the namelist which are in path folder
for cl in mylist:
    curImg=cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncoding(images):
    encodelist=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist
def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        namelist=[]
        for line in myDataList:
            entry=line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


    
encodelistKnow=findEncoding(images)
print("Encoding Complete")

cap=cv2.VideoCapture(0)

while True:
    success,img = cap.read()
    imgs=cv2.resize(img,(0,0),None,0.25,0.25)
    imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)

    facecurFrame=face_recognition.face_locations(imgs)
    encodesCurFrame= face_recognition.face_encodings(imgs,facecurFrame)

    for encodeFace,faceloc in zip(encodesCurFrame,facecurFrame):
        matches=face_recognition.compare_faces(encodelistKnow,encodeFace)
        facedis=face_recognition.face_distance(encodelistKnow,encodeFace)
        print(facedis)
        matchIndex = np.argmin(facedis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=faceloc
            y1, x2, y2, x1= y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),1)
            markAttendance(name)


    cv2.imshow("webcam",img)
    cv2.waitKey(1)

