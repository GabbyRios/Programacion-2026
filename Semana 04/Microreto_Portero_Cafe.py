"""Microreto: el portero del café."""

energia = int(input("Cuanta energia tienes de 0-100: "))
trae_cafe = input("¿Traes café? (si/no): ").lower().strip() == "si"

mensaje = "Completa las reglas del portero."

# < 30 energia y no traigo cafe
# Si traigo 30 de energia y tengo cafe (Dejeme pasar)
# Portero confundido, revise las respuestas
# TODO: usa and para detectar energía baja sin café.
if energia < 30 and not (trae_cafe):
    mensaje = "Acceso denegado: necesitas dormir o tomar cafe."   
# TODO: usa or para permitir energía suficiente o café.
elif energia >= 30 or trae_cafe:
    mensaje = "Acceso permitido: pasa, pero comparte cafe."
# TODO: escribe mensajes claros para cada resultado.
else:
    mensaje = "El guarda esta confundido, revisa las respuestas."
    
print(mensaje)