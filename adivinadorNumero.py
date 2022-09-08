from ast import While
import random

n = random.randrange(1,100)
incognita = int(input("Digita un numero cualquiera: "))
intentos = 0;

while n != incognita:
    if incognita < n:
        print("muy pequeño")
        incognita= int(input("intente de nuevo: "))
        intentos +=1
    elif incognita > n:
        print("muy grande")
        incognita= int(input("intente de nuevo: "))
        intentos +=1
    else: break

print("!has adivinado el numero!!")
intentos = print("el total de intentos fue :" + str (intentos))
