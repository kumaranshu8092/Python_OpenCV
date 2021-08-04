import cv2
import numpy as np
import face_recognition

#loading the images from local drive
imgElon=face_recognition.load_image_file("imagesBasic/Elon Musk.jpeg")
#converting images from BGR to RGB
imgElon=cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

imgElon_test=face_recognition.load_image_file("imagesBasic/Akshay Kumar.jpg")
imgElon_test=cv2.cvtColor(imgElon_test,cv2.COLOR_BGR2RGB)

#getting the location of face from the image
faceloc_elon=face_recognition.face_locations(imgElon)[0]
#encoding the face we have detected
faceencod_elon=face_recognition.face_encodings(imgElon)[0]
#drawing rectangle on the detected face
cv2.rectangle(imgElon,(faceloc_elon[3],faceloc_elon[0]),(faceloc_elon[1],faceloc_elon[2]),(255,0,255),2)

faceloc_elon_test=face_recognition.face_locations(imgElon_test)[0]
faceencod_elon_test=face_recognition.face_encodings(imgElon_test)[0]
cv2.rectangle(imgElon_test,(faceloc_elon_test[3],faceloc_elon_test[0]),(faceloc_elon_test[1],faceloc_elon_test[2]),(255,0,255),2)

#comparing the image distance to differentiate the person
result=face_recognition.compare_faces([faceencod_elon],faceencod_elon_test)
facedist=face_recognition.face_distance([faceencod_elon],faceencod_elon_test)

print(result,facedist)
cv2.putText(imgElon_test,f'{result} {round(facedist[0],2)}',(50,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)

cv2.imshow("Elon Musk",imgElon)
cv2.imshow("Elon TEST",imgElon_test)
cv2.waitKey(0)
