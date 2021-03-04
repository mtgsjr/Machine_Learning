import cv2
import numpy as np
face_cascade = cv2.CascadeCassifier('haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)
scale_factor = 1.3
while 1:
     ret, pic = capture.read()
     faces = face_cascade.detectMultiScale(pic, scale_factor, 5)
     for (x, y, w, h) in faces:
         cv2.rectangle(pic, (x, y), (x + w, y + h), (255, 0, 0), 2)
         font = cv2.FONT_HERSHEY_SIMPLEX
         cv2.putText(pic, 'Marcos Tulio', (x, y), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

      print("Numero de faces detectadas {} ".format(len(faces)))
      cv2.imshow('Detector de Faces', pic)
      k = cv2.waitKey(30) & 0xff
      if k == 27
         break

#capture.release()
cv2.destroyAllWindows()
