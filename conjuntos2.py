#Dos grupos de amigos tienen colecciones con sus géneros musicales favoritos. Se requiere determinar si ambos grupos comparten al menos un género (evaluar si las colecciones son disjuntas
# o no). Además, se debe presentar la intersección de géneros, la unión de ambos conjuntos y la diferencia simétrica (los géneros que no coinciden entre los grupos).

grupo_a = {"rock", "pop", "jazz"}
grupo_b = {"pop", "reggae", "electrónica"}


print(f"Preferencias Grupo A: {grupo_a}")
print(f"Preferencias Grupo B: {grupo_b}")
print()


tienen_comunes = not grupo_a.isdisjoint(grupo_b)
if tienen_comunes:
    print("¿Tienen géneros en común? Sí")
else:
    print("¿Tienen géneros en común? No")
generos_comunes = grupo_a.intersection(grupo_b)

print(f"Géneros comunes: {generos_comunes}")
todos_generos = grupo_a.union(grupo_b)

print(f"Unión de géneros: {todos_generos}")
generos_exclusivos = grupo_a.symmetric_difference(grupo_b)

print(f"Géneros exclusivos (diferencia simétrica): {generos_exclusivos}")