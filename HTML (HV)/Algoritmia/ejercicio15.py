# Ejercicio 15: Saber si un año es bisiesto
año = int(input("Ingrese el año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")
