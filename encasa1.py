numeros_divisibles = []
posiciones_divisibles = []
contador_no_divisibles = 0
suma_divisibles = 0

# Procesar números del 1 al 20
for i in range(1, 21):
    # Verificar si el número es divisible por 2
    if i % 2 == 0:
        numeros_divisibles.append(i)
        posiciones_divisibles.append(i)  
        # La posición coincide con el número en este caso
        suma_divisibles += i
    else:
        contador_no_divisibles += 1


print("Números divisibles por 2 y sus posiciones:")
for i in range(len(numeros_divisibles)):
    print(f"Número: {numeros_divisibles[i]}, Posición: {posiciones_divisibles[i]}")

print(f"\nCantidad de números no divisibles por 2: {contador_no_divisibles}")
print(f"Suma de los números divisibles por 2: {suma_divisibles}")