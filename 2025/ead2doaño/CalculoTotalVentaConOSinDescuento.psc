Algoritmo CalculoTotalVentaConOSinDescuento
	Definir precio, Subtotal, total Como Real
	Definir unidades Como Entero
    Mostrar "Ingrese la cantidad de producto a vender: "
    leer unidades
	Mostrar  "Ingrese el precio del producto: "
	leer precio
	Subtotal=precio*unidades
	si unidades>=2 Entonces
		Subtotal=Subtotal-(Subtotal*0.20)
		total=Subtotal
		Mostrar "El importe a pagar con descuento es de :", total
		
	SiNo
		Mostrar "El importe a pagar es de :",subtotal
	FinSi
FinAlgoritmo
