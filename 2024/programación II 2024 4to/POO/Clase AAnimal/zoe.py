class Animal:
    
    def __init__(self, especie, edad, nombre, color, tamañoCM, capacidad):
        self.especie = especie
        self.edad = edad
        self.nombre = nombre
        self.color = color
        self.tamañoCM = tamañoCM
        self.capacidad = capacidad
         #funcion que demuestra
    def mostrar(self): 
        print("_________________________")
        print("Especie:",self.especie,"\nEdad:", self.edad, "\nNombre:",self.nombre, "\nColor:",self.color,"\ntañaño:",self.tamañoCM,"\nCapacidad:",self.capacidad)
        #"tiene",animal1.nombre,animal1.color,animal1.tamañoCM,"mide",animal1.capasidad,
   
#Crear cuatro objetos de la clase Animal

animal1=Animal("pulpo",6,"pinti","morado",53,"los tentaculos")
animal2=Animal("caballo",3,"espiritu","blanco con manchas",186,"veloz")
animal3=Animal("toro",10,"franche","marroncito",170,"los cuernos")
animal4=Animal("delfin",4,"serena","azul",120,"inteligencia,habil")


animal1.mostrar()
animal2.mostrar()
animal3.mostrar()
animal4.mostrar()
