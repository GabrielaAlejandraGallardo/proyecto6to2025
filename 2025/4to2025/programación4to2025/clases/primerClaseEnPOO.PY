class Person:#Definimos la clase persona
    #Definimos la función inicializadora que recibe 2 atributos como parámetros
  def __init__(self, name, age):#self hace referencia a si mismo en el valor de atributos de cada objeto
      #que se está construyendo
    self.name = name #defino name seguido de self para guardar el valor del atributo name
    self.age = age#defino atributi age seguido de self para guardar el valor del atributo age
#Creamos un objeto de la clase persona llamando a la función inicializadora y pasandole 2 argumentos como valor
p1 = Person("John", 36)

print(p1.name)#imprimimos en pantalla el valor de name del objeto p1
print(p1.age)#imprimimos en pantalla el valor de age del objeto p1
