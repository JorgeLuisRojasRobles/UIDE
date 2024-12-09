import random
diccionario = ["computadora", "aeropuerto", "ecuador", "programacion", "teclado", "internacional"]
palabra_secreta = random.choice(diccionario)
palabra_adivinada = ["_"] * len(palabra_secreta)
intentos_incorrectos = 0
max_intentos = 5
print("BIENVENIDO AL JUEGO DEL AHORCADO")
ganaste = False 
while intentos_incorrectos < max_intentos and not ganaste:

    print("\nPalabra a adivinar:", " ".join(palabra_adivinada))
    letra_ingresada = input("Ingrese una letra: ")
    if letra_ingresada in palabra_secreta:
        print("Letra correcta")
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra_ingresada:
                palabra_adivinada[i] = letra_ingresada
    else:
        intentos_incorrectos += 1
        print("Letra incorrecta. Intentos restantes:", max_intentos - intentos_incorrectos)

    if "".join(palabra_adivinada) == palabra_secreta:
        ganaste = True
if ganaste == True:
    print("\n¡Felicidades, usted ganó el juego!")
else:
    print("\nPerdió el juego, la palabra correcta era:", palabra_secreta)
