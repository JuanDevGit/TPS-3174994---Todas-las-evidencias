# Ejercicio 5: Mostrar cinco números ordenados de mayor a menor
numeros = []
for i in range(5):
    n = int(input("Ingrese un número: "))
    numeros.append(n)
numeros.sort()
numeros = numeros[::-1]
print("Orden descendente:", numeros)
