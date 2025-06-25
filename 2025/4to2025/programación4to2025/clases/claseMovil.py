class Movil:
    def __init__(self, movil_id, fabricante_id, codigo, modelo):
        self.movil_id = movil_id
        self.fabricante_id = fabricante_id
        self.codigo = codigo
        self.modelo = modelo
    def mostrarDatos(self):    
        print("ID del Móvil:", self.movil_id)
        print("ID del Fabricante:", self.fabricante_id)
        print("Código del Móvil:", self.codigo)
        print("Modelo del Móvil:", self.modelo)
        print("=====================================")
        
m1=Movil(1, 1, "SM-G991B", "Galaxy S21")


m2=Movil(2, 2, "iPhone13,3", "iPhone 12")        
print(m1.movil_id, m1.fabricante_id, m1.codigo, m1.modelo)
m1.mostrarDatos()
m2.mostrarDatos()
