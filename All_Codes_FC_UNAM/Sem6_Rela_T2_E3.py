import numpy as np
import matplotlib.pyplot as plt

# Coordenadas de los eventos en el espacio de Minkowski
t_A = 0
x_A = 1
t_B = 1
x_B = 5

# Transformación de Lorentz
v = 0.6  # Velocidad relativa
t_A_prime = (t_A - v*x_A) / np.sqrt(1 - v**2)
t_B_prime = (t_B - v*x_B) / np.sqrt(1 - v**2)
x_A_prime = (x_A - v*t_A) / np.sqrt(1 - v**2)
x_B_prime = (x_B - v*t_B) / np.sqrt(1 - v**2)

# Parámetros para la línea de la velocidad de la luz
c = 1.0  # Velocidad de la luz
x_values = np.linspace(-5, 5, 100)
t_values = x_values / c

# Creamos el gráfico
fig, ax = plt.subplots()

# Dibujamos los eventos A y B en el espacio de Minkowski
ax.plot([x_A, x_B], [t_A, t_B], 'ro', label='Eventos A y B')

# Dibujamos los eventos A' y B' en el espacio de Minkowski transformado
ax.plot([x_A_prime, x_B_prime], [t_A_prime, t_B_prime], 'bo', label="Eventos A' y B'")

# Añadimos la línea de la velocidad de la luz
ax.plot(x_values, x_values / c, 'k--', label='Velocidad de la luz')

# Añadimos las rectas t' y x'
# Eje t' (temporal) es paralelo al eje t
ax.plot(x_values, 0.2 * x_values*v / np.sqrt(1 - v**2), 'g--', label="Recta t'")

# Eje x' (espacial) es perpendicular al eje t'
ax.plot(x_values*2, t_values, 'b--', label="Recta x'")

# Dibujamos una línea desde A' hasta la recta t' en algún punto
ax.plot([x_A_prime, 0], [t_A_prime, 0], 'b--', label="Línea desde A' a t'")

# Configuración del gráfico
ax.set_xlabel('Posición en el Espacio (x)')
ax.set_ylabel('Tiempo (t)')
ax.set_title('Espacio de Minkowski')
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
ax.legend()

plt.gca().set_aspect('equal', adjustable='box')
plt.show()
