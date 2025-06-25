class Vehiculo:
   def __init__(self, marca, modelo, anio):
       self.marca = marca
       self.modelo = modelo
       self.anio = anio




   def mostrar_informacion(self):
       print(f"Marca: {self.marca}")
       print(f"Modelo: {self.modelo}")
       print(f"Año: {self.anio}")








#Clase derivada que representa un automóvil.




class Auto(Vehiculo):
   def __init__(self, marca, modelo, anio, tipo_carroceria, num_puertas):
       super().__init__(marca, modelo, anio)
       self.tipo_carroceria = tipo_carroceria
       self.num_puertas = num_puertas




   def mostrar_informacion_completa(self):
       self.mostrar_informacion()
       print(f"Tipo de carrocería: {self.tipo_carroceria}")
       print(f"Número de puertas: {self.num_puertas}")








#Clase derivada que representa una motocicleta.
class Motocicleta(Vehiculo):
 
   def __init__(self, marca, modelo, anio, cilindrada):
       super().__init__(marca, modelo, anio)
       self.cilindrada = cilindrada




   def mostrar_informacion_completa(self):
       self.mostrar_informacion()
       print(f"Cilindrada: {self.cilindrada}")




#Clase derivada que representa un camión.
class Camion(Vehiculo):
   def __init__(self, marca, modelo, anio, capacidad_carga):
       super().__init__(marca, modelo, anio)
       self.capacidad_carga = capacidad_carga




   def mostrar_informacion_completa(self):
       self.mostrar_informacion()
       print(f"Capacidad de carga: {self.capacidad_carga} toneladas")




auto1 = Auto("Toyota", "Corolla", 2020, "Sedán", 4)
moto1 = Motocicleta("Honda", "CBX250", 2018, 250)
camion1 = Camion("Iveco", "Tector", 2022, 10)




auto1.mostrar_informacion_completa()
print("--------------------------")
moto1.mostrar_informacion_completa()
print("--------------------------")
camion1.mostrar_informacion_completa()


