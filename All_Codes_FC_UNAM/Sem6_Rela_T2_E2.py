import numpy as np
#a)
S = np.array([1, 0, 1])
SS = np.dot(S.T, S)
SS = np.squeeze(SS)
SS = np.round(SS, 4)
print("a) El cuadrado del desplazamiento es:", SS)
#b)
A = np.array([[1/np.sqrt(2), 0, 1/np.sqrt(2)],
              [0, 1, 0],
              [-1/np.sqrt(2), 0, 1/np.sqrt(2)]])
B = np.array([[1],
              [0],
              [1]])
AB = np.dot(A, B)
ABAB = np.dot(AB.T, AB)
ABAB = np.squeeze(ABAB)
ABAB = np.round(ABAB, 4)
print(" b) El cuadrado del desplazamiento es:", ABAB)
#c)
AT = np.array([[1/np.sqrt(2), 0, -1/np.sqrt(2)],
              [0, 1, 0],
              [1/np.sqrt(2), 0, 1/np.sqrt(2)]])
I = np.array([[1,0,0],
              [0, 1, 0],
              [0,0,1]])
ATI = np.dot(AT, I)
ATIA = np.dot(ATI, A)
ATIA = np.squeeze(ATIA)
ATIA = np.round(ATIA, 4)
print(" C):",ATIA)