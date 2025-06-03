# Ejercicio 20: Cuota de una hipoteca
C = float(input("Capital: "))
interes_anual = float(input("Interés anual: "))
años = int(input("Años: "))
R = interes_anual / 100 / 12
N = años * 12
cuota = C * R / (1 - (1 + R) ** -N)
print("Cuota mensual:", cuota)
