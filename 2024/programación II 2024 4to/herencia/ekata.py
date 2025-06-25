class Empleado:
      """Clase base para representar a un empleado en una empresa."""

    def __init__(self, nombre, edad, salario):
    """Constructor que inicializa los atributos del empleado."""
       self.nombre = nombre
       self.edad = edad
   

    def detalles(self):
    """Método que imprime los detalles del empleado."""
       print(f"Nombre: {self.nombre}")
       print(f"Edad: {self.edad}")
       print(f"Salario: {self.salario}")


class Gerente(Empleado):
  """Clase que representa a un gerente en una empresa."""


  def __init__(self, nombre, edad, salario, departamento):
    """Constructor que inicializa los atributos del gerente, heredando de la clase Empleado."""
    super().__init__(nombre, edad, salario)
    self.departamento = departamento


  def detalles(self):
    """Método que sobrescribe el método detalles de la clase base para incluir el departamento."""
    super().detalles()
    print(f"Departamento: {self.departamento}")


class Ingeniero(Empleado):
  """Clase que representa a un ingeniero en una empresa."""


  def __init__(self, nombre, edad, salario, especialidad):
    """Constructor que inicializa los atributos del ingeniero, heredando de la clase Empleado."""
    super().__init__(nombre, edad, salario)
    self.especialidad = especialidad


  def detalles(self):
    """Método que sobrescribe el método detalles de la clase base para incluir la especialidad."""
    super().detalles()
    print(f"Especialidad: {self.especialidad}")


# Crear instancias de Gerente e Ingeniero
gerente1 = Gerente("Gabriel Montes", 45, 50000, "Ventas")
ingeniero1 = Ingeniero("Maite Bustos", 32, 42000, "Software")


# Llamar al método detalles para cada instancia
gerente1.detalles()
ingeniero1.detalles()



