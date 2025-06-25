class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
   
    def detalles(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}")


class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento
   
    def detalles(self):
        super().detalles()
        print(f"Departamento: {self.departamento}")


class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, especialidad):
        super().__init__(nombre, edad, salario)
        self.especialidad = especialidad
   
    def detalles(self):
        super().detalles()
        print(f"Especialidad: {self.especialidad}")


gerente1 = Gerente("Lucia", 32, 120000, "Finanzas")
ingeniero1 = Ingeniero("Juan", 30, 150000, "Software")


print("Detalles del Gerente:")
gerente1.detalles()


print("\nDetalles del Ingeniero:")
ingeniero1.detalles()
