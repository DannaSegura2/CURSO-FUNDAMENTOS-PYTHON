def informe_alumnos():
    # Dos conjuntos de datos paralelos: nombres y calificaciones
    nombres = ["Danna Segura", "Nicol Amaya", "Erick Ladino", 
               "Jhon Medina", "David Rodríguez", "Sofía Torres"]
    calificaciones = [8.5, 7.2, 9.0, 6.8, 9.5, 8.0]
    
  
    print("=== INFORME DE CALIFICACIONES ===")
    print("Posición | Nombre             | Calificación")
    print("---------|--------------------|------------")
    
    for i in range(len(nombres)):
        print(f"{i+1:^6}| {nombres[i]:<19}| {calificaciones[i]:^12}")
    
   
    print("\n=== SISTEMA DE CONSULTA ===")
    print(f"Ingresa un número entre 1 y {len(nombres)} para consultar la calificación")
    print("Ingresa un valor fuera de rango para terminar")
    
    while True:
        try:
            posicion = int(input("\nIngresa la posición del alumno: "))
            
            # Verificar si la posición está dentro del rango válido
            if 1 <= posicion <= len(nombres):
                # Ajustamos la posición al índice (restando 1)
                indice = posicion - 1
                print(f"Alumno: {nombres[indice]}")
                print(f"Calificación: {calificaciones[indice]}")
            else:
                print("Posición fuera de rango. Finalizando consulta...")
                break
                
        except ValueError:
            print("Por favor, ingresa un número válido.")


if __name__ == "__main__":
    informe_alumnos()
    