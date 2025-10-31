import time
import json
import os
os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("\033[1;38;5;165m----------------***-----------------\033[0m")
    print("\033[1;38;5;10m  NADIE SE SALVA SOLO - COMIQUERÍA  \033[0m")
    print("\033[1;38;5;165m----------------***-----------------\033[0m")
    print(" ")
    print("\033[1;38;5;212m 1- Catálogo\033[0m")
    print("\033[1;38;5;213m 2- Gestión de Productos\033[0m")
    print("\033[1;38;5;85m 3- Pedidos\033[0m")
    print("\033[1;38;5;84m 4- Última visualización\033[0m")
    print("\033[1;38;5;44m 5- Buscar por Categorias\033[0m")
    print("\033[1;38;5;45m 6- Salir\033[0m")
    print("")
    eleccion = int(input(f"Ingrese la opción que desea: "))
    return eleccion

def leer_catalogo():
    if not os.path.exists("catalogo.json"):
        return []
    with open("catalogo.json", encoding="utf-8") as file:
        contenido = file.read().strip()
        if not contenido:
            return []
        return json.loads(contenido)

def guardar_catalogo(data):
    with open("catalogo.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def abrir_vistas():
    if not os.path.exists("vistas.json"):
        return []
    with open("vistas.json", encoding="utf-8") as file:
        contenido = file.read().strip()
        if not contenido:
            return []
        return json.loads(contenido)
    
def guardar_vistas(data):
    with open("vistas.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def abrir_catalogo():
    data = leer_catalogo()
    if not data:
        print("El catálogo está vacío.")
        input("Presiona Enter para volver.")
        return []
    print("\033[1;38;5;165m----------------***-----------------\033[0m") 
    print("\033[1;38;5;10m        Catálogo - Productos         \033[0m")
    for comic in data:
        print("\033[1;38;5;165m----------------***-----------------\033[0m")
        print("")
        print(f"\033[1;38;5;10m\033[4m{comic['Título']} - {comic['Editorial']}\033[0m")
        for clave, valor in comic.items():
            if clave not in ("Editorial", "Título"):
                if clave == "Precio":
                    print(f"\033[93m{clave}:\033[0m ${valor}")
                else:
                    print(f"\033[93m{clave}:\033[0m {valor}")
        print("")    
    input("\033[91mVolver atrás - Presiona Enter: \033[0m")
    return data

class Historial:
    def __init__(self):
        self.ultimos_productos = abrir_vistas()
    def agregar(self, producto):
        if producto is None:  
            return
        if producto in self.ultimos_productos:
            self.ultimos_productos.remove(producto)
            self.ultimos_productos.append(producto)
        else:
            self.ultimos_productos.append(producto)
            if len(self.ultimos_productos) > 5:
                self.ultimos_productos.pop(0)
        guardar_vistas(self.ultimos_productos)
    def mostrar(self):
        if not self.ultimos_productos:
            print("\033[1;38;5;213mNo hay productos vistos recientemente.\033[0m")
            return
        contador = 1
        tonos_rosa = [165, 171, 177, 183, 219]
        for i, producto in enumerate(reversed(self.ultimos_productos)):
            color = tonos_rosa[min(i, len(tonos_rosa) - 1)]
            print(f"\033[1;38;5;{color}m {contador}- "f"{producto['Título']} - {producto['Editorial']}\033[0m")
            contador += 1
        print("")
guardar_historial = Historial()

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

hash_map = SimpleHashMap()
for comic in leer_catalogo():
    hash_map.put(comic["Código"], comic)

def gestion_productos():
    os.system('cls' if os.name == 'nt' else 'clear')
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
    eleccion = int(input(f"Ingrese la opción que desea: "))
    if eleccion == 1:
        producto = input("- Ingrese el tipo de producto que quieras anexar: ")
        titulo = input("- Ingrese el nombre de la historieta: ")
        editorial = input("- Ingrese el nombre de la editorial: ")
        genero = input("- Ingrese el género de la historieta: ")
        alineacion = input("- Ingrese si se trata de una historia en solitario o de un equipo: ")
        personaje = input("- Ingresa el nombre del protagonista o equipo de la historia: ")    
        precio = int(input("- Ingrese el precio de tu historieta: "))
        codigo = input("- Ingrese el código del producto: ")
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
        catalogo = leer_catalogo()
        catalogo.append(nuevo_producto)
        guardar_catalogo(catalogo)
        hash_map.put(codigo, nuevo_producto)
        print("Producto agregado correctamente!")
        time.sleep(1)
        return gestion_productos()
    elif eleccion == 2:
        codigo = input("- Ingrese el código del producto: ")
        producto = hash_map.get(codigo)
        if producto:
            print("Producto encontrado:")
            print(f"\033[1;38;5;10m\033[4m{producto['Título']} - {producto['Editorial']}\033[0m")
            for clave, valor in producto.items():
                if clave not in ("Editorial", "Título"):
                    if clave == "Precio":
                        print(f"\033[93m{clave}:\033[0m ${valor}")
                    else:
                        print(f"\033[93m{clave}:\033[0m {valor}")
            campo = input(f"Ingrese el campo que desea modificar (Título, Precio, Stock, etc): ").capitalize()
            if campo in producto:
                if campo == "Precio":
                    producto[campo] = int(input(f"Ingrese el nuevo precio, precio actual \033[92m${producto[campo]}\033[0m: "))
                elif campo == "Stock":
                    producto[campo] = input(f"¿Hay stock? (True/False), actualmente \033[96m{producto[campo]}\033[0m: ").capitalize() == "True"
                else:
                    producto[campo] = input(f"Ingrese el nuevo valor para {campo}, valor actuaL \033[96m{producto[campo]}\033[0m: ")
                hash_map.put(codigo, producto)
                catalogo = leer_catalogo()
                for i, p in enumerate(catalogo):
                    if p["Código"] == codigo:
                        catalogo[i] = producto
                        break
                guardar_catalogo(catalogo)
                print("Producto actualizado correctamente!")
                time.sleep(1)
            else:
                print("Campo no válido.")
                time.sleep(1)
        else:
            print("Producto no encontrado.")
            time.sleep(1)
        return gestion_productos()
    elif eleccion == 3:
        codigo = input("- Ingrese el código del producto: ")
        producto = hash_map.get(codigo)
        if producto:
            print("Producto encontrado:")
            print(f"\033[1;38;5;10m\033[4m{producto['Título']} - {producto['Editorial']}\033[0m")
            for clave, valor in producto.items():
                if clave not in ("Editorial", "Título"):
                    if clave == "Precio":
                        print(f"\033[93m{clave}:\033[0m ${valor}")
                    else:
                        print(f"\033[93m{clave}:\033[0m {valor}")
            confirmacion = input("¿Está seguro que desea eliminar este producto? (si/no): ").lower()
            if confirmacion == "si":
                hash_map.remove(codigo)
                catalogo = leer_catalogo()
                catalogo = [p for p in catalogo if p["Código"] != codigo]
                guardar_catalogo(catalogo)
                print("Producto eliminado correctamente!")
                time.sleep(1)
            else:
                print("Eliminación cancelada.")
                time.sleep(1)
        else:
            print("Producto no encontrado.")
            time.sleep(1)
        return gestion_productos()
    elif eleccion == 4:
        codigo = input("- Ingrese el código del producto: ")
        producto = hash_map.get(codigo)
        guardar_historial.agregar(producto)
        if producto:
            print("Producto encontrado:")
            print(f"\033[1;38;5;10m\033[4m{producto['Título']} - {producto['Editorial']}\033[0m")
            for clave, valor in producto.items():
                if clave not in ("Editorial", "Título"):
                    if clave == "Precio":
                        print(f"\033[93m{clave}:\033[0m ${valor}")
                    else:
                        print(f"\033[93m{clave}:\033[0m {valor}")
        else:
            print("Producto no encontrado.")
        input("\033[91mVolver atrás - Presiona Enter: \033[0m")
        return gestion_productos()
    elif eleccion == 5:
        return

seleccion = menu()
while seleccion != 6:
    os.system('cls' if os.name == 'nt' else 'clear')
    if seleccion == 1:
        abrir_catalogo()
    elif seleccion == 2:
        gestion_productos()
    elif seleccion == 3:
        print("Sección de pedidos (en desarrollo).")
        input("\033[91mVolver atrás - Presiona Enter: \033[0m")
    elif seleccion == 4:
        print("\033[1;38;5;165m----------------***-----------------\033[0m")
        print("\033[1;38;5;10m      Últimos Productos Vistos     \033[0m")
        print("\033[1;38;5;165m----------------***-----------------\033[0m")
        print("")
        guardar_historial.mostrar()
        print("")
        input("\033[91mVolver atrás - Presiona Enter: \033[0m")
    elif seleccion == 5:
        print("Categorizacion (en desarrollo).")
        input("\033[91mVolver atrás - Presiona Enter: \033[0m")
    else:
        print("Opción no válida.")
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    seleccion = menu()