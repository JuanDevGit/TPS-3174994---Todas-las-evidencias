# Ejercicio 9: Ver si un número aparece más veces que el mayor
import random
lista = [random.randint(0, 100) for _ in range(20)]
print("Lista:", lista)
num = int(input("Ingrese un número: "))
mayor = max(lista)
print(lista.count(num) > lista.count(mayor))
