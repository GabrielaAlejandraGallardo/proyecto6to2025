"""https://colab.research.google.com/drive/1H9qiHtXhrd8LIYYOm2JvYfP7qqW-S_YW?usp=sharing
Crear un programa que permita llevar un control stock de equipos deportivos donde todos tendran una fecha de creación, un precio, una descripción. 
precio_costo,precio_venta y cantidad en stock.
 Deberá tener una función donde se pueda ingresar para un objeto una determinada cantidad vendida la cual deberá ser descontada de la cantidad en stock.
  El programa, deberá imprimir los datos de cada clase creada 
y si hubo ventas de uno o varios objeto en particular fueron vendidos, deberá mostrar la cantidad original y la cantidad luego de ejetura venta.
"""
class EquipoDeportitvo:
    def __init__(self, codEquipo,fechaCreacion,descripcion,precio_costo,precio_venta, cantidadStock, cantidadVendida):
        self.codEquipo=codEquipo
        self.fechaCreacion=fechaCreacion
        self.descripcion=descripcion 
        self.precio_costo= precio_costo
        self.precio_venta= precio_venta
        self.cantidadStock=cantidadStock
        self.cantidadVendida=cantidadVendida
        
    def mostrar(self):    
        print(f"codEquipo: {self.codEquipo} fechaCreacion: {self.fechaCreacion}  descripcion: {self.descripcion} precio_costo: {self.precio_costo} precio_venta: {self.precio_venta} cantidadStock {self.cantidadStock} cantidadVendida: {self.cantidadVendida}")
 
    def vendidos(self):
        vendido=input("Ingrese el código de equipo vendido: ")
        cv=int(input("Ingrese la cantidad vendida"))
        for e in EquipoDeportitvo:
           if vendido in EquipoDeportitvo:
              self.cantidadVendido=self.cantidadVendida-cv
e1=EquipoDeportitvo("e1","12/03/2023","Equipo pantalon, remera y campera mujer basquet",10,12,30,0) 
e1.mostrar()
e1.vendidos()              
               
            
 
 
 
 