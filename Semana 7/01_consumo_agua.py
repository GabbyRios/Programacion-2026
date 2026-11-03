
"""Caso 1: cambio del consumo diario de agua."""

consumos_litros = [120, 115, 108, 102, 96]

# Calcular consumo total y promedio diario
total = sum(consumos_litros)
promedio = total / len(consumos_litros)

# Comparar primer día con último día
ahorro = consumos_litros[0] - consumos_litros[-1]
porcentaje = (ahorro / consumos_litros[0]) * 100

# Clasificar la reducción
if porcentaje >= 15:
    clasificacion = "Reducción alta"
elif porcentaje > 0:
    clasificacion = "Reducción moderada"
else:
    clasificacion = "Sin reducción"

# Mostrar los cinco resultados
print("Consumo total:", total, "L")
print("Promedio diario:", promedio, "L")
print("Litros ahorrados:", ahorro, "L")
print("Porcentaje de reducción:", porcentaje, "%")
print("Clasificación:", clasificacion)