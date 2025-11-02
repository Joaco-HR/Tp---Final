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

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = {}
        self.productos = []

    def agregar_subcategoria(self, subcat):
        self.subcategorias[subcat.nombre] = subcat

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def obtener_todos_productos(self):
        resultado = list(self.productos)
        for subcat in self.subcategorias.values():
            resultado.extend(subcat.obtener_todos_productos())
        return resultado

    def mostrar_arbol(self, nivel=0):
        print("  " * nivel + f"- {self.nombre} ({len(self.productos)} productos)")
        for subcat in self.subcategorias.values():
            subcat.mostrar_arbol(nivel + 1)

# ===================== Función para crear árbol de categorías =====================
def crear_arbol_categorias(productos):
    root = Categoria("Categorías")
    tipo_map = {}
    for p in productos:
        tipo = p["Producto"]
        editorial = p["Editorial"]
        personaje = p["Personaje/Equipo"]

        # Crear categoría tipo
        if tipo not in tipo_map:
            tipo_map[tipo] = Categoria(tipo)
            root.agregar_subcategoria(tipo_map[tipo])
        tipo_cat = tipo_map[tipo]

        # Crear subcategoría editorial
        if editorial not in tipo_cat.subcategorias:
            tipo_cat.agregar_subcategoria(Categoria(editorial))
        editorial_cat = tipo_cat.subcategorias[editorial]

        # Crear subcategoría personaje/equipo
        if personaje not in editorial_cat.subcategorias:
            editorial_cat.agregar_subcategoria(Categoria(personaje))
        personaje_cat = editorial_cat.subcategorias[personaje]

        # Agregar producto final
        personaje_cat.agregar_producto(p)

    return root

# ===================== Función para mostrar productos por categoría =====================
def explorar_categorias():
    productos = leer_catalogo()
    if not productos:
        print("No hay productos en el catálogo.")
        input("Presiona Enter para volver...")
        return
    root = crear_arbol_categorias(productos)

    nodo_actual = root
    path = []

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\033[1;38;5;165m{' > '.join([n.nombre for n in path] + [nodo_actual.nombre])}\033[0m")
        print("Subcategorías:")
        for i, subcat in enumerate(nodo_actual.subcategorias.values(), 1):
            print(f"  {i}- {subcat.nombre} ({len(subcat.obtener_todos_productos())} productos)")
        print("0- Volver atrás")
        print("p- Ver productos en esta categoría")
        eleccion = input("Ingrese opción: ").strip().lower()
        if eleccion == "0":
            if not path:
                break
            nodo_actual = path.pop()
        elif eleccion == "p":
            productos = nodo_actual.obtener_todos_productos()
            if not productos:
                print("No hay productos en esta categoría.")
            else:
                print(f"\nProductos en {nodo_actual.nombre}:")
                for prod in productos:
                    print(f"- {prod['Título']} ({prod['Editorial']}) - ${prod['Precio']}")
            input("\nPresiona Enter para continuar...")
        elif eleccion.isdigit() and 1 <= int(eleccion) <= len(nodo_actual.subcategorias):
            idx = int(eleccion) - 1
            subcat = list(nodo_actual.subcategorias.values())[idx]
            path.append(nodo_actual)
            nodo_actual = subcat
        else:
            print("Opción no válida.")
            time.sleep(1)

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
    eleccion = input(f"Ingrese la opción que desea: ")
    if eleccion == "1":
        producto = input("- Ingrese el tipo de producto que quieras anexar: ")
        titulo = input("- Ingrese el nombre de la historieta: ")
        editorial = input("- Ingrese el nombre de la editorial: ")
        genero = input("- Ingrese el género de la historieta: ")
        alineacion = input("- Ingrese si se trata de una historia en solitario o de un equipo: ")
        personaje = input("- Ingresa el nombre del protagonista o equipo de la historia: ")    
        precio = int(input("- Ingrese el precio de tu historieta: "))
        codigo = input("- Ingrese el código del producto: ")
        catalogo = leer_catalogo()
        if any(p["Código"] == codigo for p in catalogo):
            print("Ese código ya existe.")
            time.sleep(1)
            return gestion_productos()
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
        catalogo.append(nuevo_producto)
        guardar_catalogo(catalogo)
        hash_map.put(codigo, nuevo_producto)
        print("Producto agregado correctamente!")
        time.sleep(1)
        return gestion_productos()
    elif eleccion == "2":
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
            campo = input("Ingrese el campo que desea modificar: ")
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
        return gestion_productos()
    elif eleccion == "3":
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
    elif eleccion == "4":
        codigo = input("- Ingrese el código del producto: ")
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
        return gestion_productos()
    elif eleccion == "5":
        return
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opción no válida.")
        time.sleep(1)
        return gestion_productos()

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
        print("\033[1;38;5;53m4- Volver\033[0m")
        print("")
        eleccion = input(f"Ingrese la opción que desea: ")

        if eleccion == "1":
            cliente = input("Nombre del cliente: ")
            carrito = []
            while True:
                codigo = input("Código del producto: ").strip().upper()
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
                        cantidad = input("\nCantidad deseada: ")
                        if not cantidad.isdigit() or int(cantidad) <= 0:
                            print("\033[91mCantidad inválida.\033[0m")
                            continue
                        cantidad = int(cantidad)
                        carrito.append({"producto": producto, "cantidad": cantidad})
                        otro = input("¿Deseas agregar otro producto al pedido? (si/no): ").lower()
                        if otro != "si":
                            break
                    else:
                        print("\n\033[91mEste producto no tiene stock disponible.\033[0m")
                        continuar = input("¿Deseas buscar otro producto al pedido? (si/no): ").lower()
                        if continuar != "si":
                            break
                else:
                    print("\033[91mCódigo no encontrado.\033[0m")
                    continuar = input("¿Deseas buscar otro producto al pedido? (si/no): ").lower()
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
            input("\033[91mPresiona Enter para continuar...\033[0m")
        elif eleccion == "4":
            return
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opción no válida.")
            time.sleep(1)
            return pedidos()
    
seleccion = menu()
while seleccion != "6":
    os.system('cls' if os.name == 'nt' else 'clear')
    if seleccion == "1":
        abrir_catalogo()
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
        explorar_categorias()
    elif seleccion == "6":
        break
    else:
        print("Opción no válida.")
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    seleccion = menu()