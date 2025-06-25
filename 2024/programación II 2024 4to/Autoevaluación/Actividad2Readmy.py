"""Actividad 2: Crear un programa que contenga los datos personales de personas que forman parte de una escuela: estudiantes y docentes. 
Deberas identificar los siguientes atributos y aplicarlos a Clases en POO: matricula, dni, 
nombreApellido, direccion, anioCurso, materias, cursosAcargo. crear funciones para mostrar sus datos. Crear 3 objetos para cada clase"""
class Persona:# Inicio y creacion de la clase Persona
    def __init__(self, dni, nombreApellido, direccion): # Constructor de la clase
        self.dni = dni  # Número de documento de identidad
        self.nombreApellido = nombreApellido  # Nombre completo
        self.direccion = direccion  # Dirección

    def mostrarDatos(self): # Variable mostrar datos de la clase persona
        print(f"DNI: {self.dni}")
        print(f"Nombre y Apellido: {self.nombreApellido}")
        print(f"Dirección: {self.direccion}")

class Estudiante(Persona): # Inicio y creacion de la clase Estudiante que deriva de la clase Persona
    def __init__(self, dni, nombreApellido, direccion, matricula, anioCurso, materias):
        super().__init__(dni, nombreApellido, direccion)
        self.matricula = matricula  # Número de matrícula
        self.anioCurso = anioCurso  # Año en el que cursa
        self.materias = materias  # Lista de materias cursadas

    def mostrarDatos(self): # Variable mostrar datos de la clase Estudiante
        super().mostrarDatos()
        print("---------------\n ESTUDIANTES\n---------------")
        print(f"Matrícula: {self.matricula}")
        print(f"Año: {self.anioCurso}")
        print(f"Materias: {self.materias}")

class Docente(Persona): # Inicio y creacion de la clase Docente que deriva de la clase Persona
    def __init__(self, dni, nombreApellido, direccion, cursosAcargo):
        super().__init__(dni, nombreApellido, direccion)
        self.cursosAcargo = cursosAcargo  # Lista de cursos a cargo

    def mostrarDatos(self):
        super().mostrarDatos()
        print("---------------\n DOCENTES\n---------------")
        print(f"Cursos a cargo: {self.cursosAcargo}")

# Crear objetos
estudiante1 = Estudiante("12345678", "Juan Mujica", "Av. Siempreviva 123", "1234", 3, ["Programación", "Diseño de Interfaces y Usabilidad","Matemática", "Lengua","Ingles Ap", "Ingles"])  # Un estudiante
estudiante2 = Estudiante("87654321", "Santiago Arias", "Calle Sesamo 456", "5678", 2, ["Programación", "Diseño de Interfaces y Usabilidad","Lengua","Club Ciencias", "Historia","Ingles Ap", "Ingles"])
estudiante3 = Estudiante("98765432", "Josefina Navarro", "Calle de la cuenca del sol 789", "9876", 1, ["Programación", "Diseño de Interfaces y Usabilidad""Lengua","Música","Ingles Ap", "Ingles"])

docente1 = Docente("54321987", "Yanina Ponce", "Calle de los Olmos 101", ["Ingles Ap", "Ingles"])  # Un docente
docente2 = Docente("21987543", "Gabriela Gallardo", "Avenida del Mar 123", ["Programación", "Diseño de Interfaces y Usabilidad"])
docente3 = Docente("98765432", "Emilse Sanchez", "Calle de los Robles 456", ["Matematica"])

# Mostrar datos de un estudiante
estudiante1.mostrarDatos()
estudiante2.mostrarDatos()
estudiante3.mostrarDatos()

docente1.mostrarDatos()
docente2.mostrarDatos()
docente3.mostrarDatos()