def evaluar_pieza(estandares):
    """
    Evalúa una pieza basada en los estándares de calidad cumplidos.
    
    Args:
        estandares (str): Cadena binaria donde '1' representa estándar cumplido
                        y '0' representa estándar no cumplido.
    
    Returns:
        tuple: (aprobada, estandares_fallidos) donde:
               - aprobada es un booleano (True si todos los estándares se cumplen)
               - estandares_fallidos es una lista de índices donde fallaron los estándares
    """
    estandares_fallidos = []
    
    for i, valor in enumerate(estandares):
        if valor == '0':
            estandares_fallidos.append(i + 1)  # +1 para que el índice empiece en 1
    
    return len(estandares_fallidos) == 0, estandares_fallidos

def main():
    print("SISTEMA DE CONTROL DE CALIDAD")
    print("=============================")
    
    try:
        estandares = input("Ingrese los estándares de calidad (cadena binaria de 1s y 0s): ")
        
        # Validar que la entrada sea binaria
        if not all(bit in '01' for bit in estandares):
            print("Error: La entrada debe ser una cadena binaria (solo 0s y 1s).")
            return
        
        if len(estandares) == 0:
            print("Error: Debe ingresar al menos un estándar de calidad.")
            return
        
        # Evaluar la pieza
        aprobada, estandares_fallidos = evaluar_pieza(estandares)
        
        # Mostrar resultados
        print("\nRESULTADO DE LA INSPECCIÓN:")
        print(f"Estándares evaluados: {len(estandares)}")
        
        if aprobada:
            print("Estado: APROBADA ✓")
            print("Todos los estándares de calidad han sido cumplidos.")
            print("La pieza puede continuar en la línea de producción.")
        else:
            print("Estado: RECHAZADA ✗")
            print("Se encontraron los siguientes problemas:")
            for estandar in estandares_fallidos:
                print(f"  - Estándar #{estandar} no cumplido")
            print("\n¡ALERTA! Se requiere intervención del operador.")
        
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()