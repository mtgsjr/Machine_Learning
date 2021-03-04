import cv2                           # Adiciona a biblioteca OpenCV
imagem = cv2.imread("olho.jpg")      # Armazena a imagem na variavel
fatia = imagem[100:300, 150:350]     # Coordenadas em COLUNAS e LINHAS
cv2.imshow("Fatia da Imagem",fatia)  # Exibe a fatia processada
cv2.waitKey(0)                       # Espera teclar algo para finalizar
