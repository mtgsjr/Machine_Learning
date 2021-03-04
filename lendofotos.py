#import numpy as np
import cv2

img = cv2.imread('imagem.jpg',0)       # Arquivo imagem.img para img
cv2.imshow('Imagem com Zero',img)      # Abre a janela com img dentro
cv2.waitKey(0)                         # Espera qualquer tecla
cv2.destroyAllWindows()                # Fecha a janela
