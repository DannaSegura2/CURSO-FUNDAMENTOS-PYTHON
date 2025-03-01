def calcular_indice_cosecha(frutos_recolectados, frutos_producidos):
    """
    Calcula el índice de cosecha de un cultivo.
    
    Parámetros:
    frutos_recolectados (float): Cantidad de frutos recolectados
    frutos_producidos (float): Cantidad total de frutos producidos
    
    Retorna:
    float: Índice de cosecha expresado como porcentaje
    """
    if frutos_producidos <= 0:
        return 0
        
    indice = (frutos_recolectados / frutos_producidos) * 100
    return indice

def main():
    try:
        frutos_recolectados = float(input("Ingrese la cantidad de frutos recolectados: "))
        frutos_producidos = float(input("Ingrese la cantidad total de frutos producidos: "))
        
        if frutos_recolectados < 0 or frutos_producidos < 0:
            print("Error: Las cantidades no pueden ser negativas.")
            return
            
        if frutos_recolectados > frutos_producidos:
            print("Advertencia: La cantidad de frutos recolectados no puede ser mayor que la cantidad producida.")
            return
            
        indice_cosecha = calcular_indice_cosecha(frutos_recolectados, frutos_producidos)
        print(f"El índice de cosecha es: {indice_cosecha:.2f}%")
        
        def calcular_indice_cosecha(frutos_recolectados, frutos_producidos):
            
             print(f"El índice de cosecha es: {indice_cosecha:.2f}%")
        
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
            
       
