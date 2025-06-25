//Situación problemática: Conversión de grados Celsius a Fahrenheit
//Un laboratorio de meteorología necesita convertir la temperatura registrada en grados Celsius a grados Fahrenheit. 
//El programa debe pedir al usuario que ingrese una temperatura en Celsius y mostrar la conversión a Fahrenheit.
//La fórmula es:
//Fahrenheit = (Celsius × 9/5) + 32


Algoritmo pasarDeGradosCelsiusAfahrenheit
	Definir celsius, Fahrenheit  Como Real //define las variables Celsius que guardará el valor de los mismos y Fahrenheit que guarda el resultado
	//de ejegutar la fórmula
	Mostrar "Ingrese los grados celsius que desea convertir en Fahrenheit: "//cartel que pide se ejecute una acción en este caso ingresar
	//grados celsius
	leer celsius //lee lo que ingreso el usuario y lo guarda en celsius
	Fahrenheit = (Celsius * 9/5) + 32 //se guarda en la variable Fahrenheit el resultado de la formula de conversion de celsius a Fahrenheit
	Mostrar "En Fahrenheit", Celsius, "grados celsius son :", Fahrenheit , " grados Fahrenheit " //cartel que concatena con variables
FinAlgoritmo
