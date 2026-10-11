# ENTRADA
edad = int(input("Ingrese su edad: "))

# PROCESO
if edad < 13:
    categoria = "niño"
elif edad < 18:
    categoria = "adolescente"
elif edad < 65:
    categoria = "adulto"
else:
    categoria = "adulto mayor"

# SALIDA
print(f"Usted es: {categoria}.")