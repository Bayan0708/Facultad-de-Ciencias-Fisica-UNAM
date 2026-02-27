DAGUA = 1
DACEITE = 0.9
DALCOHOL = 0.8

print ("")

h1 = (6 - (7*DALCOHOL))/(DAGUA-DALCOHOL)
print ("La altura exacta de A es de " + str(h1) + " cm")
print ("El Peso debe ser exactamente de " + str((DAGUA*9*h1)+(DALCOHOL)*9*(7-h1)) + " g gramos")
print ("A es Agua con altura "+ str(round (h1)) + (" cm y B es Alcohol con altura " )+ str(round (7-h1)) + (" cm") + ", para un Peso de " + str(round((DAGUA*9*h1)+(DALCOHOL)*9*(7-h1)))+ " g gramos")
print ("")

h2 = (6 - (7*DACEITE))/(DAGUA-DACEITE)

print ("La altura exacta de A es de " + str(h2) + " cm")
print ("El Peso debe ser exactamente de " + str((DAGUA*9*h2)+(DACEITE)*9*(7-h2)) + " g gramos")
print ("A es Agua con altura "+ str(round (h2)) + (" cm y B es Aceite con altura " )+ str(round (7-h2)) + (" cm") + ", para un Peso de " + str(round((DAGUA*9*h2)+(DACEITE)*9*(7-h2)))+ " g gramos")
print ("")

h3 = (6 - (7*DAGUA))/(DACEITE-DAGUA)
print ("La altura exacta de A es de " + str(h3) + " cm")
print ("El Peso debe ser exactamente de " + str((DACEITE*9*h3)+(DAGUA)*9*(7-h3)) + " g gramos")
print ("A es Aceite con altura "+ str(round (h3)) + (" cm y B es Agua con altura " )+ str(round (7-h3)) + (" cm") + ", para un Peso de " + str(round((DACEITE*9*h3)+(DAGUA)*9*(7-h3)))+ " g gramos")
print ("")

h4 = (6 - (7*DALCOHOL))/(DACEITE-DALCOHOL)
print ("La altura exacta de A es de " + str(h4) + " cm")
print ("El Peso debe ser exactamente de " + str((DACEITE*9*h4)+(DALCOHOL)*9*(7-h4)) + " g gramos")
print ("A es Aceite con altura "+ str(round (h4)) + (" cm y B es Alcohol con altura " )+ str(round (7-h4)) + (" cm") + ", para un Peso de " + str(round((DACEITE*9*h4)+(DALCOHOL)*9*(7-h4)))+ " g gramos")
print ("")

h5 = (6 - (7*DAGUA))/(DALCOHOL-DAGUA)
print ("La altura exacta de A es de " + str(h5) + " cm")
print ("El Peso debe ser exactamente de " + str((DALCOHOL*9*h5)+(DAGUA)*9*(7-h5)) + " g gramos")
print ("A es Alcohol con altura "+ str(round (h5)) + (" cm y B es Agua con altura " )+ str(round (7-h5)) + (" cm") + ", para un Peso de " + str(round((DALCOHOL*9*h5)+(DAGUA)*9*(7-h5)))+ " g gramos")
print ("")

h6 = (6 - (7*DACEITE))/(DALCOHOL-DACEITE)
print ("La altura exacta de A es de " + str(h6) + " cm")
print ("El Peso debe ser exactamente de " + str((DALCOHOL*9*h6)+(DACEITE)*9*(7-h6)) + " g gramos")
print ("A es Alcohol con altura "+ str(round (h6)) + (" cm y B es Aceite con altura " )+ str(round (7-h6)) + (" cm") + ", para un Peso de " + str(round((DALCOHOL*9*h6)+(DACEITE)*9*(7-h6)))+ " g gramos")
print ("")
