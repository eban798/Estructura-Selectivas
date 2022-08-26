print("Complement10 cuantas veces se repite " "a")

ca=0

numCar = 10
print("Ingrese", numCar, "caracteres: ")

for i in range(0, numCar):
 m = input("Ingrese Caracter: ")
if m == "a" :
 ca = ca + 1
#Salida
print("\nSALIDA: ")

print ("En", numCar, "caracteres hay", ca, "caracteres 'a'")
