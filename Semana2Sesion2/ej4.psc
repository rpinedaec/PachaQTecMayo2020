Proceso ejercicio_4
    Escribir "Introduce el primer numero"
    Leer numero1
    Escribir "Introduce el segundo numero"
    Leer numero2
    Escribir "Introduce el tercer numero"
    Leer numero3
    //comparamos el numero1 con el numero2 y numero3
    //Si las dos condiciones son verdaderas el numero1 es el mayor
    Si (numero1>numero2 Y numero1>numero3) Entonces
		Escribir "el numero " numero1 " es el mayor"
		//si el numero1 no es el mayor,
		//comparamos el numero2 con el numero3
    Sino
		Si (numero2>numero3) Entonces
			Escribir "El numero " numero2 " es el mayor"
		Sino
			Escribir "El numero " numero3 " es el mayor"
		FinSi
    FinSi
FinProceso