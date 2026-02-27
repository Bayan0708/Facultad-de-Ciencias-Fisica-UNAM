import numpy as np
import matplotlib.pyplot as ptl

datos = np.loadtxt ('D:\Semestre_2\Laboratorio_de_Mecánica\tirop.dat')
t = datos [:,0]
x = datos [:,1]

poli = np.polyfit (t,x,1)
print (poli)
x_ajured = poli[0]*t+poli[1]

tx = t*x

N = len (t)

m = (N*np.sum(tx)-np.sum(t*np.sum(x)))/(N*np)





