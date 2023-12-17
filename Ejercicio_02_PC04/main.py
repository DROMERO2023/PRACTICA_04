from modulos.bd import Bd
from modulos.proceso import *
from pyfiglet import Figlet
import random
from modulos.Jobs import actualizar_tipo_cambio

figlet = Figlet()
database = None

class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

def main():
    salir = False
    init = True

    while not salir:
        # Flag para que se inicie solo una vez
        if init:
            user = input("Ingrese su nombre de usuario temporal: ")
            init = False
            config()  # Ejecutar las consideraciones básicas al iniciar la aplicación

        # Solicitar al usuario que ingrese el nuevo título
        nuevo_titulo = input("Ingrese el nuevo título: ")

        # Seleccionar una fuente aleatoria de pyfiglet
        fuente_seleccionada = random.choice(figlet.getFonts())
        figlet.setFont(font=fuente_seleccionada)

        opciones = f"""
        {figlet.renderText(nuevo_titulo)}
        1. Crear producto
        2. Listar productos
        3. Buscar producto por nombre
        4. Editar nombre de producto 
        5. Eliminar producto
        6. Actualizar tipo de cambio
        7. Editar precio o stock
        8. Agregar cliente
        9. Listar clientes
        10. Salir"""
        
        print(opciones)
        opc = int(input("Ingrese una opción: "))

        if opc == 1:
            crear_producto(user)
        elif opc == 2:
            listar_producto(user)
        elif opc == 3:
            # Solicitar al usuario que ingrese el nombre del producto a buscar
            nombre_producto = input("Ingrese el nombre del producto a buscar: ")
            buscar_producto_por_nombre(nombre_producto)
        elif opc == 4:
            editar_nombre(user)
        elif opc == 5:
            eliminar_producto(user)
        elif opc == 6:
            # Llamar a la función de Jobs.py para actualizar el tipo de cambio
            actualizar_tipo_cambio()
        elif opc == 7:
            # Llamar a la función para editar precio o stock
            editar_precio_o_stock()
        elif opc == 8:
            agregar_cliente(user)
        elif opc == 9:
            listar_clientes(user)
        elif opc == 10:
            salir = True
            print("Terminando sesión....")
            break
        else:
            print("Ingrese una opción válida")

# Función que configura la inicialización de la aplicación
def config():
    global database
    database = Bd()

    # Crear la tabla products
    query_products = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        );
    """
    database.execute_query(query_products)

    # Crear la tabla tipo_cambio
    query_tipo_cambio = """
        CREATE TABLE IF NOT EXISTS tipo_cambio (
            id INTEGER PRIMARY KEY,
            fecha DATE NOT NULL,
            valor_cambio REAL NOT NULL
        );
    """
    database.execute_query(query_tipo_cambio)

    # Crear la tabla cliente
    query_cliente = """
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            direccion VARCHAR(200) NOT NULL,
            telefono VARCHAR(20) NOT NULL
        );
    """
    database.execute_query(query_cliente)

# Función para buscar producto por nombre
def buscar_producto_por_nombre(nombre_producto):
    # Implementa la lógica para buscar el producto por nombre en la base de datos
    print(f"Buscando producto por nombre: {nombre_producto}")

# Función para agregar un cliente
def agregar_cliente(user):
    print("Agregar cliente:")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    direccion_cliente = input("Ingrese la dirección del cliente: ")
    telefono_cliente = input("Ingrese el teléfono del cliente: ")

    cliente = Cliente(nombre_cliente, direccion_cliente, telefono_cliente)
    query_insert_cliente = "INSERT INTO cliente (nombre, direccion, telefono) VALUES (?, ?, ?)"

    try:
        database.execute_query(query_insert_cliente, (cliente.nombre, cliente.direccion, cliente.telefono))
        log_info = f"-{user}-se agregó un cliente: {cliente.nombre}, {cliente.direccion}, {cliente.telefono}"
        logger.register_log(log_info)
    except Exception as e:
        log_info = f"-{user}-error al agregar cliente: {e}"
        logger.register_log(log_info)

# Función para listar clientes
def listar_clientes(user):
    print("Lista de clientes:")
    print('id | nombre | direccion | telefono')
    query_listar_clientes = "SELECT * FROM cliente"

    try:
        data = database.get_data(query_listar_clientes)
        for i in data:
            print(i[0], i[1], i[2], i[3])
        log_info = f"-{user}-listó los clientes"
        logger.register_log(log_info)
    except Exception as e:
        log_info = f"-{user}-error al listar los clientes: {e}"
        logger.register_log(log_info)

if __name__ == '__main__':
    main()
