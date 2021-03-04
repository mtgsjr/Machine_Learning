import cv2
import numpy as np
cam=cv2.VideoCapture(0)
kernel=np.ones((5,5),np.uint8)
while (1):
   ret,frame=cam.read()
   rangomax=np.array([50,255,50])
   rangomin=np.array([0,51,0])
   mascara=cv2.inRange(frame,rangomin,rangomax)
   opening=cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
   x,y,w,h=cv2.boundingRect(opening)
   cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
   cv2.circle(frame,(x+w/2,y+h/2),5,(0,0,255),-1)
   cv2.imshow('Camera',frame)
   k=cv2.waitKey(1) & 0xFF
   if k==27:
      break

captura.release()
cv2.destroyAllWindows()
