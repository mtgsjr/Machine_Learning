import cv2
import numpy as np
canvas = np.ones((300, 400, 3)) * 255 #imagem 400x300, com fundo branco e 3 canais para as cores
azul = (255, 0, 0)
cv2.line(canvas, (0, 0), (400, 300), azul)

verde = (0, 255, 0)
cv2.line(canvas, (200, 0), (200, 300), verde, 3)

cv2.rectangle(canvas, (10, 70), (90, 190), verde)

vermelho = (0, 0, 255)
cv2.rectangle(canvas, (250, 50), (300, 125), vermelho, -1)

cv2.imshow("Canvas", canvas) #Mostra a Janela
cv2.waitKey(0) # Espera alguma tecla
