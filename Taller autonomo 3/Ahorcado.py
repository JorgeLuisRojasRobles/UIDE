import random

# Lista de palabras para el juego
diccionario = ["computadora", "aeropuerto", "ecuador", "programacion", "teclado", "internacional"]

# Selecciona una palabra aleatoria del diccionario
palabra_secreta = random.choice(diccionario)

# Inicializa la palabra adivinada con guiones bajos
palabra_adivinada = ["_"] * len(palabra_secreta)

# Contador de intentos incorrectos
intentos_incorrectos = 0

# Número máximo de intentos permitidos
max_intentos = 5

print("BIENVENIDO AL JUEGO DEL AHORCADO")

# Variable para verificar si el jugador ha ganado
ganaste = False 

# Bucle principal del juego
while intentos_incorrectos < max_intentos and not ganaste:

    # Muestra la palabra adivinada hasta el momento
    print("\nPalabra a adivinar:", " ".join(palabra_adivinada))
    
    # Solicita al jugador que ingrese una letra
    letra_ingresada = input("Ingrese una letra: ")
    
    # Verifica si la letra ingresada está en la palabra secreta
    if letra_ingresada in palabra_secreta:
        print("Letra correcta")
        
        # Actualiza la palabra adivinada con la letra correcta
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra_ingresada:
                palabra_adivinada[i] = letra_ingresada
    else:
        # Incrementa el contador de intentos incorrectos
        intentos_incorrectos += 1
        print("Letra incorrecta. Intentos restantes:", max_intentos - intentos_incorrectos)

    # Verifica si el jugador ha adivinado toda la palabra
    if "".join(palabra_adivinada) == palabra_secreta:
        ganaste = True

# Mensaje final del juego
if ganaste == True:
    print("\n¡Felicidades, usted ganó el juego!")
else:
    print("\nPerdió el juego, la palabra correcta era:", palabra_secreta)