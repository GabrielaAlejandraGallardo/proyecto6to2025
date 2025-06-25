import time

Peliculas_Drama = ['The Hangover', 'Superbad', 'Anchorman', 'Bridesmaids', 'Deadpool'] # Lista con las películas respectivas de cada genero de pelicula
Peliculas_Comedia =['The Shawshank Redemption', 'Forrest Gump', 'Titanic', 'The Godfather', 'Schindler\'s List'] # Lista con las peliculas respectivas de cada genero de pelicula
Peliculas_Suspenso = ['The Exorcist', 'The Shining', 'Psycho', 'Halloween', 'A Nightmare on Elm Street'] # Lista con las películas respectivas de cada genero de pelicula
Peliculas_Temor = ['Se7en', 'The Silence of the Lambs', 'Gone Girl', 'Shutter Island', 'Prisoners'] # Lista con las películas respectivas de cada genero de pelicula

Peliculas= (Peliculas_Comedia,Peliculas_Drama,Peliculas_Suspenso,Peliculas_Temor)

def Funcion_Agregar_Comedia(Pelicula_Comedia):
    Peliculas_Comedia.append(Pelicula_Comedia)
    print("Asi quedo la lista con la modificacion: \n" )
    print(Peliculas_Comedia)

def Funcion_Agregar_Drama():
    Peliculas_Drama.append(Pelicula_Drama)

def Funcion_Agregar_Suspenso():
    Peliculas_Suspenso.append(Pelicula_Suspenso)
    print("Asi quedo la lista con la modificacion: \n" ,Peliculas_Suspenso) 
    
def Funcion_AgregarTemor():
    Peliculas_Temor.append(Pelicula_Temor)

while True:
    Menu_1 = input (" Elija una opcion : \n 1- Cargar Peliculas \n 2- Mostrar peliculas \n 3-Salir \n >>>>")
    if Menu_1 == "1":
        Menu_2 = input ("Cual es el genero de la pelicula que quiere cargar: \n 1-Drama \n 2-Comedia \n 3-Suspenso \n 4-Temor \n >>>>")
        if Menu_2 == "1":
            Pelicula_Drama = input ("¿ Que pelicula quiere agregar ? : ")
            Funcion_Agregar_Drama()
            print("¡Realizado!")
           # time.sleep(3)
            print("Asi quedo la lista con la modificacion: \n" )
        elif Menu_2 == "2":
            Pelicula_Comedia = input ("¿ Que pelicula quiere agregar ? : ")
            Funcion_Agregar_Comedia(Pelicula_Comedia)
            print("¡Realizado!")
          #  time.sleep(3)
           
        elif Menu_2 == "3":
            Pelicula_Suspenso = input ("¿ Que pelicula quiere agregar ? : ")
            Funcion_Agregar_Suspenso(Pelicula_Suspenso)
            print("¡Realizado!")
       #     time.sleep(3)
            print("Asi quedo la lista con la modificacion: \n" ,Peliculas_Suspenso)
        elif Menu_2 == "4":
            Pelicula_Temor = input ("¿ Que pelicula quiere agregar ? : ")
            Funcion_AgregarTemor(Pelicula_Temor)
            print("¡Realizado!")
          #  time.sleep(3)
            print("Asi quedo la lista con la modificacion: \n" ,Peliculas_Temor)
           
        else:
            print("La opcion que ha seleccionado no se encuentra dentro de las opciones")
    elif Menu_1== "2":
        print(Peliculas)
    elif Menu_1== "3":
        print("Saliendo del programa...")
        break
    else:
        print("La opcion que ha seleccionado no se encuentra dentro de las opciones")