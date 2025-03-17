def calcular_descuento(estrato, edad, valor_matricula):
    """
    Calcula el descuento y el valor final de la matrícula según el estrato y la edad.
    
    Reglas de descuento:
    - Estrato 1, edad < 18: 20% de descuento
    - Estrato 1, edad >= 18: 15% de descuento
    - Estrato 2, edad < 18: 10% de descuento
    - Estrato 2, edad >= 18: 5% de descuento
    
    Args:
        estrato (int): Estrato del estudiante (1 o 2)
        edad (int): Edad del estudiante
        valor_matricula (float): Valor original de la matrícula
        
    Returns:
        tuple: (valor_descuento, valor_final_matricula)
    """
    porcentaje_descuento = 0
    
    if estrato == 1:
        if edad < 18:
            porcentaje_descuento = 20
        else:  # edad >= 18
            porcentaje_descuento = 15
    elif estrato == 2:
        if edad < 18:
            porcentaje_descuento = 10
        else:  # edad >= 18
            porcentaje_descuento = 5
    
    valor_descuento = (porcentaje_descuento / 100) * valor_matricula
    valor_final = valor_matricula - valor_descuento
    
    return valor_descuento, valor_final

def main():
    print("CÁLCULO DE MATRÍCULA UNIVERSITARIA")
    print("==================================")
    
    try:
        valor_matricula = float(input("Ingrese el valor de la matrícula: $"))
        estrato = int(input("Ingrese el estrato del estudiante (1 o 2): "))
        edad = int(input("Ingrese la edad del estudiante: "))
        
        # Validación de datos
        if estrato not in [1, 2]:
            print("Error: El estrato debe ser 1 o 2.")
            return
        
        if edad <= 0 or edad > 100:
            print("Error: La edad debe ser un valor válido.")
            return
        
        if valor_matricula <= 0:
            print("Error: El valor de la matrícula debe ser mayor que cero.")
            return
        
        # Cálculo del descuento y valor final
        valor_descuento, valor_final = calcular_descuento(estrato, edad, valor_matricula)
        
        # Mostrar resultados
        print("\nRESULTADOS:")
        print(f"Valor original de la matrícula: ${valor_matricula:,.2f}")
        print(f"Valor del descuento: ${valor_descuento:,.2f}")
        print(f"Valor final a pagar: ${valor_final:,.2f}")
        
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()