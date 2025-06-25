Algoritmo ventaPerfiles
	Definir  cantPerfiles Como Entero
	Definir precioPorUnidad, totalApagar, totalConDescuento Como Real
	Mostrar  "Ingrese la cantidad de perfiles:"
	leer cantPerfiles
	Mostrar "Ingrese el precio de perfil por unidad:"
	Leer precioPorUnidad
	totalApagar=cantPerfiles*precioPorUnidad
	si cantPerfiles>=3 Entonces
		totalConDescuento=totalApagar-(totalApagar*0.30)
		//totalConDescuento=totalApagar-totalConDescuento
		Mostrar "TOTAL A PAGAR CON DESCUENTO DEL 30%: ",totalConDescuento
    SiNo
		Mostrar "El total a pagar es : ", totalApagar
	FinSi
FinAlgoritmo
