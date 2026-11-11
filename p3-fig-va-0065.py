import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

print("Nahum flores NC = 0065")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro ")
mi_imagen = cv2.imread("tryhard.png")
imagen_gray = cv2.cvtColor(mi_imagen, cv2.COLOR_BGR2GRAY)
plt.imshow(imagen_gray, cmap='gray')
plt.title("lara croft y Nahum flores 0065")
plt.axis('on')
plt.show()
print("-+--+-+ puntos en la imagen  -+-+-+-+")
x = [100, 200, 300, 400, 500]
y = [100, 200, 300, 400, 500]
plt.imshow(imagen_gray, cmap='gray')
plt.scatter(x, y, s=40, c="red", marker="o")
plt.title("lara croft con puntos marcados - Nahum flores 0065")
plt.show()
print(" -+-+-+-+-+ colocar cuadro azul -+-+-+--")
img_tryhard = cv2.imread("tryhard.png")
plt.imshow(img_tryhard)
#x = [200,200,800,800,200]
#y = [800,200,200,800,800]
x = [200,200,800,800,200]
y = [800,200,200,800,800]
plt.plot(x, y, c = "blue")
plt.show()
print(" -+-+-+-+-+ colocar cuadro azul -+-+-+--")
img_tryhard = cv2.imread("tryhard.png")
plt.imshow(img_tryhard)
x = [350, 350, 650, 650, 350]
y = [650, 350, 350, 650, 650]
plt.plot(x, y, c="blue")
plt.show()
print("-+-+--+ circulo verde -+-+-+-+-+")
I = cv2.imread("tryhard.png")
plt.imshow(I)
N = 30 # lados del oligono
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc,yc) = (340,320)
r = 150 # radio
for i in range(N+1):
    t   =2*np.pi/N*i 
    x[i] = xc + r*np.cos(t)
    y[i] = yc + r*np.sin(t)

plt.plot(x, y, c="green")    
plt.show()
