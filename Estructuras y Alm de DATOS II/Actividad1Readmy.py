zapatillas={"COD1":{"MODELO":"ADIDAS ZAMBA MUJER", "MATERIAL":["CUERO","GOMA","NYLON"],"NÚMERO":38,"CANTIDADSTOCK":39},
            "COD2":{"MODELO":"TOPPER LONA AZÚL", "MATERIAL":["LONA","GOMA","NYLON","ALGODÓN"],"NÚMERO":38,"CANTIDADSTOCK":99},
            "COD3":{"MODELO":"ADIDAS ZAMBA HOMBRE", "MATERIAL":["LONA","GOMA","NYLON","ALGODÓN"],"NÚMERO":38,"CANTIDADSTOCK":99}}

while True:
    opcion=input("Ingrese una de las siguientes opciones: \n1 Mostrar zapatillas en stock \n2 Agregar zapatillas al stock \n3 Salir \n ")
    if opcion=="1":
         print("____________________________________")
         print("-------------Zapatillas-------------")
         print("____________________________________")
         for c,v in zapatillas.items():
             print(c, ":", v)
             print("____________________________________")
    elif opcion=="2":
        zapatillaAgregar=input("Escriba el código de zapatilla a agregar al stock: ") 
        MODELO=input("Escriba el Modelo de zapatilla a agregar : ") 
        MATERIAL=input("Escriba el material de zapatilla a agregar : ") 
        NUMERO=input("Escriba el Número de zapatilla a agregar : ") 
        CANTIDADSTOCK=input("Escriba la cantidad en stock de zapatilla a agregar: ") 
        zapatillas[zapatillaAgregar]=MODELO,MATERIAL,NUMERO,CANTIDADSTOCK
    elif opcion==3:
        break    