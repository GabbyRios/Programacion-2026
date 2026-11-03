
"""Caso 2: asistencia por bloques. """

# Datos iniciales
asistencias = [120, 180, 210, 250, 230]
capacidad = 300

# Inicializar acumulador y contador
total = 0
bloques = 0

# Recorrer las asistencias
for asistencia in asistencias:
    total += asistencia

    if asistencia > capacidad * 0.70:
        bloques += 1

# Calcular promedio y porcentaje de ocupación
promedio = total / len(asistencias)
porcentaje = (promedio / capacidad) * 100

# Clasificar el promedio
if porcentaje >= 80:
    estado = "Ocupación alta"
elif porcentaje >= 50:
    estado = "Ocupación media"
else:
    estado = "Ocupación baja"

# Mostrar resultados
print("Total de asistentes:", total)
print("Promedio por bloque:", promedio)
print("Porcentaje de ocupación:", porcentaje, "%")
print("Cantidad de bloques que superan el 70 %:", bloques)
print("Estado:", estado)