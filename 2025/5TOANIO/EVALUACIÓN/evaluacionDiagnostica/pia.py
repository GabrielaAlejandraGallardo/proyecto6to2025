class Estudiante:
    def __init__(self, nombre, edad, id_estudiante, rol, carrera, fecha_ingreso):
        self.nombre = nombre
        self.edad = edad
        self.id_estudiante = id_estudiante
        self.rol = rol
        self.carrera = carrera
        self.fecha_ingreso = fecha_ingreso


    def mostrar_datos(self):
        """
        Muestra los datos del estudiante.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"ID: {self.id_estudiante}")
        print(f"Rol: {self.rol}")
        print(f"Carrera: {self.carrera}")
        print(f"Fecha de ingreso: {self.fecha_ingreso}")
        print("_______________________________________")

e1=Estudiante("Gustavo Pereyra", 20, 1, "Presidente", "Ingeniería", "2023-03-01")
e1.mostrar_datos()
e2=Estudiante("Martina Gómez", 22, 2, "Tesorera", "Arquitectura", "2022-06-15")
e2.mostrar_datos()
# Lista para almacenar los estudiantes
#####estudiantes_lista = []

"""
# Función para agregar estudiantes
def agregar_estudiante(nombre, edad, id_estudiante, rol, carrera, fecha_ingreso):
    nuevo_estudiante = Estudiante(nombre, edad, id_estudiante, rol, carrera, fecha_ingreso)
    estudiantes_lista.append(nuevo_estudiante)


# Ejemplo de agregar estudiantes
agregar_estudiante("Gustavo Pereyra", 20, 1, "Presidente", "Ingeniería", "2023-03-01")
agregar_estudiante("Martina Gómez", 22, 2, "Tesorera", "Arquitectura", "2022-06-15")
agregar_estudiante("Benicio Ponce", 20, 3, "Tesorero", "Abogado", "2017-05-15")
agregar_estudiante("Agustin Campos" , 16,6 ,"Vocal 1","Programador", "2025-03-01")


# Mostrar los datos de todos los estudiantes
for estudiante in estudiantes_lista:
    estudiante.mostrar_datos()
    print("-" * 20)"""