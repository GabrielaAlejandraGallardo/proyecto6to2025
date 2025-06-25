class Empleado:
    def __init__(self, nombre, edad, salario):
       self.nombre = nombre
       self.edad = edad
       self.salario = salario


    def detalles(self):
       print(f"Nombre: {self.nombre}")
       print(f"Edad: {self.edad}")
       print(f"Salario: {self.salario}")




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
       print(f"especialidad: {self.especialidad}")
      

gerente1 = Gerente("Juan", 35, 60000, "Ventas")
print("Detalles del Gerente:")
gerente1.detalles()
ingeniero1 = Ingeniero("María", 28, 50000, "Desarrollo")


ingeniero1.detalles()