Proceso ejercicio_3
    Escribir "Introduce el primer numero"
    Leer numero1
    Escribir "Introduce el segundo numero"
    Leer numero2
    //comparamos los dos numeros,
    //si el primero es mayor o igual que el segundo entra
    Si (numero1>=numero2) Entonces
		//Si el numero1 y numero2 son iguales entra y escribe que son iguales
		//Sino lo son escribe que el numero1 es el mayor
        Si (numero1=numero2) Entonces
            escribir "los numeros " numero1 " " numero2 " son iguales"
        Sino
            Escribir numero1 " es el mayor de los dos"
        FinSi
		//Si el primer Si es falso, escribe que el numero2 es mayor
	Sino
        Escribir numero2 " es el mayor de los dos"
	FinSi
FinProceso