class Calzado:
    def __init__(self, fecha_creacion, made_in, marca, tipo, numero, suela ):
        self.fecha_creacion = fecha_creacion
        self.made_in = made_in
        self.marca =  marca
        self.tipo = tipo
        self.numero = numero
        self.suela = suela
    def mostrar(self):
        print(f"made_in: {self.made_in}, marca {self.marca}, tipo {self.tipo}, numero {self.numero}, suela {self.suela}")


class Zapatilla(Calzado):
    def __init__(self, fecha_creacion, made_in, marca, tipo, numero, suela, tipo_deportivo, materiales, modelo, stock):
        super().__init__(fecha_creacion, made_in, marca, tipo, numero, suela)
        self.tipo_deportivo = tipo_deportivo
        self.modelo = modelo
        self. materiales= materiales
        self.stock = stock
    def mostrar(self):
        super().mostrar()
        print( f"tipo de depotivo: {self.tipo_deportivo}, materiales {self.materiales}, modelo {self.modelo}, stock {self.stock}")
    
zapatilla1= Zapatilla("12-08-2020","china", "Adidas", "running", 34,"goma","deportiva","cuero", "pepe", 34)

zapatilla1.mostrar()