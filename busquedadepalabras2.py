parrafo_1 = input("ingrese el parrafo 1: ").lower()

palabra_repetida = input("Ingrese la palabra que desea buscar: ")
numero_de_veces = parrafo_1.count(palabra_repetida)
print(f"La palabra '{palabra_repetida}' aparece {numero_de_veces} veces en el párrafo.")
