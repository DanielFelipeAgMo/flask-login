import random
import os

palabras = ["PERRO","GATO","PATO","GALLINA","OSO","LORITO","PEZ","GALLINAZO","BOA","CANGREJO"]

palabra = list(random.choise(palabras))

lazo = [ "        !=======|",
         "                |",
         "                |",
         "                |",
         "                |",
         "                |",
         "                |",
         "________________|"]

ahorcado = ["        !=======|",
            "        0       |",
            "      / | \     |",
            "      \ | /     |",
            "       / \      |",
            "      /   \     |",
            "      |   |     |",
            "________________|"]

abecedario = [] #comentario
errores = 1 #comentario
resultado = [] #comentario

for i in range(len(palabra)):
	resultado.append("_")

while True:#ciclo principal
	os.system("cls")

	print("**************************")
    print("**BIENVENIDOS A SU JUEGO**")

    for i in range(errores):
        print(ahorcado[i])

    for i in range(len(lazo)-errores):
		print(lazo[i+errores])

print()
print("  ",end=" ")
for i in resultado:
	print(i,end=" ")

print()
print()

if resultado == palabra:
	print("FELICIDADES TE SALVASTE Y GANASTE")
	break

if errores > 6:
	print("HUY JUEMADRE TE AHORCASTE la palabra era: ","".join(palabra))
	break

#comentando
while True:
	letra_desorden_jugador = input("Escribe una letra: ")
	letra_jugador = letra_desorden_jugador.upper()
    if len(letra_jugador)!=1:
		print("escriba una letra pués")
	elif letra_jugador in abecedario:
        print("Recuerde que esa letra ya pusiste.")
    elif letra_jugador not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
        print("estas como elevao, recuerde que es una letra")
    else:
        abecedario.append(letra_jugador)
        break

#comprobando si la letras estan en la palabra
for i in range(len(palabra)):
	if palabra[i] == letra_jugador:
		resultado[i] = letra_jugador
if letra_jugador not in palabra:
	errores +=1

print()



