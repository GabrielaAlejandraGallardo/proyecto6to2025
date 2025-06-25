class Empleado:#Clase constructora
    def __init__(self, nombre, edad, salario):
        self.nombre=nombre#Aca se crea el objeto
        self.edad=edad
        self.salario=salario


    def detalles(self):
        print("Nombre: ",self.nombre,"\nEdad: ",self.edad,"\nSalario: $",self.salario)
        print("______________________________")




class Gerente(Empleado):
    def __init__(self, nombre, edad, salario,departamento):
        super().__init__(nombre, edad, salario)
        self.departamento=departamento


    def detalles(self):
        print("Departamento: ",self.departamento)
        return super().detalles()
   


class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, especialidad):
        super().__init__(nombre, edad, salario)
        self.especialidad=especialidad


    def detalles(self):
        print("Especialidad: ",self.especialidad)
        return super().detalles()
   


E1= Empleado("Erick",25,30000)
E1.detalles()


E2= Gerente("Amanda",40,150000,"23A")
E2.detalles()


E3= Ingeniero("Robert",54,1000000,"Analista en Sistemas")
E3.detalles()


