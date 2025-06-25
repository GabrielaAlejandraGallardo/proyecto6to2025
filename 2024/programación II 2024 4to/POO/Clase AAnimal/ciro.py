class Animal:
    def __init__(self, especie, edad, color, nombre):
       self.especie = especie
       self.edad = edad
       self.color = color
       self.nombre = nombre
    def mostrar(self):
         print("_____________")
         print("especie:",self.especie, "\nEdad:",self.edad,"\ncolor:",self.color,"\nNombre:",self.nombre)  
animal1 = Animal("gato", 3, "gris", "chimuelo")#cree el primer objeto
animal2 = Animal("loro", 2, "verde","pepo")#cree el segundo objeto
animal3 = Animal("zorro", 5, "naranja", "ciro")#cree el tercer objeto
animal1.mostrar()
animal2.mostrar()
animal3.mostrar()
