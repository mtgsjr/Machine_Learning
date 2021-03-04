import cv2
import numpy as np

arqCasc = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(arqCasc)
webcam = cv2.VideoCapture(0)  #instancia o uso da webcam
samplenumber=0;
id = raw_input("Entre com o ID: ")
while True:
    s, imagem = webcam.read() #pega efeticamente a imagem da webcam
    gray = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY) # Transforma em escala de cinza
    faces = faceCascade.detectMultiScale(gray,1.3,5);
    #imagem = cv2.flip(imagem,180) #espelha a imagem
    #faces = faceCascade.detectMultiScale(
    #    imagem,
    #    minNeighbors=5,
    #    minSize=(30, 30),
    #	maxSize=(200,200)
    #)
    # Desenha um retangulo nas faces detectadas
    for (x, y, w, h) in faces:
        samplenumber=samplenumber+1;
        cv2.imwrite("dataset/user."+str(id)+"."+str(samplenumber)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.waitKey(100)

    cv2.imshow('Cadastro do Usuario', imagem) #mostra a imagem captura na janela
    #o trecho seguinte eh apenas para parar o codigo e fechar a janela
    cv2.waitKey(1)
    if (samplenumber>20):
       break
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break

webcam.release() #dispensa o uso da webcam
cv2.destroyAllWindows() #fecha todas a janelas abertas


