#Crea una aplicación que administre el inventario de una tienda usando un diccionario, donde cada clave representa el nombre de un producto y cada valor la cantidad en stock. 
# La aplicación debe permitir consultar la cantidad de un producto, actualizar el stock de uno existente, agregar nuevos productos y eliminar aquellos que ya no estén disponibles. 
# Al final se mostrará el inventario actualizado.

inventario = {
    "manzanas": 50,
    "naranjas": 30,
    "peras": 20
}

print("Inventario inicial:")
print(inventario)
print()

def consultar_producto(nombre):
    if nombre in inventario:
        return inventario[nombre]
    else:
        return "Producto no encontrado"

def actualizar_stock(nombre, cantidad):
    if nombre in inventario:
        inventario[nombre] = cantidad
        print(f"Actualizando stock de {nombre} a {cantidad}.")
    else:
        print(f"El producto {nombre} no existe en el inventario.")

def agregar_producto(nombre, cantidad):
    if nombre not in inventario:
        inventario[nombre] = cantidad
        print(f"Agregando producto: \"{nombre}\" con stock {cantidad}.")
    else:
        print(f"El producto {nombre} ya existe. Use actualizar stock.")


def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"Eliminando producto: \"{nombre}\".")
    else:
        print(f"El producto {nombre} no existe en el inventario.")


producto = "naranjas"
cantidad = consultar_producto(producto)
print(f"Consulta: ¿Cuántas {producto} hay? -> {cantidad}")
print()


actualizar_stock("peras", 25)
agregar_producto("bananas", 40)
eliminar_producto("naranjas")
print()
print("Inventario final:")
print(inventario)