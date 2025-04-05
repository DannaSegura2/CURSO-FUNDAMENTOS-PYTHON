# Desarrolla un traductor sencillo que utilice un diccionario donde las claves sean palabras en español
# y los valores sus traducciones en inglés. El usuario ingresará una palabra en español; si la palabra se encuentra 
# en el diccionario, se mostrará su traducción. En caso contrario, se le solicitará al usuario que proporcione la traducción, la cual se agregará al diccionario. El proceso 
# se repetirá hasta que el usuario decida finalizar la consulta.

diccionario = {
    "hola": "hello",
    "mundo": "world",
    "casa": "house",
    "sol": "sun"
}

print(f"Diccionario inicial: {diccionario}")
print()


while True:
    palabra = input("Ingrese una palabra en español: ")
    
   
    if palabra.lower() == "salir":
        print("Terminando el programa.")
        break
    
   
    if palabra in diccionario :
        print(f"La traducción de '{palabra}' es: {diccionario[palabra]}")
    else:
        print(f"La palabra '{palabra}' no se encuentra en el diccionario.")
        traduccion = input(f"Ingrese la traducción de '{palabra}': ")
        
       
        diccionario[palabra] = traduccion
        print(f"Nueva entrada agregada: '{palabra}': '{traduccion}'")
    
    print() 
    