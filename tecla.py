import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imshow('frame',frame)

while(1):
    cv2.imshow('frame',frame)

    k = cv2.waitKey(30) & 0xff

    if k==27:     #Tecla Esc foi pressionada
        break
    elif k==255:  #Nenhum tecla foi pressionada
        continue
    else:
        print k   #Informa qual tecla foi pressionada

cap.release()
cv2.destroyAllWindows()
