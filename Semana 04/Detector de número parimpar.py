# ENTRADA
numero = int(input("Ingrese un número entero: "))

# PROCESO
if numero % 2 == 0:
    resultado = "par"
else:
    resultado = "impar"

# SALIDA
print(f"El número {numero} es {resultado}.")