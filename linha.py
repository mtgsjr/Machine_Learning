import cv2
import numpy as np
# Lembrando que as coordenada dos Pixels
# eh COLUNA, LINHA
img = np.zeros((500,500,3), dtype='uint8')
cv2.line(img,(50,200),(450,200),(0,0,255))
cv2.imshow('dark',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
