"""Semana 8: la red hospitalaria nos contrata como analistas de datos.

Construimos el informe debajo de este inicio con GUIA_ESTUDIANTE.md.
Leemos la fuente preparada en fuente.py y contamos las menciones recibidas.
"""

from fuente import cargar_datos

USAR_RESPALDO = False  # Lo cambiamos solo si recibimos copias actualizadas.

registros, equivalencias, origen = cargar_datos(USAR_RESPALDO)

print("Fuente:", origen)
print("Registros recibidos:", len(registros))
print("Equivalencias publicadas:", len(equivalencias))

print("\nDATOS DE PACIENTES")

for registro in registros:
    print("Cédula:", registro["paciente_cedula"])
    print("Nombre:", registro["paciente_nombre"])
    print("Diagnóstico:", registro["diagnostico"])
    print("Medicamentos:", ", ".join(registro["medicamentos"]))
    print("-" * 40)
    #conteo
    for medicamento in registro["medicamentos"]:
        print(medicamento)