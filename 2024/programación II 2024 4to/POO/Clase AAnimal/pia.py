class Animal :
   def __init__(self,idAnimal,ojos,patas,raza):
     self.idAnimal=idAnimal
     self.ojos=ojos
     self.patas=patas
     self.raza=raza
   def mostrar (self):
       print("__________________________________")
       print ("cod Animal:",self.idAnimal,"\nojos:",self.ojos,"\nPatas:",self.patas,"\nRaza:",self.raza )
Animal1=Animal(1,"marron","largas","caniche")#crea el primer objeto
Animal2=Animal(2,"azul","largas","golden")#crea el segundo objeto
Animal3=Animal(3,"negro","cortas","salchicha")#crea el tercer objeto
Animal4=Animal(4,"verde","cortas","pomeranian")#crea el cuarto objeto
Animal1.mostrar()
Animal2.mostrar()
Animal3.mostrar()
Animal4.mostrar()
