"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
donde el usuario ingrese una fruta, un número de kilos y muestre por pantalla el precio de 
ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando
de ello."""
# Diccionario con los precios de las frutas
frutas = {"Manzana": {"Precio": 1500}, "Pera": {"Precio": 800}}
# Inicializar el total
total = 0
totalCompra=0
while True:
    # Solicitar al usuario que ingrese la fruta y la cantidad
    fruta = input("Ingrese la fruta que desea vender: ")
    cant = float(input("Ingrese la cantidad a vender: "))
    # Verificar si la fruta está en el diccionario
    if fruta in frutas:
       # Calcular el total
        total = frutas[fruta]["Precio"] * cant
        totalCompra=totalCompra+total
        print(f"El valor por {cant} kilos de {fruta} es: {total}")
        print("El valor por ",cant,"kilos", "de ",fruta, " es :",total)
    else:
      print("La fruta ingresada no existe en el diccionario")
    respuesta=input("Desea vender otro producto? si/no: ")
    if respuesta=="no":
       break
print("Total de la compra es de: ",totalCompra)





























































