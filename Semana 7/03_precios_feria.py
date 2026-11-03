"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

# Calcular promedio, mínimo, máximo y rango
promedio = sum(precios) / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo

# Contar precios que superan el promedio usando while
indice = 0
sobre_promedio = 0

while indice < len(precios):
    if precios[indice] > promedio:
        sobre_promedio += 1
    indice += 1

# Clasificar el rango
if rango >= 300:
    variacion = "alta"
elif rango >= 150:
    variacion = "moderada"
else:
    variacion = "baja"

# Mostrar resultados
print("Producto:", producto)
print("Promedio: ₡", promedio)
print("Mínimo: ₡", minimo)
print("Máximo: ₡", maximo)
print("Rango: ₡", rango)
print("Precios sobre el promedio:", sobre_promedio)
print("Variación:", variacion)

# Prueba temporal: cinco precios iguales
precios = [1000, 1000, 1000, 1000, 1000]

promedio = sum(precios) / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo

indice = 0
sobre_promedio = 0

while indice < len(precios):
    if precios[indice] > promedio:
        sobre_promedio += 1
    indice += 1

print("\nPrueba con precios iguales:")
print("Rango: ₡", rango)
print("Precios sobre el promedio:", sobre_promedio)

# Restaurar la lista original
precios = [900, 850, 1000, 950, 1200]
