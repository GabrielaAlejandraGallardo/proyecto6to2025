
peliculas = {
   "Drama": [],
   "Comedia": [],
   "Suspenso": [],
   "Terror": []
} #Se crea el diccionario.




def cargar_pelicula(): #Se crea la función def para cargas las películas.
   genero = input("Ingrese el género de la película (Drama, Comedia, Suspenso, Terror): ") #Se pide que se ingrese el género.
   nombre_pelicula = input("Ingrese el nombre de la película: ") #Pide el nombre de la película.
   peliculas[genero].append(nombre_pelicula) #Películas guarda lo que se guarda en nombre_pelicula.
   print("Película cargada exitosamente.") #Muestra que se guardó bien.




def mostrar_peliculas(): #Se crea un def para mostrar peliculas.
      for genero, lista_peliculas in peliculas.items(): 
          print("\nPeliculas en el genero", genero)
          for pelicula in lista_peliculas:
              print("-", pelicula) #Muestra las películas ordenadamente en el género que corresponde.
             
def menu():
   while True: #Crea un while para seleccionar la opción que desea.
       print("\nMenu:")
       print("1. Cargar película")
       print("2. Mostrar películas")
       print("3. Salir")
       opcion = input("Seleccione una opción: ")




       if opcion == "1": #Lee la opción que seleccionó.
           cargar_pelicula()
       elif opcion == "2":
           mostrar_peliculas()
       elif opcion == "3":
           print("Hasta luego.")
           break 
       else:
           print("Opción no válida. Por favor, seleccione una opción válida.") #Si no se selecciono una opción correcta pide que vuelvas a intentarlo.
menu()