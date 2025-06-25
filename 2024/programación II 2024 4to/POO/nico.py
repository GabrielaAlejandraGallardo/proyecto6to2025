class Animal:
   def __init__(self,idAnimal,pelaje,ojo,cola):
       self.idAnimal=idAnimal
       self.pelaje=pelaje
       self.ojo=ojo
       self.cola=cola
   def mostrar(self):
         print("cod Animal:",self.idAnimal,"pelaje:",self.pelaje)


Animal1=Animal(1,"gris","marron","corta")#cree el primer objeto
Animal2=Animal(2,"marron","azul","larga")#cree el segundo objeto
Animal3=Animal(3,"leopardo","verde","larga")#cree el tercer objeto
Animal4=Animal(4,"blaco","celeste","corta")#cree el cuarto objeto
Animal1.mostrar()
Animal2.mostrar()
Animal3.mostrar()
Animal4.mostrar()