def calcular_calificacion_final():
    # Lectura de calificaciones parciales
    parcial1 = float(input("Ingrese calificación del primer parcial: "))
    parcial2 = float(input("Ingrese calificación del segundo parcial: "))
    parcial3 = float(input("Ingrese calificación del tercer parcial: "))
    
    # Lectura de examen final y trabajo final
    examen_final = float(input("Ingrese calificación del examen final: "))
    trabajo_final = float(input("Ingrese calificación del trabajo final: "))
    
    # Cálculo del promedio de parciales
    promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
    
    # Cálculo de la calificación final según los porcentajes
    calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
    
    return calificacion_final

# Ejecución del programa
try:
    resultado = calcular_calificacion_final()
    print(f"\nLa calificación final en Matemáticas es: {resultado:.2f}")
except ValueError:
    print("Error: Por favor ingrese solo valores numéricos para las calificaciones.")

if __name__ == "__main__":
    pass
