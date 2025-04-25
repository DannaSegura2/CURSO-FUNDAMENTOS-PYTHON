frase = input("Ingrese una frase: ")

palabras_procesadas = tuple("".join(c for c in palabra if c.isalpha()) for palabra in frase.split())

palabras_ordenadas = tuple(sorted(palabras_procesadas))

print("Palabras procesadas y ordenadas:", palabras_ordenadas)

frase_limpia = ""

for caracter in frase:
    if caracter.isalpha() or caracter == " ":
        frase_limpia += caracter

print("Texto limpio:", frase_limpia)
