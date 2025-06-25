dic={"or":"o","if":"si","else":"sino","elif":"sino si","for":"para","while":"mientras","and":"y"}
while True:
    palBuscar=input("Ingrese la palabra a buscar su significado en español: ")
   # palBuscar=palBuscar.title()
    if palBuscar in dic:
        print("Significado")
    else:
        print("La palabra buscada no se encuentra en el diccionario")    
    for c,v in dic.items():
        if palBuscar==c:
            print("El significado de la palabra ", c,"es: ",v)
                         
    continuarBuscando=input("Desea buscar el significado de otra palabra? S/N: ")    
    
    if continuarBuscando=="N" or continuarBuscando=="n":
        break   
    
    
    
    
    
    
    
    