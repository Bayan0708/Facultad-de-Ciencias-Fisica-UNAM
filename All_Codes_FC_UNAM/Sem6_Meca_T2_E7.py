import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir las funciones phi1 y phi2
def phi1(x, y, z):
    return x**2 + 2*x*y - y**2 + y*z + z**2 - 9

def phi2(x, y, z):
    return 3*x**2 - x*y + y**2 - 11

# Crear una malla de puntos en el espacio tridimensional
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
z = np.linspace(-5, 5, 100)
X, Y, Z = np.meshgrid(x, y, z)

# Calcular los valores de phi1 y phi2 en cada punto de la malla
F1 = phi1(X, Y, Z)
F2 = phi2(X, Y, Z)

# Crear la figura
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie phi1=0
ax.contour3D(X, Y, F1, levels=[0], colors='blue', label='Phi1=0')

# Graficar la superficie phi2=0
ax.contour3D(X, Y, F2, levels=[0], colors='red', label='Phi2=0')

# Graficar el punto (2,1,1)
ax.scatter3D(2, 1, 1, color='green', s=100, label='Punto (2,1,1)')

# Graficar el vector (1/√2)(ĵ-k̂)
ax.quiver(2, 1, 1, 0, 1/np.sqrt(2), -1/np.sqrt(2), color='purple', label='Vector')

# Etiquetas y leyenda
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.title('Gráfico de las Curvas y el Punto con un Vector')
plt.show()
