#Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases más que hereden de Fabrica,
# las cuales son Moto y Carro.
#Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
# Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno.
#Agregar una funcion que determine un descuento del 10% en el precio de llanta mayor a 100.000 pesos
class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()



class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

print("OBJETO = moto")
moto = Moto(2, "Gris", 200000)
moto.cantidad()
moto.precioConDescuento()

print("OBJETO = carro")
carro = Carro(4, "Negro", 60000)
carro.cantidad()
carro.precioConDescuento()


