import cv2
import numpy as np
import face_recognition

imgbuffit = face_recognition.load_image_file('/Users/yoonseonghyeon/Desktop/programming/python/python_AI/img/buffit.jpeg')
imgbuffit = cv2.cvtColor(imgbuffit, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('/Users/yoonseonghyeon/Desktop/programming/python/python_AI/img/buffit1.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgbuffit)[0]
encodebuffit = face_recognition.face_encodings(imgbuffit)[0]
cv2.rectangle(imgbuffit, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]),(255,0,255),2)


faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]),(255,0,255),2)


results = face_recognition.compare_faces([encodebuffit], encodeTest)
faceDis = face_recognition.face_distance([encodebuffit], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)


cv2.imshow('buffit', imgbuffit)
cv2.imshow('buffit_Text', imgTest)
cv2.waitKey(0)







