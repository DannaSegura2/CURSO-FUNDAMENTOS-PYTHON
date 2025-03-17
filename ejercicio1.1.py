# Programa para crear una lista y mostrarla invertida

# Solicitar la cantidad de elementos
cantidad = int(input("¿Cuántos elementos desea ingresar en la lista? "))

# Crear una lista vacía
lista = []

# Solicitar cada elemento
for i in range(cantidad):
    elemento = input(f"Ingrese el elemento {i+1}: ")
    lista.append(elemento)

# Mostrar la lista original
print("\nLista original:")
print(lista)

# Mostrar la lista invertida
lista_invertida = lista[::-1]  # Crea una copia invertida de la lista
print("\nLista invertida:")
print(lista_invertida)