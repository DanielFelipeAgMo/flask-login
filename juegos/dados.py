from random import randint
import sys

def lanzar():
    return randint(1,6)

dado1 = lanzar()
dado2 = lanzar()
print(f"El primer dado cayó asi:  {dado1}")
print(f"El segundo dado cayó asi:  {dado2}")
print(f"La suma de ambos dados es :  {dado1 + dado2}")

respuesta = int(input("Quieres volver a lanzar los dados?  Presiona 1 para si o 2 para no. "))
if respuesta == 1:
    dado1 = lanzar()
    dado2 = lanzar()
    print(f"El primer dado cayó asi:  {dado1}")
    print(f"El segundo dado cayó asi:  {dado2}")
    print(f"La suma de ambos dados es :  {dado1 + dado2}")
elif respuesta == 2:
    sys.exit()
else: print("Ingres un valor valido sea 1 o 2")

