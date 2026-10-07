#Solucion Mision Kit Seguro
#Autor: Gabriela Rios Rodriguez. Fecha: 2026/10/06

nombre = input("Nombre: ").strip().upper()
kit = input("Tipo de kit: ").strip().lower()
autorizacion = input("tiene autorizacion (si/no)?: ").lower() == "si"

try:
    cantidad = int(input("Ingrese la cantidad: "))
except ValueError:
    print("Error cantidad invalida, asignada -1")
    cantidad = -1
try:
    dias = int(input("Dias de prestamo: "))
except ValueError:
    print("Error cantidad dias invalida, asignada -1")
    dias = -1
    
resultado = ""
if not nombre or kit == "" or cantidad < 1 or dias < 1:
    resultado = "Registro rechazado: datos invalidos!"
elif autorizacion and cantidad <= 3 and not dias > 7: #not dias > 7 dias | dias <=7
    resultado = f"Solicitud aprobada para {nombre}: {cantidad} kit(s) de {kit}."

print(resultado)