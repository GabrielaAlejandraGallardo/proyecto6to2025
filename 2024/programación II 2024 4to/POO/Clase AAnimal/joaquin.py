class Animales:
   def __init__(self, idAnimales, lengua, patas, dientes, cola, orejas, nariz, ojos, garras, pelaje):
       self.idAnimales = idAnimales
       self.lengua = lengua
       self.patas = patas
       self.dientes = dientes
       self.cola = cola
       self.orejas = orejas
       self.nariz = nariz
       self.ojos = ojos
       self.garras = garras
       self.pelaje = pelaje
  
   def mostrar(self):
       print("ID:", self.idAnimales, "ojos:", self.ojos, "patas:", self.patas, "pelaje:", self.pelaje, "cola:", self.cola, "orejas:", self.orejas, "nariz:", self.nariz, "garras:", self.garras, "lengua:", self.lengua)


# Crear animales
perro = Animales(1, 2, 4,"pelo","marron","corto")
oso = Animales(2, 2, 4, "pelo","marron""largo")
gaviota = Animales(3, 2, 2, "plumaje","blannco","plumoso")
lobo = Animales(4, 2, 4, "pelo","gris","corto")


# Mostrar los atributos de los animales
perro.mostrar()
oso.mostrar()
gaviota.mostrar()
lobo.mostrar()





