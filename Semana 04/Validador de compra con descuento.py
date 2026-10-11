# ENTRADA
nombre = input("Ingrese el nombre del cliente: ")
monto = float(input("Ingrese el monto de la compra: ₡"))
frecuente = input("¿Es cliente frecuente? (si/no): ").strip().lower()

# PROCESO
if frecuente == "si" and monto >= 20000:
    descuento = monto * 0.10
else:
    descuento = 0

total = monto - descuento

# SALIDA
print(f"\nCliente: {nombre}")
print(f"Monto original: ₡{monto:.2f}")
print(f"Descuento: ₡{descuento:.2f}")
print(f"Total a pagar: ₡{total:.2f}")