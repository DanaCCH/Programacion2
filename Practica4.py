#Listas
#1) Escriba una función posicionesMultiplo que tome una lista y, un número, y retorne la lista formada por los elementos que están en las posiciones múltiplos de ese número.
#Por ejemplo: posicionesMultiplo([1,2,3,4,5,6,7],2) retorna [1, 3, 5, 7] y, posicionesMultiplo([1,2,3,4,5,6,7],3) da como resultado [1, 4, 7
def posicionesMultiplo(lista,n):
    return  lista[0:len(lista):n]

#2)Escriba una función que tome una lista de números y devuelva la suma acumulada, es decir, una nueva lista donde el primer elemento es el mismo, el segundo elemento es la
# suma del primero con el segundo, el tercer elemento es la suma del resultado anterior con el siguiente elemento y así sucesivamente. 
# Por ejemplo, la suma acumulada de [1, 2, 3] es [1, 3, 6].
def sumaListarari(lista):
    n = 0
    for i in range (0,len(lista)):
        n += lista[i]    
    return n

def sumaLista (lista):
    n = 0
    nuevaLista = []
    for i in range (0,len(lista)):
        n += lista[i]
        nuevaLista.append(n)
    return nuevaLista

#3) Escriba una función llamada elimina que tome una lista y elimine el primer y último elemento de 
# la lista y cree una nueva lista con los elementos que no fueron eliminados.
def elimina(lista):
    return lista[1:len(lista)-1]
def test_elimina():
    elimina([1, 2, 3, 4, 5]) == [2, 3, 4]

#4) Escriba una función ordenada que tome una lista como parámetro y devuelva True si la
# lista está ordenada en orden ascendente y devuelva False en caso contrario. Por ejemplo,
# ordenada([1, 2, 3]) retorna T rue y ordenada([’b’, ’a’]) retorna False
def lista_ordenada(lista):
    for i in range(1,len(lista)):
        if lista[i]< lista[i-1]:
            return False
    return True
def test_lista_ordenada():
    lista_ordenada([0,1,2,3]) == True
    lista_ordenada([0,1,2,20,3]) == False
    
#5) Escriba una función llamada duplicado que tome una lista y devuelva True si tiene algún elemento duplicado. 
# La función no debe modificar la lista
def duplicado(lista):
    estado = False
    n_iguales = []
    for i in lista:
        if i in n_iguales:
            return False
    return True

#def test_duplicado(lista):
    duplicado([0,0,1,2,3]) == True
    duplicado([0,1,2,3]) == False

#6) Escriba una función llamada eliminaDuplicados que tome una lista y devuelva una
#nueva lista con los elementos únicos de la lista original. No tienen porque estar en el
#mismo orden
def eliminaDuplicados(lista):
    unicos = []
    for i in lista:
        if i not in unicos:
            unicos.append(i)
    return unicos

def test_eliminaDuolicados():
    eliminaDuplicados([1,2,2,3,4]) == [1,2,3,4]

#7) Escriba una función que tome una lista y retorne la cantidad de elementos distintos que
# tiene. Se recomienda usar la función anterior.
def cantidad(lista):
    for i in eliminaDuplicados(lista):
      return len(eliminaDuplicados(lista))

#8) Se pide que implemente la función busquedaDicotomica que toma una lista de palabras 
# ordenadas alfabeticamente y, una palabra a buscar y, retorna si la palabra está en 
# la lista o no.
def busquedaDicotomica(lista, string):
    n= int(len(lista)/2)
    if string in lista[0:n]:
        return True
    elif string in lista[n:len(lista)]:
        return True
    else:
        return False

def test_busquedaDicotomica():
    busquedaDicotomica(["hola","isla","jamaica","kiwi","raton","sapo","tito"],"jamaica") == True
    busquedaDicotomica(["alas","batidor","color","dana"],"elefante") == False

###CADENAS--------------------------------------
#1) Escriba un programa que tenga una función que tome una cadena y muestre cada caracter
# que la forma del último al inicial.
def cadena(string):
    for i in string:
        print(i)
#2)Escriba un programa que contenga a la función contar(l, x) que cuente cuántas veces 
# aparece un carácter l dado en una cadena x.
def contar(l,x):
    contador = 0
    for l2 in x:
        if l2 == l:
            contador += 1
    print(contador)
#3)Escriba un programa que cuente cúantas veces aparecen cada una de las vocales en
# una cadena. No importa si la vocal aparece en mayúscula o en minúscula.
def cant_vocales(string):
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    contador = 0
    for i in string:
        for v in vocales:
            if i == v:
                contador += 1
    print(contador)
#4)Escriba un programa que contenga la función que reciba como parámetro una cadena de
# palabras separadas por espacios y devuelva, como resultado, cuántas palabras de más
# de cinco letras tiene la cadena dada.
def cadena_de_cinco(string):
    contador = 0
    contador5 = 0
    for i in string:
        if contador == 5:
            contador5 += 1
            if i != " ":
                contador = contador + 1
            elif i == " ":
                contador = 0
        elif i != " ":
            contador = contador + 1
        elif i == " ":
            contador = 0
    return contador5

