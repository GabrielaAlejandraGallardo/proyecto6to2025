class Animal:
    def __init__(self, especie, edad, color, tamaño):
        self.especie = especie
        self.edad = edad
        self.color = color
        self.tamaño = tamaño
    def mostrar(self):
        print("..........................")
        print("Especie:",self.especie,"\nEdad:", self.edad,  "\nColor:",self.color,"\tamaño:",self.tamaño)


#Crear cuatro objetos de la clase Animal
animal1 = Animal("lemur", 20,"gris con blanco y rayas negras",50)
animal2 = Animal("pinguino", 20, "negro y blanco",111)
animal3 = Animal("vaca", 25,"marroncita y con manchas blanca",150)
animal4 = Animal("ballena", 90,"azulado",18)




animal1.mostrar()
animal2.mostrar()
animal3.mostrar()
animal4.mostrar()

