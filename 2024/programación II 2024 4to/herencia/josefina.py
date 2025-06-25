class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio




    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}")




class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas


    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Puertas: {self.puertas}")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, cilindrada):
        super().__init__(marca, modelo, anio)
        self.cilindrada = cilindrada


    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Cilindrada: {self.cilindrada}")
        
        """Paso 4: Ampliar la jerarquía de clases (opcional)
Añade otra clase derivada, por ejemplo, `CamiónCamion`, que también herede de `Vehiculo`, e incluye atributos y métodos específicos para esta clase.

"""
class Camion(Vehiculo):
    
    def __init__(self, marca, modelo, anio, capacidad_carga):
        super().__init__(marca, modelo, anio)
        self.capacidad_carga = capacidad_carga
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Cadacidad de Carga: {self.capacidad_carga}")
   

# Ejemplo de uso:
mi_auto = Auto("Ford", "Focus", 2023, 4)
mi_auto.mostrar_informacion()


mi_moto = Motocicleta("Honda", "CBR", 2021, "500 cc")
mi_moto.mostrar_informacion()

mi_camion=Camion("Fiat","IVECO",1998,3000)
mi_camion.mostrar_informacion()






