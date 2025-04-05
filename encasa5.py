def aplicacion_numeros():
    
    numeros = [34, 12, 89, 45, 23, 67, 9, 51, 78]
    continuar = True
    
    # Función para mostrar el estado actual de la colección
    def mostrar_coleccion():
        print("\nColección actual:", numeros)
        print(f"Cantidad de elementos: {len(numeros)}")
    
    # Función para calcular la suma total
    def calcular_suma():
        suma = sum(numeros)
        print(f"\nLa suma total de los valores es: {suma}")
    
    # Función para reordenar los valores
    def reordenar_valores():
        print("\n=== OPCIONES DE ORDENAMIENTO ===")
        print("1. Ordenar de menor a mayor")
        print("2. Ordenar de mayor a menor")
        
        opcion = input("Selecciona una opción (1-2): ")
        
        if opcion == "1":
            numeros.sort()
            print("\nColección ordenada de menor a mayor")
        elif opcion == "2":
            numeros.sort(reverse=True)
            print("\nColección ordenada de mayor a menor")
        else:
            print("\nOpción no válida. No se realizó ningún ordenamiento.")
    
    # Función para eliminar un valor
    def eliminar_valor():
        mostrar_coleccion()
        try:
            indice = int(input("\nIngresa la posición del valor a eliminar (1-" + str(len(numeros)) + "): "))
            
            if 1 <= indice <= len(numeros):
                valor_eliminado = numeros.pop(indice-1)
                print(f"\nSe ha eliminado el valor {valor_eliminado} en la posición {indice}")
            else:
                print("\nPosición fuera de rango. No se eliminó ningún valor.")
        except ValueError:
            print("\nDebe ingresar un número válido.")
    
    # Menú principal
    while continuar:
        print("\n" + "="*40)
        print("=== OPERACIONES CON VALORES NUMÉRICOS ===")
        print("="*40)
        
        mostrar_coleccion()
        
        print("\nMENÚ DE OPCIONES:")
        print("1. Calcular suma total")
        print("2. Reordenar valores")
        print("3. Eliminar un valor")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opción (1-4): ")
        
        if opcion == "1":
            calcular_suma()
        elif opcion == "2":
            reordenar_valores()
            mostrar_coleccion()
        elif opcion == "3":
            eliminar_valor()
        elif opcion == "4":
            print("\nFinalizando aplicación. ¡Hasta pronto!")
            continuar = False
        else:
            print("\nOpción no válida. Por favor, intenta nuevamente.")

# Ejecutar la aplicación
if __name__ == "__main__":
    aplicacion_numeros()