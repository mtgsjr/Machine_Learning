import cv2

#desenha a linha diagonal
azul = (255, 0, 0)
cv2.line(canvas, (0, 0), (400, 300), azul)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#desenha a linha vertical
verde = (0, 255, 0)
cv2.line(canvas, (200, 0), (200, 300), verde, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
