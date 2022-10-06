#Listas y secuencias
# 1) Escribir una función que reciba una lista desordenada y un elemento, que:
# a) devuelva la cantidad de apariciones del elemento recibido como parámetro, en la lista;
from re import M


def lista(lista,n):
    contador = 0
    for i in lista:
        if i == n:
            contador += 1
    print(contador)
# b) busque la primera coincidencia del elemento en la lista y devuelva su posición;
def listaPosicion (lista,n):
    posicion= -1
    cantidad = 0
    for x in lista :
        posicion += 1
        if x == n and cantidad == 0:
            cantidad += 1
        elif x == n:
            cantidad += 1      
    return cantidad, posicion 
# c) utilizando la función anterior, busque todos los elementos que coincidan con el recibido como parámetro y devuelva una lista con las posiciones.
def listaPosiciones (lista,n):
    listaPosn = []
    posicion= -1
    cantidad = 0
    for x in lista :
        posicion +=1
        if x == n:
            cantidad += 1   
            listaPosn.append(posicion)
    return listaPosn

#2) Escribir una función que tome una lista de números desordenada, que:
# a) devuelva el valor máximo;
# b) devuelva una tupla que incluya el valor máximo y su posición;
# c) ¿qué sucede si los elementos son listas de caracteres?

def listaNum(lista):
    nuevaLista = []
    max = nuevaLista[0]
    for i in nuevaLista[i]:
        if i> max:
            max = 0

#3) Escribir una función que tome una lista ordenada y un elemento. Si el elemento se encuentra en la lista, 
# debe encontrar su posición mediante búsqueda binaria y devolverlo. Si no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición.
def busqueda(lista,elemento):
    posicion = 1
    n= int(len(lista)/2)
    for elemento in lista:
        if elemento in lista[0:n]:
            posicion += 1
            return posicion
        elif elemento in lista[n:len(lista)]:
            posicion += 1
            return posicion

#Diccionarios
#1) Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las claves sean los 
# primeros elementos de las tuplas, y los valores una lista con los segundo. 

def tuplas_a_diccionario(lista):
    creaDic = {}
    for x,y in lista:
        creaDic.setdefault(x,[]).append(y)
    print (creaDic)
l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]
print(tuplas_a_diccionario(l))

#2) Diccionarios usados para contar:
# a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
# de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo dia que hace hoy" 
pruebaDic = { "que": 2, "lindo": 1, "día": 1, "hace": 1, "hoy": 1}

def contador(cadena):
    creaContador = {}
    palabra = ""
    for cadena in cadena:
        if cadena == cadena:
            print(str (cadena))
      