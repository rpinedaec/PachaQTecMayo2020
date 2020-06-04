Proceso ejercicio_10
	Escribir "Introduce un numero"
	Leer numero
	//Hasta que no se introduzca un numero mayor que 0 no saldra del bucle
	Mientras (numero<=0) hacer
		Escribir "escribe un numero mayor que 0"
		Leer numero
	FinMientras
	Si (numero MOD 2=0) Entonces
		Escribir "El " numero " es par"
	Sino
		Escribir "El " numero " no es par"
	FinSi
FinProceso