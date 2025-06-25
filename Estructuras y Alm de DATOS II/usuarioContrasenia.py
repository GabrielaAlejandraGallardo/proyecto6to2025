##c=input("INGRESE SU CONTRASENIA: ")
contador=1
u=""
c=""
while u!="pepe" or c!="1234" and contador<4:
    print("________________________________")
    u=input("INGRESE SU NOMBRE DE USUARIO: ")
    c=input("INGRESE SU CONTRASENIA: ")
    print(" Vuelta Numero: ",contador)
    contador=contador+1
    
    if u=="pepe" and c=="1234":
       print("Bienvenido al sistema")
    else:
       print("Usted no puede ingresar al sistema")   
   
    