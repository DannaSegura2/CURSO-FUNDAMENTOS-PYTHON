lista_de_numeros = [15, 20, 25, 30, 35]
print(lista_de_numeros)
while True:
    print("\n1. Promedio")
    print("2. Máximo")
    print("3. Mínimo")
    print("4. Eliminar un número")
    print("5. Ver lista")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        if lista_de_numeros:
            promedio = sum(lista_de_numeros) / len(lista_de_numeros)
            print("Promedio:", promedio)
        else:
            print("La lista está vacía. No se puede calcular el promedio.")

    elif opcion == "2":
        if lista_de_numeros:
            print("Máximo:", max(lista_de_numeros))
        else:
            print("La lista está vacía.")

    elif opcion == "3":
        if lista_de_numeros:
            print("Mínimo:", min(lista_de_numeros))
        else:
            print("La lista está vacía.")

    elif opcion == "4":
        if lista_de_numeros:
            valor = int(input("Número a eliminar: "))
            if valor in lista_de_numeros:
                lista_de_numeros.remove(valor)
                print("Número eliminado.")
            else:
                print("Ese número no está en la lista.")
        else:
            print("La lista está vacía. No hay nada que eliminar.")

    elif opcion == "5":
        print("Lista actual:", lista_de_numeros)

    elif opcion == "6":
        print("Adiós")
        break

    else:
        print("Opción no válida.")