listaEstudiantes = [["Camili","Lopez", 23423435]]

def añadeElementos(listaEstudiantes):
    n = input("Ingrese su nombre: ")
    a = input("Ingrese su apellido: ")
    d = input("Ingrese su DNI: ")
    listaEstudiantes.append([n, a, d])  # Agrupar los valores en una lista
    opcionderecursividad=input("Desea añadir otro elemento si/no: ")
    if opcionderecursividad=="si":  #funcion recursiva, que se llama así misma
        añadeElementos(listaEstudiantes)
        
def mostrarEstudiantes(listaEstudiantes):
   for i in listaEstudiantes:
      print(i)    

#print(listaEstudiantes)

#rta="si"       
while True:#rta=="si":      
    opcion=int(input("\n Menú de Opciones\n 1-AÑADIR ESTUDIANTE A LA LISTA\n 2-MOSTRAR ESTUDIANTES EN LA LISTA\n 3-Salir \n"))
    if opcion==1:
        
        añadeElementos(listaEstudiantes)
    elif opcion==2:    
        mostrarEstudiantes(listaEstudiantes)
    else:
        print("Saliendo del sistema....")
        break
            

   
   