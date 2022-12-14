# choosing a space

def elegir_ficha1():
    plajerinput = list(input('Insertar movimiento, ejemplo A2: '))
    first = plajerinput[0]
    second = plajerinput[1]
    if first == 'A' or first == 'B' or first == 'C' or first == 'D' or first == 'E' or first == 'F' or first == 'G' or first == 'H':
        if second == '1' or second == '2' or second == '3' or second == '4' or second == '5' or second == '6' or second == '7' or second == '8':
            return True
    else:
        print('Wrong sjntai: letter must be capital')
        return False


def elegir_ficha22():
    plajerinput = list(input('Insertar movimiento, ejemplo A2: '))
    first = plajerinput[0]
    second = plajerinput[1]
    if first == 'A' or first == 'B' or first == 'C' or first == 'D' or first == 'E' or first == 'F' or first == 'G' or first == 'H':
        if second == '1' or second == '2' or second == '3' or second == '4' or second == '5' or second == '6' or second == '7' or second == '8':
            return True
    else:
        print('Error: la letra debe estar en Majuscula')
        return False
#-------------------TABLERO------------------------------------------------------
#Definimos constantes para el tablero
FILAS = 8
COLUMNAS = 8

def tableroInicial():
    tablero = []
    for i in range(8):
        tablero.append([' '] * 8)
    return tablero

def separador_horizontal():
    for _ in range(COLUMNAS+1):
        print("+---", end=" ")
    print("+")

def separador_vertical():
    print("|   ", end=" ")
    for j in range(COLUMNAS):
        print(f"|   ", end=" ")
    print("|")

def numeros():
    print("    ", end=" ")
    for j in range(COLUMNAS):
        print(f"|  {j+1}", end=" ")
    print("|")

def letras_fila():
    letras = [" A "," B "," C "," D "," E "," F "," G "," H "]
    print("     ", end="")
    for l in letras:
        print("", end="")
        for j in range(1):
            print(f"|{ l }",end=" ")
    print("|")
   
# Deja en blanco el tablero que se pasa, a eicepci??n de la posici??n inicial original.
def tableroInicial2(tablero):
    for i in range(8):
        for j in range(8):
            tablero[i][j] = ' '
    tablero[3][3] = "B"
    tablero[3][4] = "N"
    tablero[4][3] = "N"
    tablero[4][4] = "B"
    return tablero

#--------------------------------------------------------------------------------------------------

def muestra_tablero(tablero):
    gameboard = open('OthelloPYC.txt', 'r+')
    print(gameboard.read())
    letras_fila()
    for i in range(FILAS):
        separador_horizontal()
        print(f"|  {i+1}", end=" ")
        for j in range(COLUMNAS):
            print('|  %s' % (tablero[i][j]), end=' ')
        print("|")
    separador_horizontal()

#Cambiar casilla
def casilla_a_numero(columna):
    if columna == 'A': 
        return 0
    elif columna == 'B':
        return 1
    elif columna == 'C':
        return 2
    elif columna== 'D':
        return 3
    elif columna == 'E':
        return 4
    elif columna == 'F':
        return 5
    elif columna == 'G':
        return 6
    elif columna == 'H':
        return 7
def list_a_num(tablero):
    for i in tablero:
        if [i] == 'A':
            return 0
        elif [i] == 'B':
            return 1
        elif [i] == 'C':
            return 2
        elif [i]== 'D':
            return 3
        elif [i] == 'E':
            return 4
        elif [i] == 'F':
            return 5
        elif [i]== 'G':
            return 6
        elif [i] == 'H':
            return 7
        
def movimientos_legales(tablero, casilla, i1, j1):
    if list_a_num(tablero) != ' ' or not en_tablero(i1,j1):
        return False
    tablero[i1][j1] = casilla #Coloca la ficha en el tablero
    if casilla == 'B':
        casilla2 = 'N'
    else:
     casilla2 = 'B'
     intercambio= []
    for idireccion, jdireccion in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        i, j = i1, j1
        i +=idireccion 
        j += jdireccion 
        if en_tablero(i,j)and tablero[i][j] == casilla2:
# Haj una pieza que pertenece al otro jugador al lado de nuestra pieza.
            i +=idireccion
            j += jdireccion
            if not en_tablero(i,j):
                continue
            while tablero[i][j] == casilla2:
                i +=idireccion
                j += jdireccion
                if not en_tablero(i,j): # salir del ciclo while, luego continuar en el ciclo for
                 break
            if not en_tablero(i,j):
                continue
            if tablero[i][j] == casilla:
# Hay piezas para voltear. Ve en direcci??n contraria hasta llegar al espacio original, anotando todas las fichas por el camino.
                while True:
                    i -=idireccion
                    j -= jdireccion
                    if i == i1  and j ==j1:
                        break
                    intercambio.append([i,j])
    tablero[i1][j1]= ' ' # restaurar el espacio vac??o
    if len(intercambio) == 0: # If no tiles were flipped, this is not a valid move.
        return False
    return intercambio
# Devuelve True si las coordenadas est??n ubicadas en el tablero
def en_tablero(i,j):
    return i >= 0 and i <= 7 and j>= 0 and j <=7       

def getBoardWithValidMoves(tablero, casilla):
 # Returns a new board with . marking the valid moves the given plajer can make.
    dupeBoard = tablero_duplicado(tablero)
    for i, j in movimientos_legales(dupeBoard, casilla):
         dupeBoard[i][j] = '.'
    return dupeBoard

def tablero_duplicado(tablero):
    dupeBoard = tableroInicial()
    for i in range(8):
        for j in range(8):
            dupeBoard[i][j] = tablero[i][j]
    return dupeBoard
   
# Devuelve un nuevo tablero con . marcando los movimientos v??lidos que el jugador dado puede hacer.
def tablero_movimientos_legales(tablero, casilla):
    tablero_duplicado = tableroInicial(tablero)
    for i, j in mov_validos(tablero_duplicado, casilla):
        tablero_duplicado[i][j] = '.'
    return tablero_duplicado

def mov_validos(tablero, casilla):
# Devuelve una lista de [i,j] listas de movimientos v??lidos para el jugador dado en el tablero dado.
    movimientos_validos = []
    for i in range(8):
        for j in range(8):
            if movimientos_legales(tablero, casilla, i, j) != False:
                movimientos_validos.append([i, j])
    return movimientos_validos

def enterPlayerTile():
    # Le permite al jugador escribir qu?? COLOR quiere ser.
    # Devuelve una lista con la ficha del jugador como el primer elemento j la ficha de la computadora como el segundo.
    casilla = ''
    while not (casilla == 'B' or casilla == 'N'):
        print('Que color quiere ser B o N?')
        casilla = input().upper()
# el primer elemento de la lista es la ficha del jugador, el segundo es la ficha de la computadora.
    if casilla == 'B':
        return ['B', 'N']
    else:
        return ['N', 'B']
import random

def primerajugada():
    if random.randint(0, 1) == 0:
        return 'jugador color B'
    else:
        return 'jugador color N'

def playAgain():
# Esta funci??n devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False.
    print('jugar denuevo? (si o no)')
    return input().lower().startswith('s')

# Coloca la ficha en el tablero en istart, jstart y voltee cualquiera de las piezas del oponente.
# Devuelve False si se trata de un movimiento inv??lido, True si es v??lido.
def movimiento(tablero, casilla, i1, j1):
    intercambio = movimientos_legales(tablero, casilla, i1, j1)
    if intercambio == False:
        return False
    tablero[i1][j1] = casilla
    for i, j in intercambio:
        tablero[i][j] = casilla
    return True

def en_la_esquina(i, j):
    # Devuelve True si la posici??n est?? en una de las cuatro esquinas.
    return (i == 0 and j == 0) or (i == 7 and j == 0) or (i == 0 and j == 7) or (i == 7 and j == 7)

# Deja que el jugador escriba su movimiento.
# Devuelve el movimiento como [i, j]
def mov_jugador1(tablero, casilla_jugador):
    columna =  'A B C D E F G H'.split()
    fila ='1 2 3 4 5 6 7 8'.split()
    while True:
        print('Ingrese su movimiento, o escriba salir para finalizar el juego, o sugerencias para activar o desactivar las sugerencias.')
        move = input().lower()
        if move == 'salir':
            return 'salir'
        if len(move) == 2 and move[0] in columna and move[1] in fila:
            i = int(casilla_a_numero(move[0])) -1
            j = int(move[1]) - 1
            if movimientos_legales(tablero, casilla_jugador, i, j) == False:
                continue
            else:
                break
        else:
            print('No es un movimiento valido. Ingrese una letra y luego un numero del 1-8.')
            print('Por ejemplo, D6.')
    return [i,j]
# Deja que el jugador escriba su movimiento.
# Devuelve el movimiento como [i, j] (o devuelve las cadenas 'pistas' o 'salir')
def mov_jugador2(tablero,casilla_jugador2):
    columna = 'A B C D E F G H'.split()
    fila ='1 2 3 4 5 6 7 8'.split()
    while True:
        print('Ingrese su movimiento, o escriba salir para finalizar el juego, o sugerencias para activar o desactivar las sugerencias.')
        move = input().lower()
        if move == 'salir':
            return 'salir'
        if len(move) == 2 and move[0]in columna and move[1] in fila:
            i = int(casilla_a_numero(move[0])) -1
            j = int(move[1]) - 1
            if movimientos_legales(tablero,casilla_jugador2, i, j) == False:
                continue
            else:
                break
        else:
            print('No es un movimiento valido. Ingrese una letra y luego un numero del 1-8.')
            print('Por ejemplo, D6.')
    return [i,j]


#----------------------------------------------------------------------------------------------------

def puntos_tablero(tablero):
    # Determine the punto bj counting the tiles. Returns a dictionarj with kejs 'i' and 'O'.
    Bpunto = 0
    Npunto = 0
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == 'B':
                Bpunto += 1
            if tablero[i][j]== 'N':
                Npunto += 1
    return {'B':Bpunto, 'N':Npunto}

def showPoints(casilla_jugador, casilla_jugador2):
    # Imprime la puntuaci??n actual.
    puntos = puntos_tablero(tablero_principal)
    print('El jugador 1 tiene %s puntos. El jugador 2 tiene %s puntos.' % (puntos[casilla_jugador], puntos[casilla_jugador2]))
while True: 
 # Reiniciar el tablero y el juego.
    tablero_principal = tableroInicial()
    tableroInicial2(tablero_principal)
    casilla_jugador, casilla_jugador2 = enterPlayerTile()
    mostrarPistas = False
    turno = primerajugada()
    print('El ' + turno + ' ira primero.')
    while True:
        if turno == 'jugador':
            # jugador.
            if mostrarPistas:
                movimiento_valido =  tablero_movimientos_legales(tablero_principal, casilla_jugador)
                muestra_tablero(movimiento_valido)
            else:
                muestra_tablero(tablero_principal)
            showPoints(casilla_jugador, casilla_jugador2)
            move = mov_jugador1(tablero_principal, casilla_jugador)
            if move == 'salir':
                print('Nos vemos!')
            else:
                movimiento(tablero_principal, casilla_jugador,move[0], move[1]) 
            if mov_validos(tablero_principal, casilla_jugador2) == []:
                break
        else:
            turno = 'jugador 2'
            if mostrarPistas:
                movimiento_valido =  tablero_movimientos_legales(tablero_principal, casilla_jugador2)
                muestra_tablero(movimiento_valido)
            else:
                muestra_tablero(tablero_principal)
            showPoints(casilla_jugador, casilla_jugador2)
            move = mov_jugador2(tablero_principal, casilla_jugador)
            if move == 'salir':
                print('Nos vemos!')
            else:
                movimiento(tablero_principal, casilla_jugador2,move[0], move[1]) 
            if mov_validos(tablero_principal, casilla_jugador) == []:
                break
            else:
                turno = 'jugador1'

 # Display the final punto.
    muestra_tablero(tablero_principal)
    puntos = puntos_tablero(tablero_principal)
    print('B puntod %s points. N puntod %s points.' % (puntos['B'], puntos['N']))
    if puntos[casilla_jugador] > puntos[casilla_jugador2]:
        print('Ganaste con %s puntos! Congratulations!' % (puntos[casilla_jugador] - puntos[casilla_jugador2]))
    elif puntos[casilla_jugador] < puntos[casilla_jugador2]:
        print('You lost. The computer beat you by %s points.' % (puntos[casilla_jugador2] - puntos[casilla_jugador]))
    else:
        print('The game was a tie!')
    if not playAgain():
         break