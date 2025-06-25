class Vehiculos:
    def __init__(self, marca, modelo, year):
        self.marca=marca
        self.modelo=modelo
        self.year=year
   
    def printname(self):
        print(self.marca,self.modelo,self.year)




    def mostrar(self):
        print("Marca: ", self.marca, "\nModelo: ",self.modelo,"\nYear: ", self.year)
        print("______________________________________")




class Autos(Vehiculos):
    def __init__(self, marca, modelo, year, matricula, color, capacidad):
        super().__init__(marca, modelo, year)




        self.matricula=matricula
        self.color=color
        self.capacidaddepersonas=capacidad




    def printname(self):
        print(self.matricula,self.color,self.capacidaddepersonas)




    def mostrar(self):
        print("Matricula: ", self.matricula,"\nColor: ", self.color,"\nCapacidad de Personas: ", self.capacidaddepersonas)
        return super().mostrar()
   
class Motos(Vehiculos):
    def __init__(self, marca, modelo, year, color, tipo, cilindrada):
        super().__init__(marca, modelo, year)


        self.color=color
        self.tipo=tipo
        self.cilindrada=cilindrada


    def printname(self):
        print(self.color,self.tipo,self.cilindrada)


    def mostrar(self):
        print("Color: ",self.color,"\nTipo: ",self.tipo,"\nCilindrada: ",self.cilindrada)
        return super().mostrar()
   
class Camiones(Vehiculos):
    def __init__(self, marca, modelo, year, capacidaddecarga, kilometros):
        super().__init__(marca, modelo, year)


        self.capacidadecarga=capacidaddecarga
        self.kilometros=kilometros


    def printname(self):
        print(self.capacidadecarga,self.kilometros)


    def mostrar(self):
        print("Capacidad de Carga: ",self.capacidadecarga,"\nKilometros: ",self.kilometros)
        return super().mostrar()  


V1= Autos("Mercedes","AMG-GT",2014,"T53PO","Amarillo","2 personas")


V2= Motos("Honda", "CBR 600 RR", 2018,"Rojo","Deportiva", 600)


V3= Camiones("Iveco","Tector",2017,"55 t",164000)




V1.mostrar()
V2.mostrar()
V3.mostrar()
class Vehiculos:
    def __init__(self, marca, modelo, year):
        self.marca=marca
        self.modelo=modelo
        self.year=year
   
    def printname(self):
        print(self.marca,self.modelo,self.year)




    def mostrar(self):
        print("Marca: ", self.marca, "\nModelo: ",self.modelo,"\nyear: ", self.year)
        print("______________________________________")




class Autos(Vehiculos):
    def __init__(self, marca, modelo, year, matricula, color, capacidad):
        super().__init__(marca, modelo, year)




        self.matricula=matricula
        self.color=color
        self.capacidaddepersonas=capacidad




    def printname(self):
        print(self.matricula,self.color,self.capacidaddepersonas)




    def mostrar(self):
        print("Matricula: ", self.matricula,"\nColor: ", self.color,"\nCapacidad de Personas: ", self.capacidaddepersonas)
        return super().mostrar()
   
class Motos(Vehiculos):
    def __init__(self, marca, modelo, year, color, tipo, cilindrada):
        super().__init__(marca, modelo, year)


        self.color=color
        self.tipo=tipo
        self.cilindrada=cilindrada


    def printname(self):
        print(self.color,self.tipo,self.cilindrada)


    def mostrar(self):
        print("Color: ",self.color,"\nTipo: ",self.tipo,"\nCilindrada: ",self.cilindrada)
        return super().mostrar()
   
class Camiones(Vehiculos):
    def __init__(self, marca, modelo, year, capacidaddecarga, kilometros):
        super().__init__(marca, modelo, year)


        self.capacidadecarga=capacidaddecarga
        self.kilometros=kilometros


    def printname(self):
        print(self.capacidadecarga,self.kilometros)


    def mostrar(self):
        print("Capacidad de Carga: ",self.capacidadecarga,"\nKilometros: ",self.kilometros)
        return super().mostrar()  


V1= Autos("Mercedes","AMG-GT",2014,"T53PO","Amarillo","2 personas")


V2= Motos("Honda", "CBR 600 RR", 2018,"Rojo","Deportiva", 600)


V3= Camiones("Iveco","Tector",2017,"55 t",164000)




V1.mostrar()
V2.mostrar()
V3.mostrar()
