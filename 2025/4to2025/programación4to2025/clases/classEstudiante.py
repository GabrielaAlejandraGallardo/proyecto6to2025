class Estudiante:
    def __init__(self,id, nombre, apellido):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
    """def mostrarDatos(self):    
        print("ID del Estudiante:", self.id)
        print("Nombre del Estudiante:", self.nombre)
        print("Apellido del Estudiante:", self.apellido)
        print("=====================================")  """
    def __str__(self):
        return"ID del Estudiante:", self.id,"Nombre del Estudiante:", self.nombre,"Apellido del Estudiante:", self.apellido 
            
        
e1=Estudiante(1, "Juan", "Pérez",)
e2=Estudiante(2, "Ana", "Gómez")
print(Estudiante.__str__(e1))
print(Estudiante.__str__(e2))   


