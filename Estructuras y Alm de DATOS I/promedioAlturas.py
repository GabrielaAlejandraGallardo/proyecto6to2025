"""Crear un algoritmo que permita ingresar 4 alturas 
//y luego muestre el promedio de alturas
Algoritmo ejercicio1
	Definir a1,a2,a3,a4, promedio Como Real
	Mostrar "Ingrese la primer altura: "
	leer a1
	Mostrar "Ingrese la segunda altura: "
	leer a2
	Mostrar "Ingrese la tercer altura: "
	leer a3
	Mostrar "Ingrese la cuarta altura:"
	leer a4
	promedio=(a1+a2+a3+a4)/4
	Mostrar "La altura promedio es de : ",promedio
FinAlgoritmo"""
a1=float(input("Ingrese la 1er altura: "))
a2=float(input("Ingrese la 2da altura: "))	
a3=float(input("Ingrese la 3er altura: "))
a4=float(input("Ingrese la 4ta altura: "))

promedio=(a1+a2+a3+a4)/4

print("El promedio de alturas es de: ", promedio)