def gestionar_actividades():
    # Lista inicial de actividades con su estado 
    actividades = [
        {"nombre": "Ejercicio matutino", "completada": True},
        {"nombre": "Revisar correos", "completada": False},
        {"nombre": "Reunión de equipo", "completada": True},
        {"nombre": "Trabajar en proyecto", "completada": False},
        {"nombre": "Almuerzo", "completada": True},
        {"nombre": "Llamadas pendientes", "completada": False},
        {"nombre": "Actualizar documentación", "completada": True},
        {"nombre": "Revisar tareas del día siguiente", "completada": False}
    ]
    
    # Mostrar estado inicial con posiciones
    print("=== ESTADO INICIAL DE ACTIVIDADES ===")
    for i, actividad in enumerate(actividades, 1):
        estado = "✓" if actividad["completada"] else "✗"
        print(f"{i}. {actividad['nombre']} [{estado}]")
    
    # Filtrar actividades completadas
    actividades_completadas = [act for act in actividades if act["completada"]]
    
    # Filtrar actividades pendientes para actualizar la lista
    actividades_pendientes = [act for act in actividades if not act["completada"]]
    
    # Mostrar actividades completadas
    print("\n=== ACTIVIDADES COMPLETADAS ===")
    for i, actividad in enumerate(actividades_completadas, 1):
        print(f"{i}. {actividad['nombre']}")
    
    # Actualizar conjunto de actividades (quedarnos solo con las pendientes)
    actividades = actividades_pendientes
    
    # Estado final después del filtrado
    print("\n=== ESTADO FINAL (ACTIVIDADES PENDIENTES) ===")
    for i, actividad in enumerate(actividades, 1):
        print(f"{i}. {actividad['nombre']} [✗]")
    

    print(f"\nResumen: {len(actividades_completadas)} actividades completadas y {len(actividades)} pendientes")


if __name__ == "__main__":
    gestionar_actividades()