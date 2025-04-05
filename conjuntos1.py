#Se dispone de una lista de códigos de productos que puede contener elementos duplicados. El reto consiste en convertir la lista en una colección que elimine los duplicados, agregar 
# un nuevo producto al conjunto y luego descartar un producto específico. Posteriormente, se compararán dos colecciones (por ejemplo, inventarios de dos almacenes) para identificar los 
# productos comunes, aquellos exclusivos de cada inventario y los que no se repiten entre ambos.


productos_lista = [101, 102, 103, 104, 105, 101, 102]
inventario = set(productos_lista)


print(f"Inventario original: {inventario}")
producto_nuevo = 110
inventario.add(producto_nuevo)

print(f"Inventario tras agregar producto {producto_nuevo}: {inventario}")
producto_descartar = 103
inventario.discard(producto_descartar)

print(f"Inventario tras descartar producto {producto_descartar}: {inventario}")
print()
almacen_a = {101, 102, 104, 110}
print(f"Inventario Almacén A: {almacen_a}")
almacen_b = {102, 104, 107, 110}

print(f"Inventario Almacén B: {almacen_b}")
productos_comunes = almacen_a.intersection(almacen_b)

print(f"Productos comunes: {productos_comunes}")
exclusivos_a = almacen_a.difference(almacen_b)

print(f"Productos exclusivos en Almacén A: {exclusivos_a}")
exclusivos_b = almacen_b.difference(almacen_a)

print(f"Productos exclusivos en Almacén B: {exclusivos_b}")