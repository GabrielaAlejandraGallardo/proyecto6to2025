# Definición de la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
   
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}")




# Definición de la clase derivada Auto
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas
   
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Puertas: {self.puertas}")




# Definición de la clase derivada Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada
   
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Cilindrada: {self.cilindrada} cc")




# Ejemplo adicional de clase derivada Camioneta (opcional)
class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, año, carga):
        super().__init__(marca, modelo, año)
        self.carga = carga
   
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Capacidad de Carga: {self.carga} kg")




# Instanciación de objetos y prueba de la herencia
def main():
    # Creación de objetos
    auto1 = Auto("renault ", "12", 1994, 4)
    moto1 = Motocicleta("yamaha", "R7", 2022, 450)
    camioneta1 = Camioneta("ram 1500", "trx", 2024, 950)


    # Mostrar información de los vehículos
    print("Información del Auto:")
    auto1.mostrar_informacion()


    print("\nInformación de la Motocicleta:")
    moto1.mostrar_informacion()


    print("\nInformación de la Camioneta:")
    camioneta1.mostrar_informacion()


if __name__ == "__main__":
    main()


