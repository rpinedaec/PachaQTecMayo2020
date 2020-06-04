Proceso ejercicio_5
	Escribir "Introduce el primer numero"
	Leer numero1
	Escribir "Introduce el segundo numero"
	Leer numero2
	Escribir "Introduce el tercer numero"
	Leer numero3
	//si el numero1 es menor que 0,
	//multiplicara los numero y sino los sumara
	Si (numero1<0) Entonces
		resultado<-numero1*numero2*numero3
	Sino
		resultado<-numero1+numero2+numero3
	FinSi
	Escribir resultado
FinProceso