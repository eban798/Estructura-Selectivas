print("Ejercicio13: VERIFICAR SI EL AÑO ES BISIESTO.")

anio = int( input("Ingrese año: "))

print("\nSALIDA: ")

if (anio % 400 == 0) or (anio % 4 == 0) and (anio % 100 != 0):
 print("El año es BISIESTO")
else:
 print("El año NO es BISIESTO")
