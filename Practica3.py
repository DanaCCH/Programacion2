#1 Ciclos con While:
def ejercicio1 (n = 100):
    h = ''
    while n >= 20:
        h +=  ' ' + str(n) #str es string
        n -= 5
    return h
def test_ejercicio1():
    assert ejercicio1(100) == ' 100 95 90 85 80 75 70 65 60 55 50 45 40 35 30 25 20'

#2
def ejercicio2 (a, b, c):
    n = 2
    suma = 0
    sumas = 0
    if a/b > 30:
        suma = a/c*b**3
        return suma
    if a/b <= 30:
        while n <= 30:
            sumas += n**2
            n += 2
        return sumas

#3
def ejercicio3(n = 50):
    h = 0
    while n >= 20:
        h += n
        n -= 2
    return h
def test_ejercicio3():
    assert ejercicio3(50) == 560

#4
def ejercicio4(n = 1):
    p = 0
    i = 0
    while n <= 100:
        if n %2 == 0:
            p += n
        else:
            i += n
        n += 1
    return 'Pares= ' + str(p) + ' e Impares: ' + str(i)
#Ciclo For:
def ejercicio5(s):
    for x in s:
        print(x)
        #for z in x:
         #  print(z)
        print('***************')

from random import * #importa todas las funciones del módulo
a = random() #luego usamos directamente la función
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#1) Simule lanzamientos de un dado. Muestre el resultado en cada intento y, finalice cuando salga el número 7. También añada cuantas veces se lanzó el dado.
def dado (c=1, f=7):
    contador = 0 + 1
    intentos = randint(c, f)
    while intentos != f:
        contador += 1
        print(intentos)
        intentos = randint(c, f)
    print (f)
    print (contador, "haz hecho esa cantidad de intentos")

#2) Simule n lanzamientos de dos dados, donde n es un valor que se debe pedir que se ingrese por teclado. Muestre cuántas veces los dados tuvieron el mismo resultados.
def dados():
    n= int(input("Ingrese cuantos lanzamientos se debe hacer: "))
    dado1= randint(1,6)
    dado2= randint(1,6)
    contador = 0 
    lanzamientos = n
    while lanzamientos != 0:
        if dado1 == dado2:
            contador += 1
            lanzamientos -= 1
            dado1= randint(1,6)
            dado2= randint(1,6)
        else:
            lanzamientos -= 1
            dado1= randint(1,6)
            dado2= randint(1,6)
    print("Los dados tuvieron el mismo resultado:", contador)

#3) Simule n lanzamientos de un juego con un dado con las siguientes reglas: Si sale 6 gana 4 pesos; con un 3 gana 1 dólar; si sale 1 sigue jugando y, con 2,4 o 5 pierde 2 pesos.
#Muestre los valores que salen y, el resultado final del juego.
def juego(n):
    dado = randint(1,6)
    dineroTotal= 0
    lanzamientos = n
    while lanzamientos != 0:
        print(dado)
        if dado == 6:
            dineroTotal += 4
            lanzamientos -= 1
            dado = randint(1,6)
        elif dado == 3:
            dineroTotal += 1
            lanzamientos -= 1
            dado = randint(1,6)
        elif dado == 1:
            dado = randint(1,6)
            lanzamientos -= 1
        elif dado == 2 or dado == 4 or dado == 5:
            dineroTotal -= 2
            lanzamientos -= 1
            dado = randint(1,6)
    print("El dinero total acumulado es", dineroTotal)

    
def DadoApuesta (n):
    dado1 = randint(1, 6)
    pesos = 0
    dolar = 0
    count = n
    
    while count != 0:
        print (dado1)

        if dado1 == 6:
            pesos = pesos + 4
            count = count - 1
            dado1 = randint(1,6)
        
        elif dado1 == 3 :
            dolar = dolar + 1
            count = count - 1
            dado1 = randint(1,6)

        elif dado1 == 1:
            count = count - 1
            dado1 = randint(1,6)

        elif dado1 == 2 or dado1 == 4 or dado1 == 5 :
            pesos = pesos - 2
            count = count - 1
            dado1 = randint(1,6) 

    print ("Tienes ",dolar, "dolares y ",pesos, "pesos." )