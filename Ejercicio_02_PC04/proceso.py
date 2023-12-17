# proceso.py
from modulos.bd import *
from modulos.log import *

logger = Log()
BdIv2 = Bd()

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def tuplaDatos(self):
        return (self.name, self.price, self.stock)

def crear_producto(user, database):
    print("Ingrese información del producto")
    name = input("Ingrese el valor para nombre: ")
    price = float(input("Ingrese el valor para precio: "))
    stock = int(input("Ingrese el valor para stock: "))
    p1 = Product(name, price, stock)

    try:
        query = "INSERT INTO products(name, price, stock) VALUES (?, ?, ?)"
        database.execute_query(query, (p1.name, p1.price, p1.stock))
        log_info = f"-{user}-creó un producto: {p1.name}, {p1.price}, {p1.stock}"
        logger.register_log(log_info)
    except Exception as e:
        log_info = f"-{user}-error al crear un producto: {e}"
        logger.register_log(log_info)

def listar_producto(user, database):
    print("Lista de productos:")
    print('id | nombre | precio | stock')
    query = "SELECT * FROM products"

    try:
        data = database.get_data(query)
        log_info = f"-{user}-listó los productos"
        logger.register_log(log_info)
        for i in data:
            print(i[0], i[1], i[2], i[3])
    except Exception as e:
        log_info = f"-{user}-error al listar los productos: {e}"
        logger.register_log(log_info)

def eliminar_producto(user, database):
    id_producto = int(input("Ingrese el id del producto a eliminar: "))
    query = f"DELETE FROM products WHERE id = {id_producto}"
    try:
        database.execute_query(query)
        log_info = f"-{user}-se eliminó un producto con id {id_producto}"
        logger.register_log(log_info)
    except Exception as e:
        log_info = f"-{user}-error al eliminar el producto: {e}"
        logger.register_log(log_info)

def editar_nombre(user, database):
    print("Actualizar el nombre del producto")
    id_producto = int(input("Ingrese el id del producto a actualizar: "))
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    query = f"UPDATE products SET name = '{nuevo_nombre}' WHERE id = {id_producto}"
    try:
        database.execute_query(query)
        log_info = f"-{user}-se actualizó el nombre de un producto con id {id_producto}"
        logger.register_log(log_info)
    except Exception as e:
        log_info = f"-{user}-error al actualizar el nombre del producto: {e}"
        logger.register_log(log_info)

def editar_precio_o_stock(user, database):
    print("Editar precio o stock del producto")
    id_producto = int(input("Ingrese el id del producto a editar: "))
    opcion = input("Seleccione la opción a editar (1. Precio, 2. Stock): ")

    if opcion == "1":
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        query = f"UPDATE products SET price = {nuevo_precio} WHERE id = {id_producto}"
        campo_editado = "precio"
    elif opcion == "2":
        nuevo_stock = int(input("Ingrese el nuevo stock: "))
        query = f"UPDATE products SET stock = {nuevo_stock} WHERE id = {id_producto}"
        campo_editado = "stock"
    else:
        print("Opción no válida.")
        return

    try:
        database.execute_query(query)
        log_info = f"-{user}-se actualizó el {campo_editado} del producto con id {id_producto}"
        logger.register_log(log_info)
    except Exception as e:
        log_info = f"-{user}-error al actualizar el {campo_editado} del producto: {e}"
        logger.register_log(log_info)

def buscar_producto_por_nombre(user, database):
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    query = f"SELECT * FROM products WHERE name LIKE '%{nombre_buscar}%'"

    try:
        data = database.get_data(query)
        log_info = f"-{user}-buscó productos por nombre: {nombre_buscar}"
        logger.register_log(log_info)

        if not data:
            print(f"No se encontraron productos con el nombre '{nombre_buscar}'.")
        else:
            print("Resultados de la búsqueda:")
            print('id | nombre | precio | stock')
            for i in data:
                print(i[0], i[1], i[2], i[3])
    except Exception as e:
        log_info = f"-{user}-error al buscar productos por nombre: {e}"
        logger.register_log(log_info)

# Agrega esta línea para ejecutar la función principal del archivo proceso.py si se ejecuta como script
if __name__ == '__main__':
    main()
