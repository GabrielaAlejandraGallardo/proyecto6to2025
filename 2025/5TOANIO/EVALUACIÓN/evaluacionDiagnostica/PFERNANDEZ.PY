       #Desafio 1
#Se nos pide como programadores, desarrollar un programa con POO para administrar altas de Estudiantes que integrarán una lista de centro de estudiantes.
#Los estudiantes dentro de esta lista realizarán acciones correspondientes a un rol específico QUE DESARROLLARÁN.
#Para resolver el problema derán tener en cuenta primero los atributos relevantes que tiene un integrante de centro de estudiantes, seleccionasol seis (COMO FUNDAMENTALES).
#Una vez definidos los atributos, define la clase que necesita el programa, los objetos que crees necesarios (cantidad de estudiantes miembros de cada lista)
#y define una función para mostrar los datos de cada objeto.




class Estudiante:
    def __init__(self, id, curso, division, name, fullname, yearsold, rol, gmail):
        self.id = id
        self.curso = curso
        self.division = division
        self.name = name
        self.fullname = fullname
        self.yearsold = yearsold
        self.rol = rol
        self.gmail = gmail


    def mostrar_datos(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.curso} {self.division}")
        print(f"Nombre: {self.name} {self.fullname}")
        print(f"Edad: {self.yearsold} años")
        print(f"Rol: {self.rol}")
        print(f"Gmail: {self.gmail}")
        print("------------------------")


class ListaEstudiantes:
    def __init__(self, name_lista):
        self.name_lista = name_lista
        self.estudiantes = []


    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)












    def mostrar_estudiantes(self):
        print(f"Lista de estudiantes: {self.name_lista}")
        for estudiante in self.estudiantes:
            estudiante.mostrar_datos()


lista_estudiantes = ListaEstudiantes("Centro de Estudiantes")


estudiante1 = Estudiante("1972","6to","A","Axel", "Jonas", 17, "Presidente", "axeeelj.perez@example.com")
estudiante1.mostrar_datos()
estudiante2 = Estudiante("7842","6to","A","Lorena", "Minuet", 18, "Vicepresidente", "lorenaminuet.gonzalez@example.com")
estudiante2.mostrar_datos()
estudiante3 = Estudiante("0093","5to","A","Lautaro", "Montiel", 16, "Secretario", "mostiellau@gmail.com")
estudiante3.mostrar_datos()
estudiante4 = Estudiante("0593","5to","A","Samuel", "Nazareth", 17, "Tesorero", "samunazaa@gmail.com")
estudiante4.mostrar_datos()








