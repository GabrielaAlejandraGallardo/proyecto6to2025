class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Salario Base: {self.salario_base}")

class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono_anual):
        super().__init__(nombre, salario_base)
        self.bono_anual = bono_anual

    def calcular_salario(self):
        return self.salario_base + self.bono_anual

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Bono Anual: {self.bono_anual}")

# Similar para Desarrollador y Diseñador