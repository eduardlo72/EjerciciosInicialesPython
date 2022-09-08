import random


def generar_contrasena():
    mayusculas = ["A","B","C","D","E","F","G","H"]
    minusculas = ["a","b","c","d","e","f","g","h"]
    simbolos = ["!","@","#","$","%","&","/"]
    numeros = ["1","2","3","4","5","6","7","8","9","0"]
    caracteres = mayusculas + minusculas + simbolos + numeros
    contrasena = []
    for i in range(15):
        caranter_ramdom = random.choice(caracteres)
        contrasena.append(caranter_ramdom)
    # convertir una lista a string
    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)
    print(len(contrasena))


if __name__ == "__main__":
    run()