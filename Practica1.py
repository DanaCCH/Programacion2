#Ejercicio 1:
#Escriba un programa que imprima los primeros 25 numeros pares
from __future__ import division


def pares(n):
    if n % 2 == 0 and n <= 50:
        print("El numero",n," es par")
        pares(n + 1)
    elif n < 50:
        pares(n + 1)
#Ejercicio 2:
#Escriba un programa que imprima los primeros 100 naturales pares
def primerosCien(n):
    if n % 2 == 0 and n <=200:
        print(n)
        primerosCien(n + 1)
    elif n < 200:
        primerosCien(n + 1)
#Ejercicio 3:
#Escriba un programa que imprima los primeros n numeros pares mayores que m
def primerosN(n, m):
    if n == 0:
        return #caso base
    elif m % 2 == 0:
        print(m)
        primerosN(n-1, m+1)
    else:
        primerosN(n, m+1)
#Ejercicio 4:
#Escriba un programa que calcule e imprima el resulado de la suma de los primeros 50 numeros naturales usando una funcion recursiva
def suma50(n):
    if n == 0:
        return 0 #caso base
    elif n <= 50:
        return  n + suma50(n - 1)
#Ejercicio 5:
#Escriba un programa que calcule e imprima el resultado de la suma de los primeros n numeros naturales usando funcion recursiva
def sumaPrimeros(n):
    if n == 0:
        return 0 #caso base
    else:
        return n + sumaPrimeros(n - 1)
#Ejercicio 6:
#Escriba un programa que calcule e imprima el resultado de la suma de los numeros naturales mayores que n y menores que m con recursion
def sumaN(n, m):
    if (n + 1) == m:
        return 0 #caso base, pues m es el tope
    elif (n + 1) < m:
        return (n + 1) + sumaN(n + 1, m)
#--------------------------CADENAS--------------------------------------
#Ejercicio 7:
#Escriba un programa que reciba un nombre y retorne el nombre pasado concatenando 2 veces. Es decir, supongamos que la funcion se duplica
#si hacemos duplica("federico") el resultado seria: "federicofederico"
def duplicoNombre():
   n= input("Ingrese su nombre: ")
   return n*2
#Ejercicio 8:
#Escriba un programa que reciba un nombre y un numero n, y retorne el nombre pasado concatenado n veces. Es decir, supongamos que la funcion
#se duplica, si hacemos duplica("federico", 3) el resultado seria: "federicofedericofederico"
def variasVeces(n, m):
    return n*m
#-------------------PROGRAMAS INTERACTIVOS----------------------------
#Ejercicio 9:
# a) Escriba una funcion suma que reciba dos numeros y retorne el resultado de la suma de ambos.
def suma(a, b):
    return a + b
# b) Escriba una funcion resta que reciba dos numeros y retorne el resulado de la resta de ambos.
def resta(a, b):
    return a - b
# c) Escriba una funcion multiplica que reciba dos numeros y retorne el resultado de la multiplicacion de ambos.
def multiplica(a, b):
    return a*b
# d) Escriba una funcion que divide que reciba dos numeros y retorne el resultado de la division de ambos numeros.
def devide(a, b):
    return a/b
# e) Escriba un programa que muestre un mensaje pidiendo que elija una opcion de las mismas, luego debe pedirse el ingreso de dos numeros y mostrar el resultado
def operacion():
    mensaje= int(input("\t 1. Suma \n \t 2. Resta \n \t 3. Multiplica \n \t 4. Divide \n \t 5. Salir \n Ingrese una opcion: "))
    if mensaje==5:
        return
    a=int(input("Ingrese el primer numero: "))
    b=int(input("Ingrese el segundo numero: "))
    if mensaje==1:
        print("La suma entre ", a, "y ", b, "es: ", suma(a, b))
    elif mensaje==2:
        print("La resta entre ", a,"y ", b, "es: ", resta(a,b))
    elif mensaje==3:
        print("La multiplicacion entre ", a,"y ", b, "es: ", multiplica(a, b))
    elif mensaje==4:
        print("La division entre ",a, "y ", b, "es: ", division(a,b))
    operacion()



    