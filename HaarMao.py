import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)

df = cv2.CascadeClassifier('mao.xml')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    iPB = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Executa a deteccao
    objs = df.detectMultiScale(iPB, scaleFactor = 1.05, minNeighbors = 7, minSize = (30,30), flags = cv2.CASCADE_SCALE_IMAGE)

    #Desenha retangulos amarelos na iamgem original (colorida)
    for (x, y, w, h) in objs:
      cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 7)
      
    #Exibe imagem. Titulo da janela exibe numero de faces
    #cv2.imshow(str(len(objs))+' objetos(s) encontrado(s).', frame)
    cv2.imshow('Im watching you!', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
