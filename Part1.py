import face_recognition
import numpy as np
import cv2


imgSaved = face_recognition.load_image_file('C:/Users/Hp/Downloads/Attendence System 18/Images/Pearl_1804023.jpg')
imgSaved = cv2.cvtColor(imgSaved,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('C:/Users/Hp/Downloads/Attendence System 18/Images/Tahmina_1804034.JPG')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
 
faceLoc = face_recognition.face_locations(imgSaved)[0]
encodeSaved = face_recognition.face_encodings(imgSaved)[0]
cv2.rectangle(imgSaved,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
 
faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)
 
results = face_recognition.compare_faces([encodeSaved],encodeTest)
faceDis = face_recognition.face_distance([encodeSaved],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
 
cv2.imshow('New',imgSaved)
cv2.imshow('Old',imgTest)
cv2.waitKey(0)