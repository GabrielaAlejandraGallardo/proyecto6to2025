class Animal:
    def __init__(self, especie, edad, color):
        self.especie = especie
        self.edad = edad
        self.color = color
    def mostrar(self):
        print("::::::::::::::::::::::")
        print("Especie:",self.especie,"\nEdad:",self.edad,"\nColor:", self.color)


animal1 =Animal("Marmota", 4, "marron")
animal2 =Animal("Hurón", 6, "gris")
animal3 =Animal("Hipopotamo", 3, "Marron")
animal4 =Animal("Ardilla", 2, "anaranjada")


animal1.mostrar()
animal2.mostrar()
animal3.mostrar()
animal4.mostrar()
