print("Ejercicio12: SUELDO A PERCIBIR")

SUE = float( input("Ingrese Sueldo: "))

if SUE < 1000:
 AUM = SUE*0.15
SUE = SUE + AUM

print("\nSALIDA: ")

print("El sueldo es:", SUE)