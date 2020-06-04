Proceso ejercicio_6
	Escribir "Introduce un numero"
	Leer numero
	//si el numero es mayor que 0, calcula la potencia y la raiz
	//sino muestra un mensaje de error y sale del programa
	Si (numero>0) Entonces
		potencia<-numero^2
		raiz_cuadrada<-RAIZ(numero)
		Escribir "Su potencia es " potencia
		Escribir "Su raiz es " raiz_cuadrada
	Sino
		Escribir "Error, introduce un numero mayor que 0"
	FinSi
FinProceso