def run():
    diccionario_nuevo= {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(diccionario_nuevo['llave1'])
    poblacion_pais ={
        'Colombia': 48500300,
        'Brasil': 25039610,
        'Argentina': 44936120
    }
    
    for pais in poblacion_pais.values():
        print(pais)
    
    
    for pais, poblacion in poblacion_pais.items():
        print(pais + ' tiene '+ str(poblacion)+' habitantes')
    
if __name__== '__main__':
    run()