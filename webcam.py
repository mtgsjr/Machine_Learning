import cv2
import numpy as np

captura = cv2.VideoCapture(0)

while(1):
    ret, frame = captura.read()
    cv2.imshow("Hello World!", frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

captura.release()
cv2.destroyAllWindows()
