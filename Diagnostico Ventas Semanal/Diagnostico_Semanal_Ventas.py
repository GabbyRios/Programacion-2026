
"""Análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]

meta_centro = 640000
meta_norte = 700000

# Tienda Centro
total_centro = sum(ventas_centro)
cantidad_centro = len(ventas_centro)
mayor_centro = max(ventas_centro)
menor_centro = min(ventas_centro)

promedio_centro = total_centro / cantidad_centro
rango_centro = mayor_centro - menor_centro
diferencia_centro = total_centro - meta_centro
porcentaje_centro = total_centro * 100 / meta_centro

# Estado de la meta de Centro
if total_centro > meta_centro:
    estado_centro = "Superó la meta"
elif total_centro == meta_centro:
    estado_centro = "Igualó la meta"
else:
    estado_centro = "No alcanzó la meta"

# Tienda Norte
total_norte = sum(ventas_norte)
cantidad_norte = len(ventas_norte)
mayor_norte = max(ventas_norte)
menor_norte = min(ventas_norte)

promedio_norte = total_norte / cantidad_norte
rango_norte = mayor_norte - menor_norte
diferencia_norte = total_norte - meta_norte
porcentaje_norte = total_norte * 100 / meta_norte

# Estado de la meta de Norte
if total_norte > meta_norte:
    estado_norte = "Superó la meta"
elif total_norte == meta_norte:
    estado_norte = "Igualó la meta"
else:
    estado_norte = "No alcanzó la meta"

# Comparación de totales y rangos
diferencia_totales = abs(total_centro - total_norte)

if total_centro > total_norte:
    tienda_mayor_total = "Centro"
elif total_norte > total_centro:
    tienda_mayor_total = "Norte"
else:
    tienda_mayor_total = "Ambas tiendas empataron"

if rango_centro > rango_norte:
    tienda_mayor_rango = "Centro"
elif rango_norte > rango_centro:
    tienda_mayor_rango = "Norte"
else:
    tienda_mayor_rango = "Ambas tiendas tienen el mismo rango"

# Reporte de resultados
print("===== REPORTE DE VENTAS =====")

print("\nTIENDA CENTRO")
print(f"Total semanal: ₡{total_centro:,.0f}")
print(f"Cantidad de registros: {cantidad_centro}")
print(f"Venta mayor: ₡{mayor_centro:,.0f}")
print(f"Venta menor: ₡{menor_centro:,.0f}")
print(f"Promedio diario: ₡{promedio_centro:,.2f}")
print(f"Rango de ventas: ₡{rango_centro:,.0f}")
print(f"Diferencia respecto a la meta: ₡{diferencia_centro:,.0f}")
print(f"Cumplimiento de la meta: {porcentaje_centro:.2f}%")
print(f"Estado: {estado_centro}")

print("\nTIENDA NORTE")
print(f"Total semanal: ₡{total_norte:,.0f}")
print(f"Cantidad de registros: {cantidad_norte}")
print(f"Venta mayor: ₡{mayor_norte:,.0f}")
print(f"Venta menor: ₡{menor_norte:,.0f}")
print(f"Promedio diario: ₡{promedio_norte:,.2f}")
print(f"Rango de ventas: ₡{rango_norte:,.0f}")
print(f"Diferencia respecto a la meta: ₡{diferencia_norte:,.0f}")
print(f"Cumplimiento de la meta: {porcentaje_norte:.2f}%")
print(f"Estado: {estado_norte}")

print("\nCOMPARACIÓN")
print(f"Tienda con mayor total: {tienda_mayor_total}")
print(f"Diferencia entre los totales: ₡{diferencia_totales:,.0f}")
print(f"Tienda con mayor rango: {tienda_mayor_rango}")

# Tres conclusiones
print("\nCONCLUSIONES")
print("1. La tienda Norte obtuvo un total semanal mayor que Centro.")
print("2. Centro tuvo un rango de ventas mayor, por lo que sus ventas variaron más.")
print("3. Centro no alcanzó su meta, mientras que Norte la superó.")

print(f"centro total: ₡{total_centro:,.0f}")
print(f"Centro logro: {porcentaje_centro:.2f}%")
print(f"norte total: ₡{total_norte:,.0f}")
print(f"Norte logro: {porcentaje_norte:.2f}%")

