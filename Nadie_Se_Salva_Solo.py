import time
import os
os.system('cls')

def menu():
    print("\033[1;38;5;165m----------------***-----------------\033[0m")
    print("\033[1;38;5;10m  NADIE SE SALVA SOLO - COMIQUERÍA  \033[0m")
    print("\033[1;38;5;165m----------------***-----------------\033[0m")
    print(" ")
    print("\033[1;38;5;213m 1- Gestion de Productos\033[0m")
    print("\033[1;38;5;53m 2- Pedidos\033[0m")
    print("\033[1;38;5;99m 3- Catalogo\033[0m")
    print("\033[1;38;5;31m 4- Ultima visualizacion\033[0m")
    print("\033[1;38;5;33m 5- Salir\033[0m")
    print("")
    eleccion= int(input(f"Ingrese la opcion que desea: "))

    return eleccion

seleccion = menu()

while seleccion != 6:
    if seleccion == 1:
        print(1)
    elif seleccion == 2:
        print(2)
    elif seleccion == 3:
        print(3)
    elif seleccion == 4:
        print(4)
    elif seleccion >= 5:
        break
    time.sleep(3.5)
    os.system('cls')
    seleccion = menu()