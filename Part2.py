import face_recognition
import numpy as np
import cv2
import os

path='C:/Users/Hp/Downloads/Attendence System 18/Images'
images=[]
className=[]
StudentList=os.listdir(path)
print(StudentList)
for cl in StudentList:
    curImg=cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    className.append(os.path.splitext(cl)[0])
print(className)

def findEncodings(images):
    encodelist=[]
    for img in images:
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist
EncodeListKnown= findEncodings(images)
print(len(EncodeListKnown))

cap= cv2.VideoCapture(0)

while True:
    success, img= cap.read()
    imgS= cv2.resize(img,(0,0),None,0.25,0.25)
    imgS= cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
    
    facesCurFrame=face_recognition.face_locations(imgS)
    encodesCurFrame=face_recognition.face_encodings(imgS,facesCurFrame)
    
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches=face_recognition.compare_faces(EncodeListKnown,encodeFace)
        faceDis=face_recognition.face_distance(EncodeListKnown,encodeFace)
        print(faceDis)
        matchindex=np.argmin(faceDis)
        if matches[matchindex]:
            name=className[matchindex].upper()
            print(name)