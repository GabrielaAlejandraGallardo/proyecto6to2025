Algoritmo sin_titulo //DESARROLLAR UN ALGORITMO QUE PERMITA INGRESAR 2 IMPORTES, LUEGO SUMAR AMBOS IMPORTES Y SI LA
	//SUMA DE AMBOS ES MAYOR A 1000 APLICAR EL 10% MENOS AL TOTAL
	
	Definir i1,i2,total Como Real
	Mostrar "Ingrese primer importe: "
	leer i1
	Mostrar "Ingrese segundo importe: "
	leer i2
	total=i1+i2
	si total >1000 Entonces
		total=total-(total*0.10)
		Mostrar "El total con descuento es: ", total
	FinSi
FinAlgoritmo
