class Fabricante:
        def __init__(self,idFabricante,nombre):
             self.idFabricante=idFabricante
             self.nombre=nombre
                          
                          
                          
                          
        #Definimos la función mostrarDatos que imprime los atributos del fabricante
        #Esta función no recibe parámetros, ya que utiliza los atributos de la instancia actual (self)
        def mostrarDatos(self):
            print("ID del Fabricante:", self.idFabricante)
            print("Nombre del Fabricante:", self.nombre)
#Definimos la clase Fabricante con un constructor que recibe dos parámetros: idFabricante y nombre.
          
fabricante1=Fabricante(1,"Samsung")
fabricante2=Fabricante(2,"Apple")
fabricante3=Fabricante(3,"Huawei")

print(fabricante1.idFabricante,fabricante1.nombre)
#LLAMO A LA FUNCIÓN mostrarDatos() DE LA CLASE Fabricante PARA IMPRIMIR LOS DATOS DEL FABRICANTE
fabricante1.mostrarDatos()

print(fabricante2.idFabricante,fabricante2.nombre)
print(fabricante3.idFabricante,fabricante3.nombre)
#El código define una clase Fabricante con un constructor que inicializa dos atributos: idFabricante y nombre.