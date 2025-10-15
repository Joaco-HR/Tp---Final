import os
os.system('cls')
import time

class bcolors:
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'

    ENDC = '\033[0m' # finalizar
    BOLD = '\033[1m' # negrita
    UNDERLINE = '\033[4m' # subrayado

def DelayedPrint(*values, delayChar = 0.05, delayLine = 0.3):
    for character in ''.join(values):
        print(character, end='')   # Imprimir caracter por caracter, sin realizar el salto de linea al final.
        time.sleep(delayChar)   # Realizar una pausa de delayChar segundos.

    time.sleep(delayLine)   # Al finalizar de imprimir el texto, realizar una pausa de delayLine segundos
    print()   # Imprimir un salto de linea

def menu():
    print(f"{bcolors.Red}1) Jugar{bcolors.ENDC}")

    print(f"{bcolors.Yellow}{bcolors.BOLD}2) Tutorial{bcolors.ENDC}")

    print(f"{bcolors.Green}{bcolors.BOLD}3) Creditos{bcolors.ENDC}")

    print(f"{bcolors.Blue}{bcolors.BOLD}4) Salir{bcolors.ENDC}")

    eleccion= int(input(f"{bcolors.Black}{bcolors.BOLD}{bcolors.UNDERLINE}Ingrese la opcion que desea: {bcolors.ENDC}"))

    return eleccion

seleccion = menu()

def menu_juego():
    print(f"{bcolors.Green}{bcolors.BOLD}1) Nivel 1{bcolors.ENDC}")
    print(f"{bcolors.Yellow}{bcolors.BOLD}2) Nivel 2{bcolors.ENDC}")
    print(f"{bcolors.Red}{bcolors.BOLD}3) Nivel 3{bcolors.ENDC}")
    eleccion_juego= int(input("Ingrese la opcion que desea: "))

    return eleccion_juego

numeroMaximo= 0

vida = 3

corazones =   ["❤️", "  ❤️", "  ❤️",]
corazones_1 = ["❤️", "  ❤️", "  🤍",]
corazones_2 = ["❤️", "  🤍", "🤍",]
corazones_3 = ["🤍", "🤍", "🤍",]

lineas= ""
matriz_resultado = []
matriz_nivel =[]
def DefinirVariablesGlobales(opcion):
    global numeroMaximo
    global lineas
    global matriz_nivel
    global matriz_resultado
    if opcion == 1:
        numeroMaximo=4
        lineas = "-----------------"
        matriz_nivel= [
    [" ", " ", 4, 3],
    [4, " ", 2, " "],
    [3, 4, " ", " "],
    [" ", 2, " ", 4],]
        matriz_resultado= [
    [2, 1, 4, 3],
    [4, 3, 2, 1],
    [3, 4, 1, 2],
    [1, 2, 3, 4],]
        
    elif opcion == 2:
        numeroMaximo = 9
        lineas= "-------------------------------------"
        matriz_nivel=  [ 
    [5," ", 9, " ", 7, 6, 4, 1," "],
    [" ", 2, 8, 3, 1, " ", 9, 6, 5],
    [6," "," ", 2, 9, 5, 7, " ", 8],
    [4, 6, 2," "," ", 9, 8, 7, 1],
    [" ", 8, 5, 7, 2, 1," ", 4, " "],
    [1, 9," ", 4," ", 8, 2, 5, 3],
    [2, 5, 6, 1," ", 7, 3, 9, " "],
    [" ", 1, 3, 6, 4, 2, " ", 8, 7],
    [8, 7," ", 9, " ", 3, " ", 2, 6]]


        matriz_resultado= [ 
    [5, 3, 9, 8, 7, 6, 4, 1, 2],
    [7, 2, 8, 3, 1, 4, 9, 6, 5],
    [6, 4, 1, 2, 9, 5, 7, 3, 8],
    [4, 6, 2, 5, 3, 9, 8, 7, 1],
    [3, 8, 5, 7, 2, 1, 6, 4, 9],
    [1, 9, 7, 4, 6, 8, 2, 5, 3],
    [2, 5, 6, 1, 8, 7, 3, 9, 4],
    [9, 1, 3, 6, 4, 2, 5, 8, 7],
    [8, 7, 4, 9, 5, 3, 1, 2, 6]]

    elif opcion == 3:
        lineas= "-------------------------------------"
        numeroMaximo= 9
        matriz_nivel = [
            [5, 3, " ", " ", 7, " ", " ", " ", " "],
            [6, " ", " ", 1, 9, 5, " ", " ", " "],
            [" ", 9, 8, " ", " ", " ", " ", 6, " "],
            [8, " ", " ", " ", 6, " ", " ", " ", 3],
            [4, " ", " ", 8, " ", 3, " ", " ", 1],
            [7, " ", " ", " ", 2, " ", " ", " ", 6],
            [" ", 6, " ", " ", " ", " ", 2, 8, " "],
            [" ", " ", " ", 4, 1, 9, " ", " ", 5],
            [" ", " ", " ", " ", 8, " ", " ", 7, 9],
            ]
        matriz_resultado=  [
[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3 ,7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 7, 9],
]


def mostrarCorazones(corazones):
    print(f"{bcolors.Red}{bcolors.BOLD}Vidas: {bcolors.ENDC}",end = " ")
    for corazon in corazones:
        print(f" {corazon} ",end = " ")
    print(" ")





def mostrarSudoku(matriz_nivel_2):
    global lineas
    print(f"{bcolors.White}\t\t\t\t\t {lineas}{bcolors.ENDC}")
    for lista in matriz_nivel_2:
        print(f"{bcolors.White}\t\t\t\t\t |{bcolors.ENDC}",end = "")
        for elemento in lista:
            print(f"{bcolors.Cyan} {elemento}{bcolors.ENDC}" f"{bcolors.White} |{bcolors.ENDC}", end= "")
        print("")
        print(f"{bcolors.White}\t\t\t\t\t {lineas}{bcolors.ENDC}")



def chequeoIngreso(numero2):
    global vida
    global numeroMaximo
    while numero2 < 1 or numero2 >9:
        print(f"{bcolors.Yellow}{bcolors.BOLD}ERROR - Has perdido una vida{bcolors.ENDC}")
        vida -=1
        if not conteodevidas(vida):
            numero2 = int(input(f"{bcolors.Grey}{bcolors.BOLD}Ingrese un numero del 1 al {numeroMaximo}: {bcolors.ENDC}"))
        else: 
            break
    return numero2

def conteodevidas(vida):
    if vida == 2:
        mostrarCorazones(corazones_1)
    elif vida == 1:
        mostrarCorazones(corazones_2)
    else:
        mostrarCorazones(corazones_3)
        print(f"{bcolors.Red}{bcolors.BOLD}Perdiste {bcolors.ENDC}")
        return True
    return False



def ingresar_numero (matriz_nivel_2):
    global vida
    global numeroMaximo
    fila = int(input(f"{bcolors.Grey}{bcolors.BOLD}Ingrese en que fila desea ingresar (1-{numeroMaximo}): {bcolors.ENDC}"))
    fila =chequeoIngreso(fila)
    columna= int(input(f"{bcolors.Grey}{bcolors.BOLD}Ingrese en que columna desea ingresar(1-{numeroMaximo}): {bcolors.ENDC}"))
    columna = chequeoIngreso(columna)    
    numero = int(input(f"{bcolors.Grey}{bcolors.BOLD}Ingrese un numero del 1 al {numeroMaximo}: {bcolors.ENDC}"))
    numero = chequeoIngreso(numero)
    
    fila -=1
    columna -=1
    if chequearNumeroCorrecto(fila,columna,numero):
        matriz_nivel_2[fila][columna] = numero
    else:
        vida -=1
        conteodevidas(vida)
    return 

def chequearNumeroCorrecto(fila,columna,numero):
    global matriz_nivel
    global matriz_resultado
    global vida
    if numero == matriz_resultado[fila][columna]:
        print(f"{bcolors.Green}{bcolors.BOLD}CORRECTO{bcolors.ENDC}")
        
        return True

    else:   
        print(f"{bcolors.Red}{bcolors.BOLD}INCORRECTO{bcolors.ENDC}")
        return False

def juego1():
    global vida
    vida = 3
    estado="jugando"
    mostrarCorazones(corazones)
    while estado == "jugando":
        mostrarSudoku(matriz_nivel)
        ingresar_numero(matriz_nivel)
        if vida == 0:
            estado = "perdido"
            break
        if matriz_nivel == matriz_resultado:
            estado= "ganado"
            break
    if estado == "perdido":
        print(f"{bcolors.Magenta}{bcolors.BOLD}Lamento informarte que has perdido el Nivel 1{bcolors.ENDC}")
    else:
        print(f"{bcolors.Green}{bcolors.BOLD}Felicitaciones0 has ganado el Nivel 1!{bcolors.ENDC}")

def juego2():
    global vida
    vida = 3
    estado="jugando"
    mostrarCorazones(corazones)
    while estado == "jugando":
        mostrarSudoku(matriz_nivel)
        ingresar_numero(matriz_nivel)
        if vida == 0:
            estado = "perdido"
            break
        if matriz_nivel == matriz_resultado:
            estado= "ganado"
            break
    if estado == "perdido":
        print(f"{bcolors.Magenta}{bcolors.BOLD}Lamento informarte que has perdido el Nivel 2{bcolors.ENDC}")
    else:
        print(f"{bcolors.Green}{bcolors.BOLD}Felicitaciones has ganado el Nivel 2!{bcolors.ENDC}")

def juego3():
    global vida
    vida = 3
    estado="jugando"
    mostrarCorazones(corazones)
    while estado == "jugando":
        mostrarSudoku(matriz_nivel)
        ingresar_numero(matriz_nivel)
        if vida == 0:
            estado = "perdido"
            break
        if matriz_nivel == matriz_resultado:
            estado= "ganado"
            break
    if estado == "perdido":
        print(f"{bcolors.Magenta}{bcolors.BOLD}Lamento informarte que has perdido el Nivel 3{bcolors.ENDC}")
    else:
        print(f"{bcolors.Green}{bcolors.BOLD}Felicitaciones has ganado el Nivel 3!{bcolors.ENDC}")


while seleccion  != 4:
    if seleccion == 1:
        eleccionDeNivel= menu_juego()
        DefinirVariablesGlobales(eleccionDeNivel)
        if eleccionDeNivel == 1:
            juego1()
        elif eleccionDeNivel == 2:
            juego2()
        elif eleccionDeNivel == 3:
            juego3()
        
    elif seleccion == 2:
        DelayedPrint(f"{bcolors.Magenta}El sudoku es un juego matemático que consiste en rellenar un tablero de 9x9 o 4x4 casillas, dividido en 9 o en 4 bloques de 3x3 o 2x2 casillas, con los números del 1 al 9 del caso del 3x3 y de los números del 1 al 4 en el caso del 2x2, en este juego contarás con 3 vidas las cuales iras perdiendo en el caso de equivocarte de número y/o posición.{bcolors.Cyan}")
    elif seleccion == 3:
        DelayedPrint(f"{bcolors.Cyan}{bcolors.BOLD}Este juego fue desarollado por los alumnos Joaquin Rodriguez de 2do A y Facundo Benitez de 2do B{bcolors.ENDC}")
        DelayedPrint(f"{bcolors.Cyan}{bcolors.BOLD}Estos alumnos pertenecen al grupo de taller C{bcolors.ENDC}")
        DelayedPrint(f"{bcolors.Cyan}{bcolors.BOLD}Y en conjunto desarrollaron el juego llamado Sudoku{bcolors.ENDC}")
        DelayedPrint(f"{bcolors.Cyan}{bcolors.BOLD}Esperamos que les guste.{bcolors.ENDC}")
    else:
        #Error
        print("error")
    seleccion = menu()