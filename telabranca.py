import cv2
import numpy as np
canvas = np.ones((300, 400, 3)) * 255 
#imagem 400x300, com fundo branco e 3 canais para as cores
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
