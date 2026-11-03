"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Acumuladores y estructuras
total_minutos = 0

conteo_categorias = {
    "Acceso": 0,
    "Equipo": 0,
    "Red": 0
}

pendientes = 0
provincias_pendientes = set()
casos_urgentes = []

# (id, minutos)
caso_mas_largo = ("", 0)

# Recorrido único
for incidencia in incidencias:
    total_minutos += incidencia["minutos_atencion"]

    categoria = incidencia["categoria"]
    conteo_categorias[categoria] += 1

    # Actualizar caso más largo
    if incidencia["minutos_atencion"] > caso_mas_largo[1]:
        caso_mas_largo = (
            incidencia["id"],
            incidencia["minutos_atencion"]
        )

    # Casos pendientes
    if not incidencia["resuelto"]:
        pendientes += 1
        provincias_pendientes.add(incidencia["provincia"])

        if incidencia["minutos_atencion"] >= 60:
            casos_urgentes.append(
                (
                    incidencia["id"],
                    incidencia["minutos_atencion"]
                )
            )

# Promedio
promedio_minutos = total_minutos / len(incidencias)

# Resultados
print("Total de casos:", len(incidencias))
print("Total de minutos:", total_minutos)
print("Promedio de minutos:", promedio_minutos)

print("\nConteo por categoría:")
print(conteo_categorias)

print("\nPendientes:", pendientes)

print("\nProvincias con pendientes:")
print(provincias_pendientes)

print("\nCasos urgentes:")
print(casos_urgentes)

print("\nCaso más largo:")
print(caso_mas_largo)

print("\n¿Hay pendientes en San Jose?")
print("San Jose" in provincias_pendientes)
