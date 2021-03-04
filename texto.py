import cv2
import numpy as np
img = np.zeros((500,500,3), dtype='uint8')
fonte=cv2.FONT_HERSHEY_DUPLEX
texto='Marcos Tulio'
cv2.putText(img,texto,(100,100), fonte, 0.8,(255,255,255),4,cv2.LINE_8)
cv2.imshow('dark',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
