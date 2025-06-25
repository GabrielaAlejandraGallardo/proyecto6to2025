class Animal:
    def __init__(self, nombre, especie, edad, color):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.color = color
    def mostrar(self):
        print("____________________")
        print("Nombre:", self.nombre,"\nEspecie:", self.especie, "\nEdad:",self.edad,"\nColor:", self.color)    


# Crear objetos de la clase Animal
animal1 = Animal("Facu", "Perro", 5, "Marrón")
animal2 = Animal("Martin", "Gato", 3, "Gris")
animal3 = Animal("Dumbo", "Elefante", 10, "Gris")
animal4 = Animal("Tomy", "Pájaro", 2, "Amarillo")


# mostrarr información de los animales

animal1.mostrar()
animal2.mostrar()
animal3.mostrar()
animal4.mostrar()
"""
print("Información del animal 1:")
print("Nombre:", animal1.nombre)
print("Especie:", animal1.especie)
print("Edad:", animal1.edad)
print("Color:", animal1.color)
print()


print("Información del animal 2:")
print("Nombre:", animal2.nombre)
print("Especie:", animal2.especie)
print("Edad:", animal2.edad)
print()


print("Información del animal 3:")
print("Nombre:", animal3.nombre)
print("Especie:", animal3.especie)
print("Edad:", animal3.edad)
print("Color:", animal3.color)
print()


print("Información del animal 4:")
print("Nombre:", animal4.nombre)
print("Especie:", animal4.especie)
print("Edad:", animal4.edad)
print("Color:", animal4.color)

"""