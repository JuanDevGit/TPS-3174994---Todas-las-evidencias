# Ejercicio 2: Calcular la suma 1 + 2 + ... + N
n = int(input("Ingrese un número: "))
suma = 0
for i in range(1, n + 1):      # el último 1 es para que el número n, el que ingreso el usuario, si se sume a la suma, sino, solo llegaria al numero anterior.
    suma += i
print("La suma es:", suma)
