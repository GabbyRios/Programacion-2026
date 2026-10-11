# ENTRADA
try:
    total_cuenta = float(input("Ingrese el total de la cuenta: "))
    porcentaje = float(input("Ingrese el porcentaje de propina: "))
    
        # PROCESO
    if total_cuenta < 0 or porcentaje < 0:
        print("Error: los valores no pueden ser negativos.")
    else:
        propina = total_cuenta * porcentaje / 100
        total_final = total_cuenta + propina

        # SALIDA
        print(f"Propina: {propina:.2f}")
        print(f"Total final a pagar: {total_final:.2f}")

except ValueError:
    print("Error: debe ingresar valores numéricos.")