import cv2
import numpy as np

arqCasc = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(arqCasc)
webcam = cv2.VideoCapture(0)  #instancia o uso da webcam
rec=cv2.createLBPHFaceRecognizer();
rec.load("recognizer/trainningData.yml")
id=0
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,2,1,0,3)
while True:
    s, imagem = webcam.read() #pega efeticamente a imagem da webcam
    gray = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY) # Transforma em escala de cinza
    faces = faceCascade.detectMultiScale(gray,1.3,5);
    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 2)
	id,conf=rec.predict(gray[y:y+h,x:x+w])
	if (id == 1):
           id = "Marcos"
	if (id == 2):
   	   id = "Pablo"
 	cv2.cv.PutText(cv2.cv.fromarray(imagem),str(id),(x,y+w),font,255);

    cv2.imshow('Reconhecimento', imagem) #mostra a imagem captura na janela

    #o trecho seguinte eh apenas para parar o codigo e fechar a janela
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break

webcam.release() #dispensa o uso da webcam
cv2.destroyAllWindows() #fecha todas a janelas abertas


