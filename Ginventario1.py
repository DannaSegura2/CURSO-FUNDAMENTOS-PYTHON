productos = ["coca-cola", "sprite", "fanta", "kola-romana", "quatro"]
cantidades =[20, 20, 10, 15, 20]
stock= 15

for i in range(len(productos)):
  print(f"{i + 1}. {productos[i]}: {cantidades[i]} ")
  if cantidades[i] < stock:
    print("Productos con bajo stock: ")
    print(f"El producto {productos[i]} no tiene suficiente stock: {cantidades[i]} unidades")


producto_seleccionado =int(input("Ingrese el número del producto que desea actualizar: "))
nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

cantidades[producto_seleccionado -1] = nueva_cantidad

for i in range(len(productos)):
  print(f"{i + 1}. {productos[i]}: {cantidades[i]} ")
  if cantidades[i] < stock:
    print("Productos con bajo stock: ")
    print(f"El producto {productos[i]} no tiene suficiente stock: {cantidades[i]} unidades")