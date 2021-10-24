
from random import *

fila1 = ["","",""]
fila2 = ["","",""]
fila3 = ["","",""]

tablero = [fila1,fila2,fila3]

jugador = "X"

jugar = True

Mensaje = "Se a llenado el tablero, Gracias por Jugar"

"""
-----------
juego
-----------
"""

def MostrarTablero():
    for x in tablero:
        print(x)

def LimpiarTablero():
    for x in tablero:
        for y in range(len(x)):
            x[y] = ""


def TurnoDeJuego(jugar):

    contador = 0
    Correcto = False
    
    try:
        while Correcto==False:

            posicionX = randint(0,2)
            posicionY = randint(0,2)
            
            if(tablero[posicionX][posicionY]==""):
                tablero[posicionX][posicionY]= jugar
                Correcto=True
                contador +=1
            else:
                #print("ya está ocupada por",tablero[posicionX][posicionY])
                if(contador==9):
                    contador = 0
                    break
    
    except(Exception):
    
        print("Algo salio mal")


def Ganar(ficha):
    z = 0

    while z == 0:
        for x in range(3):
            if ficha==tablero[x][0] and ficha==tablero[x][1] and ficha==tablero[x][2]:
                return True
            else:
                z = 1
    while z == 1:
        for x in range(3):
            if ficha==tablero[0][x] and ficha==tablero[1][x] and ficha==tablero[2][x]:
                return True
            else:
                z = 2
    while z == 2:
        contador = 0
        for x in range(3):
            if(tablero[x][x]==ficha):
                contador+=1
                if(contador==3):
                    return True
            else:
                z = 3
    while z==3:
        if(tablero[2][0]==ficha and tablero[1][1]==ficha and tablero[0][2]==ficha):
            return True
        else:
            break

while jugar:

    ComprobarJugador= input("Deseas Jugar S/N (Solo Mayuscula) :")

    while(ComprobarJugador == "S"):
        MostrarTablero()        

        if(Ganar(jugador)!=True):

            if(Ganar("X")==True):
                print("Gano X")
                LimpiarTablero()
                break

            elif(Ganar("O")==True):
                print("Gano O")
                LimpiarTablero()
                break

            elif(jugador == "X"):        
                print("Jugador X")
                TurnoDeJuego(jugador)
                jugador="O"
            
            elif(jugador =="O"):
                print("Jugador O")
                TurnoDeJuego(jugador)
                jugador="X"

            

        else:
            LimpiarTablero()
            break

    if(ComprobarJugador == "N"):    
        jugar = False



####################

