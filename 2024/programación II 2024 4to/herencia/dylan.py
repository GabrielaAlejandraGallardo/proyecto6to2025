class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio


    def printname(self):
        print(self.marca, self.modelo, self.anio, self.color, self.ruedas)


class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas, color):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas
        self.color = color


class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, color, ruedas):
        super().__init__(marca, modelo, anio)
        self.ruedas = ruedas
        self.color = color


    def printname(self):
        super().printname()


x1 = Moto("motomel", "mk1", "2009", "rojo", "4")
x1.printname()
