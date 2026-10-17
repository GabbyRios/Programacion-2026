import random

numero = random.randint(1, 5)

while True:
    intento = int(input("Adivina el número del 1 al 5: "))

    if intento == numero:
        print("¡Correcto! Ganaste.")
        break
    else:
        print("Intenta de nuevo.")