def tablas():
    flag=True
    while flag==True:
        numero=int(input("Numero que desea saber la tabla: "))
        for i in range(0,10):
            total=numero*i
            print(f"{numero} x  {i}  = {total}")
            i+=1
        respuesta=input("Desea saber otro Numero? Si/No: ")
        if respuesta=="Si" or respuesta=="si":
            continue
        else:
            break
        


if __name__ == "__main__":
    tablas()