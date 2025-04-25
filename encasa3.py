def filtrar_letras():
    # Solicitar entrada al usuario
    texto = input("Por favor, introduce una secuencia de caracteres: ")
    
    # Descomponer el texto en caracteres individuales
    caracteres = list(texto)
    
    # Mostrar la descomposición
    print("\nDescomposición del texto:")
    for i, caracter in enumerate(caracteres):
        print(f"Posición {i}: '{caracter}'")
        solo_letras = [char for char in caracteres if char.isalpha()]
    
    # Convertir la colección resultante en una estructura inmutable (tupla)
    resultado_inmutable = tuple(solo_letras)
    
    # Mostrar los resultados
    print("\nCaracteres filtrados (solo letras):")
    print(f"Total de caracteres originales: {len(caracteres)}")
    print(f"Total de letras filtradas: {len(solo_letras)}")
    print("\nResultado final (estructura inmutable):")
    print(resultado_inmutable)
    
    # Mostrar como texto concatenado
    texto_final = ''.join(resultado_inmutable)
    print(f"\nTexto filtrado: '{texto_final}'")

if __name__ == "__main__":
    filtrar_letras()