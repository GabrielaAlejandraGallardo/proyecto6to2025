# Definición de la clase Animal
class Animal:
    # Método constructor (__init__) para inicializar las propiedades del animal
    def __init__(self, nombre, edad, raza, historial, datosDuenios):
        # Atributos del animal
        self.nombre = nombre          # Nombre del animal
        self.edad = edad              # Edad del animal
        self.raza = raza              # Raza del animal
        self.historial = historial    # Historial médico o de salud del animal
        self.datosDuenios = datosDuenios  # Información sobre los dueños del animal
    
    # Método para mostrar la información del animal
    def mostrar(self):
        # Imprime los detalles del animal utilizando una cadena formateada
        print(f"NOMBRE {self.nombre}, edad:{self.edad}, raza: {self.raza}, historial: {self.historial}, datosDuenios: {self.datosDuenios}")


# Definición de la clase Gato que hereda de la clase Animal
class Gato(Animal):
    # Método constructor (__init__) para inicializar las propiedades del gato
    def __init__(self, nombre, edad, raza, historial, datosDuenios, orejas, cola, unias):
        # Llamada al constructor de la clase base (Animal) para inicializar las propiedades heredadas
        super().__init__(nombre, edad, raza, historial, datosDuenios)
        # Propiedades adicionales específicas de los gatos
        self.orejas = orejas        # Número de orejas
        self.cola = cola            # Longitud de la cola (o si tiene o no cola)
        self.unias = unias          # Características de las uñas (por ejemplo, "afiladas")
    
    # Método para mostrar la información del gato
    def mostrar(self):
        # Llama al método 'mostrar' de la clase base (Animal) para mostrar la información general
        super().mostrar()
        # Luego imprime las características adicionales del gato (orejas, cola, uñas)
        print(f" Orejas: {self.orejas} COLA: {self.cola}, Unias: {self.unias}")


# Creación de un objeto de la clase Animal
a1 = Animal("pepe", 2, "belga", "garrapatas", "juan, teléfono: 304945855")
# Llamada al método mostrar para imprimir los detalles del objeto 'a1'
a1.mostrar()

# Creación de un objeto de la clase Gato
g1 = Gato("pepito", 2, "siames", "garrapatas y pulgas", "juana, teléfono: 304945345", 2, 1, "filosas")
# Llamada al método mostrar para imprimir los detalles del objeto 'g1' (gato)
g1.mostrar()