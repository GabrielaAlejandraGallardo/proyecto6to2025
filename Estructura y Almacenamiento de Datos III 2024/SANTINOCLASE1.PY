aN=int(input("Ingrese el año de nacimiento que figura en el DNI --->")) # Pregunta al usuario y a la información la guarda en la variable 'aN'  (Int)
   
aA=2024 # Determina la información de 'eN' (int)
e=aA-aN  #Resta los datos 'aN' y 'eN' para sacar el resultado 'e'(int)
if e >=18: #Estructura condicional simple ESTRUCTURA DE DATO ES PRIMITIVO BOOLEAN0 booleano)
   
    print("Puede ingresar al boliche") #Resultado del 'if' que indica que el usuario puede entrar al 'boliche'


elif e<18: # Estructura condicional anidada (Booleano)
   
    print("No puede ingresar al boliche")  #Resultado del 'elif' que indica que el usuario no puede entrar al 'boliche


else: #Estructura condicional compuesta (Booleano)
   
    print("La opcion no es valida") #Resultado del 'else' que indica que la opción no es válida
