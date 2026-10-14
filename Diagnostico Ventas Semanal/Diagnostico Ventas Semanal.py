"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 640000
meta_norte = 700000

# TODO: calcula total, cantidad, mayor y menor para Centro.
total_centro = sum(ventas_centro) # Total de ventas semanal
cantidad_centro = len(ventas_centro) # Catidad de días registrados

promedio_centro = total_centro / cantidad_centro # Promedio ventas diario
menor_centro = min(ventas_centro) #venta minima de la tienda del Centro
mayor_centro = max(ventas_centro) #venta maxima de la tienda del Centro

porcentaje_centro = (total_centro * 100 / meta_centro)

#TODO: decide si cada tienda supero, igualo o no alcanzo su meta
if total_centro > meta_centro:
    estado_centro = "meta superada"
elif total_centro == meta_centro:
    estado_centro = "meta alcanzada exactamente"
else:
    estado_centro = "meta NO alcanzada"
