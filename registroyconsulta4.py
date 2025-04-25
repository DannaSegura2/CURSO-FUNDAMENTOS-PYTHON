def mostrar_menu():
    print("\n Menú:")
    print("1. Agregar nuevo Estudiante")
    print("2. Listar todos los Estudiantes")
    print("3. Consultar calificación de un estudiante")
    print("4. Actualizar calificación de un estudiante")
    print("5. Eliminar un estudiante del registro")
    print("6. Salir")

registros = {
    "Sergio Prato": 95,
    "Chloe Sanchez": 77,
    "Guada Hernandez": 100,
    "Laura Baron": 65
}

for reg in registros:
  print(reg)

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if nombre in registros:
            print("El estudiante ya está registrado.")
        else:
            try:
                calificacion = float(input("Ingrese la calificación: "))
                registros[nombre] = calificacion
                print(f" Registro agregado: {nombre} - {calificacion}")
            except ValueError:
                print(" La calificación debe ser un número.")

    elif opcion == "2":
        if registros:
            print("\n Lista de calificaciones:")
            for nombre, calificacion in registros.items():
                print(f"- {nombre}: {calificacion}")
        else:
            print(" No hay registros disponibles.")

    elif opcion == "3":
        nombre = input("Ingrese el nombre del estudiante a consultar: ").strip()
        if nombre in registros:
            print(f" {nombre} tiene una calificación de {registros[nombre]}")
        else:
            print(" Estudiante no encontrado.")

    elif opcion == "4":
        nombre = input("Ingrese el nombre del estudiante que quiere actualizar: ").strip()
        if nombre in registros:
            try:
                nueva_calificacion = float(input(f"Ingrese la nueva calificación para {nombre}: "))
                registros[nombre] = nueva_calificacion
                print(f" Calificación actualizada: {nombre} - {nueva_calificacion}")
            except ValueError:
                print(" La calificación debe ser un número.")
        else:
            print("Estudiante no encontrado.")

    elif opcion == "5":
        nombre = input("Ingrese el nombre del estudiante que quiere eliminar: ").strip()
        if nombre in registros:
            del registros[nombre]
            print(f"{nombre} ha sido eliminado del registro.")
        else:
            print(" Estudiante no encontrado.")

    elif opcion == "6":
        print(" Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print(" Opción no válida. Intenta de nuevo.")