#DESARROLLAR UN ALGORITMO QUE PERMITA INGRESAR 2 IMPORTES, LUEGO SUMAR AMBOS IMPORTES Y El RESULTADO

#explicación:
#VARIABLE  convierte el tipo de datos de string(cadena) a float (Real) el valor que ingrese el usuario se guarda en variable
importe1=float(input("Ingrese primer importe: "))
importe2=float(input("Ingrese segundo importe: "))
#realiza la operación suma y en la v ariable toltal se guarda el resultado de la suma de ambos importes
total=importe1+importe2
#Muestra en pantalla el total uniendo el carter entre parentesis a la variable total por medio de coma
print("el total es: ",total)
