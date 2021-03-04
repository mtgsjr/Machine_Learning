import numpy as np
import cv2

img = cv2.imread('imagem.jpg')          # ler imagem jpg
img = cv2.imwrite('imagem.png',img)     # gravar imagem png
img = cv2.imread('imagem.png',1)        # Ler imagem png
cv2.imshow('Imagem em PNG',img)         # Abrir uma janela  
cv2.waitKey(0)                          # Espere ESC
cv2.destroyAllWindows()                 # Fechar Janela
