n=input("Ingrese un número para sumar sus digitos:")# "23"
lista=list(n)#["2","3"]
suma=0
for digito in lista:
    suma=suma+int(digito)#2+3
print(suma)    