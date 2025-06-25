#Torneo de deportes

deportesTorneoFebrero=["futbol","Basquet"]
i=0
def agregarDeporte(deportesTorneoFebrero):
   deporteAagregarAlista=input("Ingrese nuevo deporte:")
#if "futbol" in deportesTorneoFebrero:
 #deportesTorneoFebrero.remove("futbol")
   if deporteAagregarAlista in deportesTorneoFebrero:
    print("El deporte agregado ya está en la lista")
 #deportesTorneoFebrero.remove("futbol")
   else:
    deportesTorneoFebrero.append(deporteAagregarAlista) 
    
rta="si" 
while rta=="si":
 rta=input("Escriba el nombre del deporte a agregar:")
 agregarDeporte(deportesTorneoFebrero)
 rta=input("Desea ingresar otro deporte a la lista del torno si o no:")
 if rta=="no":
     print("gracias por participar de la organización del torneo")

for deporte in deportesTorneoFebrero:
  i=i+1
  print(i,deporte)
  
  