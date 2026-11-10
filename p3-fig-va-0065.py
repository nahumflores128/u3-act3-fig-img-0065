import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import cv2

print("Nahum flores NC = 0065")
print("UIII Act3 colocar puntos a una imagen en blanco y negro")
mi_imagen = cv2.imread("tryhard.png")
imagen_gray = cv2.cvtColor(mi_imagen, cv2.COLOR_BGR2GRAY)
plt.imshow(imagen_gray, cmap='gray')
plt.title("lara croft y Nahum flores 0065")
plt.axis('on')
plt.show()
print("-+--+-+ puntos en la imagen -+-+-+-+")
x = [240, 312, 305, 290, 385]
y = [185, 185, 255, 300, 370]
plt.imshow(imagen_gray, cmap='gray')
plt.scatter(x, y, s=40, c="red", marker="o")
plt.title("lara croft con puntos marcados - Nahum flores 0065")
plt.show()