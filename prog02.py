import cv2                                    # Importa o OpenCV
captura = cv2.VideoCapture(0)                 # liga a webcam
while(1):                                     # Enquanto verdade
    ret,frame = captura.read()
    (b, g, r) = frame[200, 200]
    frame[198:202, 198:202] = (0, 0, 255)
    frame[10:90, 10:90] = (b, g, r)
    cv2.imshow('Hello World!',frame)
    k = cv2.waitKey(30) & 0xff                # 'k' recebe o valor da tecla
    if k == 27:                               # Se teclar ESC
        break                                 # Quebra o laco e sai

captura.release()                             # desliga a webcam
cv2.destroyAllWindows()                       # fecha a janela
