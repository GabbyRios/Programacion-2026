"""Microreto: ¿nos conviene la promoción?"""

# Entrada: datos del producto
producto = ["Cafe", 5000, 20]

nombre = producto[0]
precio_actual = producto[1]
unidades_actuales = producto[2]

# Proceso: calcular el descuento
descuento = precio_actual * 15 / 100
precio_promocional = precio_actual - descuento

# Calcular el ingreso actual
ingreso_actual = precio_actual * unidades_actuales

# Proyectar un aumento del 20% en las ventas
aumento_unidades = unidades_actuales * 20 / 100
unidades_proyectadas = unidades_actuales + aumento_unidades

# Calcular el ingreso con la promoción
ingreso_promocion = precio_promocional * unidades_proyectadas
diferencia = ingreso_promocion - ingreso_actual

# Decidir si conviene lanzar la promoción
if diferencia > 0:
    recomendacion = "lanzar"
else:
    recomendacion = "no lanzar"

# Salida: reporte completo
print(f"""ANÁLISIS DE PROMOCIÓN
Producto: {nombre}
Precio actual: ₡{precio_actual}
Unidades actuales: {unidades_actuales}
Ingreso actual: ₡{ingreso_actual}
Descuento: 15%
Precio promocional: ₡{precio_promocional}
Unidades proyectadas (supuesto +20%): {int(unidades_proyectadas)}
Ingreso con promoción: ₡{ingreso_promocion}
Diferencia: ₡{diferencia}
RECOMENDACIÓN: {recomendacion}.""")
