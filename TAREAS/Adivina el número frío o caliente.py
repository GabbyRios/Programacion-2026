import random

secreto = random.randint(1, 20)
intentos = 0

while True:
    numero = int(input("Adivina el número del 1 al 20: "))
    intentos = intentos + 1

    if numero == secreto:
        print("Correcto. Adivinaste en", intentos, "intentos.")
        break
    else:
        if secreto > numero:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

        distancia = abs(numero - secreto)

        if distancia <= 2:
            print("Pista: hirviendo.")
        elif distancia <= 5:
            print("Pista: caliente.")
        elif distancia <= 10:
            print("Pista: tibio.")