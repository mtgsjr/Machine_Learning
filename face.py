import cv2

arqCasc = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(arqCasc)

webcam = cv2.VideoCapture(0)  #instancia o uso da webcam

while True:
    s, imagem = webcam.read() #pega efeticamente a imagem da webcam
    imagem = cv2.flip(imagem,180) #espelha a imagem

    faces = faceCascade.detectMultiScale(
        imagem,
        minNeighbors=5,
        minSize=(30, 30),
	maxSize=(200,200)
    )

    # Desenha um retangulo nas faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Video', imagem) #mostra a imagem captura na janela

    #o trecho seguinte eh apenas para parar o codigo e fechar a janela
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release() #dispensa o uso da webcam
cv2.destroyAllWindows() #fecha todas a janelas abertas


