import cv2
def canny_webcam():
    "Captura de Imagem (ao vivo)"
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        frame = cv2.GaussianBlur(frame, (7, 7), 1.41)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(frame, 25, 75)
        cv2.imshow('Deteccao de Bordas de Canny | <ESC> para sair', edge)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
        	break

canny_webcam()
