numerosEnteros=[]
while True:#se con la funcion break
    numero=int(input("Ingrese un número entero:"))
    numerosEnteros.append(numero)
    if numero==0:
        break
print(numerosEnteros)    
print("El valor mayor es: ")    
print(max(numerosEnteros))