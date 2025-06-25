#DATOS PRIMITIVOS
# Crear una variable de tipo cadena de texto
nombre="Taku Córdoba"
print(type(nombre),nombre)#mostramos el tipo de dato de la variable nombre
# Reemplazar un elemento en una lista
edad=14 #creamos una variable y le asignamos un dato tipo int
print(type(edad),edad)#mostramos el tipo de dato de la variable edad
altura=1.70 #creamos una variable y le asignamos un dato tipo float
print(type(altura),altura)#mostramos el tipo de dato de la variable altura
estudiante=True #creamos una variable y le asignamos un dato tipo boolean
print(type(estudiante),estudiante)#mostramos el tipo de dato de la variable estudiante 
casado=False #creamos una variable y le asignamos un dato tipo boolean
print(type(casado),casado)#mostramos el tipo de dato de la variable casado 
#DATOS COLECCIÓN TIPO LISTA
deportes=["futbol","Tennis","voley","natación","atletismo"]#creamos una variable y le asignamos una lista de deportes

print(deportes)
preguntoDeporteAremplazar=input("Ingrese el deporte a reemplazar: ")
if preguntoDeporteAremplazar in deportes:
    variableGuardaIndiceDeElementoAreemplazar=deportes.index(preguntoDeporteAremplazar)
    deporteRemplaza=input("INGRESE EL DEPORTE POR EL QUE DESEA REEMPLAZAR:")
    deportes[variableGuardaIndiceDeElementoAreemplazar]=deporteRemplaza
    print("El deporte se reemplazó con éxito")
else:
    print("El deporte no se encuentra en la lista")
    
print(deportes)    
    