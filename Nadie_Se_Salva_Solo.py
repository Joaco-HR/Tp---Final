import os
os.system('cls')

print("\033[1;38;5;165m----------------***-----------------\033[0m")
print("\033[1;38;5;10m  NADIE SE SALVA SOLO - COMIQUERÍA  \033[0m")
print("\033[1;38;5;165m----------------***-----------------\033[0m")
print(" ")


def menu():
    print(f"\033[1m1- Gestion de Productos\033[0m")
    print(f"\033[1m2- Pedidos\033[0m")
    print(f"\033[1m3- Productos\033[0m")
    print(f"\033[1m4- Ultima visualizacion\033[0m")
    print(f"\033[1m5- Salir\033[0m")
    print("")
    eleccion= int(input(f"Ingrese la opcion que desea: "))

    return eleccion

seleccion = menu()
