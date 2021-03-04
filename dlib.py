import cv2
import dlib

def imprimePontos (webcam, pontosFaciais):
    for p in pontosFaciais.parts():
        cv2.circle(webcam, (p.x, p.y), 2,(0, 255,0), 2)

fonte = cv2.FONT_HERSHEY_COMPLEX_SMALL
webcam = cv2.VideoCapture(0)
detectorFace = dlib.get_frontal_face_detector()
detectorPontosFaciais = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
conectado, imagem = webcam.read()

while (True):
    conectado, imagem = webcam.read()
    facesDetectadas = detectorFace(imagem, 2)
    for face in facesDetectadas:
        pontos = detectorPontosFaciais(imagem, face)
        print(pontos.parts())
        print(len(pontos.parts()))
        imprimePontos(webcam,pontos)
        cv2.imshow('Pontos Faciais', imagem)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
           break

webcam.release()
cv2.destroyAllWindows()
