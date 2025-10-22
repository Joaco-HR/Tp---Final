import os
os.system('cls')

catalago = [
    {
        "Producto": "Cómic",
        "Editorial": "DC",
        "Género": "Superhéroes",
        "Alineación": "Solitario",
        "Personaje/Equipo": "Batman",
        "Título": "Batman Return",
        "Precio": 32400,
        "Stock": True,
        "Código": "DC-B01"
    },
    {
        "Producto": "Cómic",
        "Editorial": "DC",
        "Género": "Superhéroes",
        "Alineación": "Solitario",
        "Personaje/Equipo": "Superman",
        "Título": "Superman: Man of Tomorrow",
        "Precio": 36000,
        "Stock": True,
        "Código": "DC-S01"
    },
    {
        "Producto": "Cómic",
        "Editorial": "DC",
        "Género": "Superhéroes",
        "Alineación": "Solitario",
        "Personaje/Equipo": "Wonder Woman",
        "Título": "Wonder Woman: Spirit of Truth",
        "Precio": 48500,
        "Stock": True,
        "Código": "DC-W01"
    },
    {
        "Producto": "Cómic",
        "Editorial": "DC",
        "Género": "Superhéroes",
        "Alineación": "Equipo",
        "Personaje/Equipo": "Justice League",
        "Título": "La Trinidad",
        "Precio": 50000,
        "Stock": False,
        "Código": "DC-JL01"
    },
    {
        "Producto": "Cómic",
        "Editorial": "Marvel",
        "Género": "Superhéroes",
        "Alineación": "Solitario",
        "Personaje/Equipo": "Spider-Man",
        "Título": "Spider-Man: First Year",
        "Precio": 47000,
        "Stock": True,
        "Código": "MAR-S01"
    },
    {
        "Producto": "Cómic",
        "Editorial": "Marvel",
        "Género": "Superhéroes",
        "Alineación": "Equipo",
        "Personaje/Equipo": "Avengers",
        "Título": "Civil War",
        "Precio": 50000,
        "Stock": True,
        "Código": "MAR-AV01"
    },
    {
        "Producto": "Manga",
        "Editorial": "Ivrea",
        "Género": "Bizarro",
        "Alineación": "Solitario",
        "Personaje/Equipo": "Jojo",
        "Título": "Steel Ball Run",
        "Precio": 17000,
        "Stock": False,
        "Código": "JO-JO01"
    }
]

def menu():
    print("\033[1;38;5;165m----------------***-----------------\033[0m")
    print("\033[1;38;5;10m  NADIE SE SALVA SOLO - COMIQUERÍA  \033[0m")
    print("\033[1;38;5;165m----------------***-----------------\033[0m")
    print(" ")
    print("\033[1;38;5;213m 1- Catalogo\033[0m")
    print("\033[1;38;5;53m 2- Gestion de Productos\033[0m")
    print("\033[1;38;5;99m 3- Pedidos\033[0m")
    print("\033[1;38;5;31m 4- Ultima visualizacion\033[0m")
    print("\033[1;38;5;33m 5- Salir\033[0m")
    print("")
    eleccion= int(input(f"Ingrese la opcion que desea: "))

    return eleccion

class SimpleHashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        numeric_sum = sum(int(char) for char in key if char.isdigit())
        return numeric_sum % self.size 

    def put(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value) 
                return
        bucket.append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None 

    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i] 
                return

    def print_map(self):
        print("Hash Map Contents:")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")

hash_map = SimpleHashMap()
for comic in catalago:
    hash_map.put(comic["Código"], comic)

def gestion_productos():
    print("\033[1;38;5;165m----------------***-----------------\033[0m")
    print("\033[1;38;5;10m        Gestión  -  Productos  \033[0m")
    print("\033[1;38;5;165m----------------***-----------------\033[0m")
    print("")
    print("\033[1;38;5;33m 1- Agregar Producto\033[0m")
    print("\033[1;38;5;31m 2- Actualizar Producto\033[0m")
    print("\033[1;38;5;99m 3- Eliminar Producto\033[0m")
    print("\033[1;38;5;53m 4- Buscar Producto por Código\033[0m")
    print("\033[1;38;5;213m 5- Volver\033[0m")
    print("")
    eleccion= int(input(f"Ingrese la opcion que desea: "))
    
    if eleccion == 1:
        producto = input("- Ingrese el tipo de producto que quieras anexar: ")
        titulo = input("- Ingrese el nombre de la historieta: ")
        editorial = input("- Ingrese el nombre de la editorial: ")
        genero = input("- Ingrese el genero de la historieta: ")
        alineacion = input("- Ingrese si se trata de una historia en solitario o de un equipo: ")
        personaje = input("- Ingresa el nombre del protagonista o equipo de la historia: ")    
        precio = int(input("- Ingrese el precio de tu historieta: "))
        codigo = input("- Ingrese el codigo del producto: ")
        nuevo_producto = {
            "Producto": producto,
            "Editorial": editorial,
            "Género": genero,
            "Alineación": alineacion,
            "Personaje/Equipo": personaje,
            "Título": titulo,
            "Precio": precio,
            "Stock": True,
            "Código": codigo
        }
        hash_map.put(codigo, nuevo_producto)
        catalago.append(nuevo_producto) 
        print("Producto agregado correctamente!")
    elif eleccion == 2:
        codigo = input("- Ingrese el codigo del producto: ")
        producto = hash_map.get(codigo)
        if producto:
            print("Producto encontrado")
            for clave, valor in comic.items():
                    if clave == "Precio":
                        print(f"\033[93m{clave}:\033[0m {valor}")
            eleccion= input(f"Ingrese la opcion que desea modificar(Titulo, Stock, etc): ").capitalize()
            if eleccion in producto:
                if eleccion == "Precio":
                    nuevo_precio = float(input(f"Ingrese el nuevo precio (actual: ${producto['Precio']}): "))
                    producto[eleccion] = nuevo_precio
                    print("Precio actualizado correctamente!")
                elif eleccion == "Stock":
                    nuevo_stock = input(f"Ingrese el nuevo estado de stock (actual: {'Disponible' if producto['Stock'] else 'No Disponible'}): ") == 'True'
                    producto[eleccion] = nuevo_stock
                    print("Stock actualizado correctamente!")
                else:
                    nuevo_valor = input(f"Ingrese el nuevo valor para {eleccion} (actual: {producto[eleccion]}): ")
                    producto[eleccion] = nuevo_valor
                    print(f"{eleccion} actualizado correctamente!")
                hash_map.put(codigo, producto)
                catalago.append(producto)
            else:
                print("Campo que se quiero modificar no exsiste o esta mal redactado")
        else:
            print("Producto no encontrado.")

    elif eleccion == 5:
        return
    
seleccion = menu()
while seleccion != 6:
    if seleccion == 1:
        os.system('cls')
        print("\033[1;38;5;165m----------------***-----------------\033[0m")
        print("\033[1;38;5;10m        Catalago - Productos         \033[0m")
        for comic in catalago:
            print("\033[1;38;5;165m----------------***-----------------\033[0m")
            print("")
            print("\033[1;38;5;10m\033[4m" + comic["Título"] + " - " + comic["Editorial"] + "\033[0m")
            for clave, valor in comic.items():
                if (clave != "Editorial" and clave != "Título"):
                    if clave == "Precio":
                        print(f"\033[93m{clave}:\033[0m ${valor}")
                    else:
                        print(f"\033[93m{clave}:\033[0m {valor}")
            print("")
        salir = input("\033[91mVolver atras - Presiona Enter: \033[0m")
    elif seleccion == 2:
        os.system('cls')
        gestion_productos()
    elif seleccion == 3:
        os.system('cls')
        print(3)
        print("")
        salir = input("\033[91mVolver atras - Presiona Enter: \033[0m")
    elif seleccion == 4:
        os.system('cls')
        print(4)
        print("")
        salir = input("\033[91mVolver atras - Presiona Enter: \033[0m")
    elif seleccion >= 5:
        break
    os.system('cls')
    seleccion = menu()  