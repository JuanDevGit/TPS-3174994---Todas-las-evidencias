# Ejercicio 6: Buscar un número en una lista de 20 números aleatorios
import random
lista = [random.randint(0, 100) for _ in range(20)]
print("Lista:", lista)
num = int(input("Ingrese un número a buscar: "))
if num in lista:
    print("Número encontrado en la posición:", lista.index(num))
else:
    print("Número no encontrado")
