import cv2
def calculaDiferenca(img1, img2, img3):
  d1 = cv2.absdiff(img3, img2)
  d2 = cv2.absdiff(img2, img1)
  return cv2.bitwise_and(d1, d2)

webcam = cv2.VideoCapture(0) #instancia o uso da webcam
janela = "OpenCV FPB | Q para sair"
#cv2.namedWindow(janela, cv2.CV_WINDOW_AUTOSIZE) #cria uma janela

#faz a leitura inicial de imagens
ultima        = cv2.cvtColor(webcam.read()[1], cv2.COLOR_RGB2GRAY)
penultima     = ultima
antepenultima = ultima

while True:
  antepenultima = penultima
  penultima     = ultima
  ultima        = cv2.cvtColor(webcam.read()[1], cv2.COLOR_RGB2GRAY)

  cv2.imshow(janela, calculaDiferenca(antepenultima,penultima,ultima))

  if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyWindow(janela)
    break

print "Fim do Programa"
