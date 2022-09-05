#Bucles For
#Ejercicio 1: 
#Escribir un ciclo definido para imprimir por pantalla todos los numeros entre 10 y 20.
for ciclo in range (10,21):
    print(ciclo)

#Ejercicio 2:
#Escribir un programa que imprima por pantalla todas las fichas de domino, de una por linea y sin repetir.
def domino():
	for j in range (0,7):
		for i in range (j,7):
			print(j,i)

#Ejercicio 3:
#Modificar el programa anterior para que pueda generar fichas de un juego que puede tener numeros de 0 a n.
def fichas(n):
    for fichas in range(0, n+1):
        print(fichas)

#Ejercicio 4:
#Escribir una función que tome una cantidad m de valores que son ingresados por el usuario y, en la medida que lo ingresa, se muestra el factorial de ese número. 
# El valor de m es ingresado inicialmente por el usuario
def numFactorial():
    m=int(input("Ingrese un numero: "))
    factorial=1
    for numero in range(1, m+1):
        factorial=factorial*numero
    print(factorial)
    numFactorial()

#Ejercicio 5:
#Usando la función, dada como ejemplo en la presentación de La Receta en Python, para convertir una temperatura en Fahrenheit a Celsius se pide que genere una tabla de
#conversión de temperaturas, desde 0 ◦F hasta 120◦F, de 10 en 10.
def farCel(f):
  return (f-32)*5/9

def tablaTemp():
	print("Temp F - Temp C")
	for n in range(0,121, 10):
		print(n, "-", farCel(n))

# Ejercicio 7:
def num_triang(n):
	if n == 0:
		return 0 #caso base
	else:
		return n + num_triang(n - 1)
# Sin ecuacion
def sumaPrimeros(n):
	for n in range(0, n+1):
		print(n , "-", num_triang(n))
# Con ecuacion 
def ecu(n):
	return (n * (n+1)) / 2

def sumaPrimeros1(n):
	for n in range(0, n+1):
		print(n, "-", ecu(n))
#-----------------------------------------------------------------------------
#Bucles While
#Ejercicio 8:
#Nos piden que escribamos una función que le pida al usuario que ingrese un número positivo. Si el usuario ingresa cualquier cosa que no sea lo pedido se le debe informar
#de su error mediante un mensaje y volverle a pedir el número
def positivo():
    x = int(input("Por favor ingrese un numero positivo >> "))
    while (x <= 0):
        if (x < 0):
            print("Ingreso un numero negativo...")
        if (x == 0):
            print("Ingreso cero...")
        x = int(input("Por favor ingrese un numero positivo >> "))
    print(x)
#Ejercicio 9:
#Escriba un programa que permita al usuario ingresar un conjunto de notas, preguntando a cada paso si desea ingresar más notas, 
#e imprimiendo el promedio correspondiente, al finalizar la toma de datos
def ingresar_notas():
    x = int(input("Ingrese una nota o -1 para salir \n >> "))
    if (x == -1):
        print("No se ingresaron notas")
    else:
        suma = 0
        contador = 0
        while (x != -1):
            suma += x
            contador += 1
            x = int(input("Ingrese una nota o -1 para salir \n >> "))
        print("El promedio de notas es: ", suma / contador)

#Ejercicio 10:
#Escriba un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número mientras no sea mayor que el primero. 
#El programa terminará escribiendo los dos números
def numeros():
    x1 = int(input("Ingrese el primer numero: "))
    x2 = int(input("Ingrese el segundo numero: "))
    while (x1 < x2):
        print("El segundo numero es mayor que el primero")
        x2 = int(input("Ingrese el segundo numero: "))
    print("Los numeros ingresados fueron correctos,", x1, x2)

#Ejercicio 11:
#Escriba una función que reciba dos números como parámetros, y devuelva cuántos múltiplos del primero hay, que sean menores que el segundo.
# a) Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
# b) Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea mayor que el segundo.
# c) Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?
def conFor(n1, n2):
    contador=0
    for x in range (n1,n2+1,1):
        if x % n1 == 0:
            contador = contador + 1
    print(contador)        

def multiplos(n1, n2):
    print(len(range(n1, n2, n1)))

#def conWhile():
    primer = int(input("Primer Numero: "))
    segundo = int(input("Segundo Numero: "))
    l = []
    i = primer
    while i <= segundo:
            if i % primer == 0:
                l.append(i)
                i = i + 1
            else:
                i = i + 1
    return(l)
#print(conWhile())

#Ejercicio 12: Manejo de contraseñas
# a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
# b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
# c) Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).
def contraseña():
    contraseña = "Programacion2"
    msj = input("Ingrese la contraseña: ")
    while (contraseña != msj):
        print("Contraseña Incorrecta")
        msj = input("Ingrese la contraseña: ")
    print("Contraseña Correcta")

def contraseña_Intentos():
    contraseña = "Programacion2"
    msj = input("Ingrese la contraseña: ")
    intento = 0
    while (contraseña != msj and intento < 2):
        print("Contraseña Incorrecta")
        intento += 1
        msj = input("Ingrese la contraseña: ")

#def contraseñaBoolean():
    Programacion2 = False
    msj = input("Ingrese la contraseña: ")
    intento = 0
    while (not Programacion2 and not intento == 2):
        print("Contraseña Incorrecta")
        intento += 1
        if msj == "Programacion2":
            Programacion2 = True
        else:
            print(msj)

#Ejercicio 13:
#Escriba una función que reciba un número natural e imprima todos los números primos que hay hasta ese número. Para esto se pide que:
# a) Defina una función es_primo que toma un número natural y verifique si es un número primo.
# b) Resuelva el problema usando la función definida en el punto anterior.
def es_primo(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def primos(n):
    for i in range(2, n+1):
        if es_primo(i):
            print(i)

#Ejercicio 14: Potencia de dos
# a) Escribir una función es_potencia_de_dos que reciba como parámetro un número natural, y devuelva True si el número es una potencia de 2, y False en caso contrario.
# b) Escribir una función que, dados dos números naturales pasados como parámetros, devuelva la suma de todas las potencias de 2 que hay en el rango formado por esos números
# (0 si no hay ninguna potencia de 2 entre los dos). Utilizar la función es_potencia_de_dos, descripta en el punto anterior.
def es_potencia_de_dos(n):
    return (n & (n - 1) == 0) and n != 0 