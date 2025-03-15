# Programa para eliminar todas las apariciones de un número en una lista

# Crear una lista de números (puedes modificar esta lista según tus necesidades)
numeros = [4, 7, 2, 9, 4, 5, 3, 4, 8, 2, 1, 4]
print(f"Lista original: {numeros}")

# Solicitar el número a eliminar
numero_a_eliminar = int(input("Ingrese el número que desea eliminar de la lista: "))

# Crear una nueva lista sin el número especificado
lista_final = [numero for numero in numeros if numero != numero_a_eliminar]

# Alternativa usando while y count (método tradicional)
'''
lista_final = numeros.copy()
while numero_a_eliminar in lista_final:
    lista_final.remove(numero_a_eliminar)
'''

# Mostrar la lista final
print(f"Lista después de eliminar todas las apariciones del número {numero_a_eliminar}: {lista_final}")