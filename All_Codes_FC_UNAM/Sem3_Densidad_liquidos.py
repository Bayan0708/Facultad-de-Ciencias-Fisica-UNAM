import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Datos de la tabla
profundidades = [
    0.0120, 0.0320, 0.0600, 0.0790, 0.0990, 
    0.1180, 0.1380, 0.1580, 0.1780, 0.1960
]

acetonas = [0.0140, 0.0310, 0.0510, 0.0630, 0.0810, 0.1030, 0.1220, 0.1480, 0.1560, 0.1640]
aceites = [0.0150, 0.0350, 0.0570, 0.0770, 0.0860, 0.1100, 0.1260, 0.1480, 0.1420, 0.1570]
alcoholes = [0.0090, 0.0240, 0.0370, 0.0570, 0.0770, 0.0980, 0.1120, 0.1260, 0.1480, 0.1590]
shampoos = [0.0110, 0.0140, 0.0350, 0.0490, 0.0540, None, None, None, None, None]
aguas = [0.0100, 0.0310, 0.0510, 0.0720, 0.0830, 0.1000, 0.1200, 0.1410, 0.1600, 0.1720]

# Crear DataFrame
data = {
    "Profundidades (m)": profundidades,
    "Acetona (m)": acetonas,
    "Aceite (m)": aceites,
    "Alcohol (m)": alcoholes,
    "Shampoo (m)": shampoos,
    "Agua (m)": aguas
}

df = pd.DataFrame(data)

# Calcular estadísticas básicas
stats = df.describe()

# Graficar los datos
plt.figure(figsize=(10, 6))
for liquido in ["Acetona (m)", "Aceite (m)", "Alcohol (m)", "Shampoo (m)", "Agua (m)"]:
    plt.plot(df["Profundidades (m)"], df[liquido], marker='o', label=liquido)

plt.xlabel("Profundidad (m)")
plt.ylabel("L (m)")
plt.title("Relación entre profundidad y diferencia de altura en el manómetro")
plt.legend()
plt.grid()
plt.show()

# Guardar estadísticas en un archivo
stats.to_csv("estadisticas_liquidos.csv")

# Mostrar estadísticas
print(stats)
