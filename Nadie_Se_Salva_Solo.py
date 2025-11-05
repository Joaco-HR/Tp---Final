import time
import json
import os
from collections import deque

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
    eleccion = input(f"Ingrese la opción que desea: ")
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

def abrir_pedidos():
    if not os.path.exists("pedidos.json"):
        return []
    with open("pedidos.json", encoding="utf-8") as file:
        contenido = file.read().strip()
        if not contenido:
            return []
        return json.loads(contenido)
    
def guardar_pedidos(data):
     with open("pedidos.json", "w", encoding="utf-8") as file:
        json.dump(list(data), file, ensure_ascii=False, indent=4)
        
def input_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("⚠️  Este campo no puede estar vacío.")
            continue
        if any(char.isdigit() for char in valor):
            print("⚠️  No se permiten números. Intente nuevamente.")
            continue
        return valor

def input_numero(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        else:
            print("⚠️  Solo se permiten números enteros positivos. Intente nuevamente.")
            
def input_stock(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor == "True":
            return True
        elif valor == "False":
            return False
        else:
            print("⚠️  Solo se permite ingresar 'True' o 'False'. Intente nuevamente.")

def input_codigo(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("⚠️  El código no puede estar vacío.")
        elif " " in valor:
            print("⚠️  El código no debe contener espacios.")
        else:
            return valor
            
def mostrar_catalogo():
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
        titulo = comic.get("Título", "Sin título")
        editorial = comic.get("Editorial", "Desconocida")
        print(f"\033[1;38;5;10m\033[4m{titulo} - {editorial}\033[0m")
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

class Categoria:
    COLORES_NIVELES = ["\033[38;5;226m","\033[38;5;220m","\033[38;5;214m","\033[38;5;178m","\033[38;5;136m"]
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = {}
        self.productos = []

    def agregar_producto(self, niveles, producto):
        if not niveles:
            self.productos.append(producto)
            return
        nivel = niveles[0]
        if nivel not in self.subcategorias:
            self.subcategorias[nivel] = Categoria(nivel)
        self.subcategorias[nivel].agregar_producto(niveles[1:], producto)

    def color_por_nivel(self, nivel):
        return self.COLORES_NIVELES[nivel] if nivel < len(self.COLORES_NIVELES) else self.COLORES_NIVELES[-1]

    def mostrar(self, nivel=0):
        sangria = "   " * nivel
        color = self.color_por_nivel(nivel)
        print(f"{sangria}{color}- {self.nombre}\033[0m")

        for sub in self.subcategorias.values():
            sub.mostrar(nivel + 1)

        for p in self.productos:
            print(f"{sangria}   - {p['Título']}")

    def buscar_categoria(self, nombre):
        resultados = []
        if self.nombre.lower() == nombre.lower():
            resultados.append(self)
        for sub in self.subcategorias.values():
            resultados.extend(sub.buscar_categoria(nombre))
        return resultados

    def mostrar_resultados(self, nombre):
        resultados = self.buscar_categoria(nombre)
        if not resultados:
            print("\033[91mNo se encontraron categorías con ese nombre.\033[0m")
        else:
            for nodo in resultados:
                print(f"\n\033[1;38;5;171mResultados para \033[1;33m{nodo.nombre}\033[0m:")
                nodo.mostrar()

def construir_arbol_catalogo(catalogo):
    raiz = Categoria("Categorías")
    for producto in catalogo:
        niveles = [
            producto.get("Producto", "Desconocido"),
            producto.get("Editorial", "Desconocido"),
            producto.get("Personaje/Equipo", "General")
        ]
        raiz.agregar_producto(niveles, producto)
    return raiz

class SimpleHashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]
    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size
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
    while True:
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
        eleccion = input("Ingrese la opción que desea: ").strip()
        if eleccion == "1":
            producto = input_texto("- Ingrese el tipo de producto que quieras anexar: ")
            titulo = input_texto("- Ingrese el nombre de la historieta: ")
            editorial = input_texto("- Ingrese el nombre de la editorial: ")
            genero = input_texto("- Ingrese el género de la historieta: ")
            alineacion = input_texto("- Ingrese si se trata de una historia en solitario o de un equipo: ")
            personaje = input_texto("- Ingresa el nombre del protagonista o equipo de la historia: ")
            precio = input_numero("- Ingrese el precio de tu historieta: ")
            stock = input_stock("- Ingrese el valor del Stock(TRUE/FALSE): ")
            codigo = input_codigo("- Ingrese el código del producto: ")
    
            catalogo = leer_catalogo()
            if any(p["Código"] == codigo for p in catalogo):
                print("⚠️  Ese código ya existe.")
                time.sleep(1)
    
            nuevo_producto = {
                "Producto": producto,
                "Editorial": editorial,
                "Género": genero,
                "Alineación": alineacion,
                "Personaje/Equipo": personaje,
                "Título": titulo,
                "Precio": precio,
                "Stock": stock,
                "Código": codigo
            }
    
            catalogo.append(nuevo_producto)
            guardar_catalogo(catalogo)
            hash_map.put(codigo, nuevo_producto)
            print("✅ Producto agregado correctamente!")
            time.sleep(1)
        elif eleccion == "2":
            codigo = input("- Ingrese el código del producto: ").upper()
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
                campo = input_texto("Ingrese el campo que desea modificar: ")
                campo_real = None
                for k in producto.keys():
                    if k.lower() == campo.lower():
                        campo_real = k
                        break
                if campo_real:
                    if campo_real == "Precio": 
                        producto[campo_real] = int(input(f"Ingrese el nuevo precio, precio actual \033[92m${producto[campo_real]}\033[0m: ")) 
                    elif campo_real == "Stock": 
                        producto[campo_real] = input(f"¿Hay stock? (True/False), actualmente \033[96m{producto[campo_real]}\033[0m: ").capitalize() == "True" 
                    else: 
                        producto[campo_real] = input(f"Ingrese el nuevo valor para {campo_real}, valor actuaL \033[96m{producto[campo_real]}\033[0m: ")
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
        elif eleccion == "3":
            codigo = input("- Ingrese el código del producto: ").upper()
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
                confirmacion = input_texto("¿Está seguro que desea eliminar este producto? (si/no): ").lower()
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
        elif eleccion == "4":
            codigo = input("- Ingrese el código del producto: ").upper()
            producto = hash_map.get(codigo)
            if producto:
                guardar_historial.agregar(producto)
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
            input("\033[91mPresiona Enter para continuar...\033[0m")
        elif eleccion == "5":
            return
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("⚠️  Opción no válida.")
            time.sleep(1)

cola_pedidos = deque(abrir_pedidos())

def pedidos():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[1;38;5;165m----------------***-----------------\033[0m")
        print("\033[1;38;5;10m         Gestión de Pedidos         \033[0m")
        print("\033[1;38;5;165m----------------***-----------------\033[0m")
        print("")
        print("\033[1;38;5;33m 1- Nuevo pedido\033[0m")          
        print("\033[1;38;5;31m 2- Ver pedidos pendientes\033[0m") 
        print("\033[1;38;5;99m 3- Procesar siguiente pedido\033[0m") 
        print("\033[1;38;5;53m 4- Volver\033[0m")
        print("")
        eleccion = input(f"Ingrese la opción que desea: ")

        if eleccion == "1":
            cliente = input_texto("Nombre del cliente: ")
            carrito = []
            while True:
                codigo = input("Código del producto: ").upper()
                producto = hash_map.get(codigo)
                if producto:
                    if producto["Stock"]:
                        print(f"\033[1;38;5;10m\033[4m{producto['Título']} - {producto['Editorial']}\033[0m")
                        for clave, valor in producto.items():
                            if clave not in ("Editorial", "Título"):
                                if clave == "Precio":
                                    print(f"\033[93m- {clave}:\033[0m ${valor}")
                                else:
                                    print(f"\033[93m- {clave}:\033[0m {valor}")
                        cantidad = input_numero("\nCantidad deseada: ")
                        cantidad = int(cantidad)
                        carrito.append({"producto": producto, "cantidad": cantidad})
                        otro = input_texto("¿Deseas agregar otro producto al pedido? (si/no): ").lower()
                        if otro != "si":
                            break
                    else:
                        print("\n\033[91m ⚠️  Este producto no tiene stock disponible.\033[0m")
                        continuar = input_texto("¿Deseas buscar otro producto al pedido? (si/no): ").lower()
                        if continuar != "si":
                            break
                else:
                    print("\033[91m⚠️  Código no encontrado.\033[0m")
                    continuar = input_texto("¿Deseas buscar otro producto al pedido? (si/no): ").lower()
                    if continuar != "si":
                        break
            if carrito:
                pedido = {"cliente": cliente, "productos": carrito, "hora": time.strftime("%H:%M:%S")}
                cola_pedidos.append(pedido)
                guardar_pedidos(cola_pedidos)
                print("\n\033[92mPedido agregado correctamente.\033[0m")
            input("Presiona Enter para volver...")
        elif eleccion == "2":
            if not cola_pedidos:
                print("No hay pedidos pendientes.")
            else:
                print("Pedidos pendientes:")
                for i, p in enumerate(cola_pedidos, 1):
                    print(f"{i}- {p['cliente']} realizó un pedido del producto/os:")
                    for item in p["productos"]:
                        prod = item["producto"]
                        print(f"   \033[96m{item['cantidad']}x {prod['Título']} - {prod['Editorial']}\033[0m a las {p['hora']}.")
                    print("")
            input("\033[91mPresiona Enter para continuar...\033[0m")
        elif eleccion == "3":
            if not cola_pedidos:
                print("No hay pedidos para procesar.")
            else:
                atendido = cola_pedidos.popleft()
                guardar_pedidos(cola_pedidos)
                print(f"\nProcesando pedido de \033[1;38;5;213m{atendido['cliente']}\033[0m:")
                for item in atendido["productos"]:
                    prod = item["producto"]
                    print(f"   - {item['cantidad']}x {prod['Título']} ({prod['Editorial']})")
                print("Procesando Pedido...")
                time.sleep(2    )
            input("\033[91mPresiona Enter para continuar...\033[0m")
        elif eleccion == "4":
            return
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("⚠️  Opción no válida.")
            time.sleep(1)
            return pedidos()

def abrir_categorias():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[1;38;5;165m----------------***-----------------\033[0m")
        print("\033[1;38;5;10m       BÚSQUEDA POR CATEGORÍAS      \033[0m")
        print("\033[1;38;5;165m----------------***-----------------\033[0m")
        print("")
        print("\033[1;38;5;33m 1- Ver árbol completo\033[0m")
        print("\033[1;38;5;99m 2- Buscar categoría específica\033[0m")
        print("\033[1;38;5;213m 3- Volver\033[0m")
        print("")

        opcion_cat = input("Ingrese la opción que desea: ").strip()
        catalogo = leer_catalogo()
        raiz = construir_arbol_catalogo(catalogo)

        if opcion_cat == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[1;38;5;165m----------------***-----------------\033[0m")
            print("\033[1;38;5;10m     Arbol - Categorias Completo  \033[0m")
            print("\033[1;38;5;165m----------------***-----------------\n\033[0m")
            raiz.mostrar()
            input("\n\033[91mPresiona Enter para volver...\033[0m")
        elif opcion_cat == "2":
            nombre = input_texto("Ingrese el nombre de la categoría a buscar: ").strip()
            raiz.mostrar_resultados(nombre)
            input("\n\033[91mPresiona Enter para volver...\033[0m")
        elif opcion_cat == "3":
            break
        else:
            print("⚠️  Opción no válida.")
            time.sleep(1)

seleccion = menu()
while seleccion != "6":
    os.system('cls' if os.name == 'nt' else 'clear')
    if seleccion == "1":
        mostrar_catalogo()
    elif seleccion == "2":
        gestion_productos()
    elif seleccion == "3":
        pedidos()
    elif seleccion == "4":
        print("\033[1;38;5;165m----------------***-----------------\033[0m")
        print("\033[1;38;5;10m      Últimos Productos Vistos     \033[0m")
        print("\033[1;38;5;165m----------------***-----------------\033[0m")
        print("")
        guardar_historial.mostrar()
        print("")
        input("\033[91mPresiona Enter para continuar...\033[0m")
    elif seleccion == "5":
        abrir_categorias()
    elif seleccion == "6":
        break
    else:
        print("⚠️  Opción no válida.")
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    seleccion = menu()