import cv2
imagem = cv2.imread("olho.jpg")

#cv2.imshow("Original", imagem)

print "Altura (height): %d pixels" % (imagem.shape[0])
print "Largura (width): %d pixels" % (imagem.shape[1])
print "Canais (channels): %d"      % (imagem.shape[2])

(b, g, r) = imagem[0, 0]
print "Cor do pixel em (0, 0) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b)

(b, g, r) = imagem[305, 250]
print "Cor do pixel em (250, 305) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b)

(b, g, r) = imagem[30, 250]
print "Cor do pixel em (250, 30) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b)

cv2.waitKey(0)
