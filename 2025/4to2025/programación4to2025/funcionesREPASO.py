def copulativa():
    print("Jesús come manzana y Nacho come naranjas  ")
    repetir=input("Desea repetir función si/no")
    copulativa()
    
def yuxtapuesta():
    return  "Ayer fuí a la plaza, tomé helado con mi amigo"


while True:
    print("________________")
    op=input("menu: \n 1. copulativa \n 2. Yuxtapuesta \n 3.Salir \n ")
    print("________________")
    if op=="1":
        copulativa()
    elif op=="2":
        print(yuxtapuesta())    
        
    elif op=="3":
        print("Saliendo del Programa")
        break
        