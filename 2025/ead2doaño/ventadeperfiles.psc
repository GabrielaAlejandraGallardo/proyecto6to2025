
Algoritmo ventadeperfiles
	definir perfiles Como Entero
	definir precios, total, totalcondescuento como real
	mostrar"cual la cantidad de perfiles que se desea ingresar"
	Leer perfiles
	mostrar"ingrese el precio del perfil por unidad"
	leer precios
	total=precios*perfiles
	si perfiles>=3 Entonces
		totalcondescuento=total*0.3
		totalcondescuento=total-totalcondescuento
		mostrar"el total con el descuento del 30% es: ", totalcondescuento
	SiNo
		mostrar"el total a pagar es : ", total
	FinSi
	
FinAlgoritmo

