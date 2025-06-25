#Crear menú que permita seleccionar  distintas opciones: 
estudiantes=["Juan Perez", "Martina Martinez", "Juana Pereyra"]
op=input("MENÚ OPCIONES \n 1- Añadir elemento en la lista.\n 2- Reemplazar elemento determinado en la lista.\n 3- Insertar elemento en posición determianda de la lista.\n 4-Mostrar la lista de elementos.\n")
if op=="1":
    ne=input("Ingrese el nombre de estudiante que desea añadir:")
    estudiantes.append(ne)
    print("Lista de estudiantes:", estudiantes)
elif op=="2":
    nr=input("Ingrese el nombre de estudainte que desea reemplazar:")  
    i=estudiantes.index(nr)
    r=input("Ingrese nuevo nombre que reemplaza anterior:")
    estudiantes[i]=r
    print("Lista de estudiantes:", estudiantes)
elif op=="3":
    ei=input("Ingrese el nombre de estudiante que desea insertar:")
    pi=int(input("Ingrese la posición de indice donde desea insertar el nuevo elemento:"))
    estudiantes.insert(pi,ei)
    print("Lista de estudiantes:", estudiantes)
elif op=="4":
    print("Lista de estudiantes:", estudiantes)
    
else:
    print("OPCIÓN NO VÁLIDA")    

    
    