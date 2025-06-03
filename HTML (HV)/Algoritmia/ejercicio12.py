# Ejercicio 12: Crear una lista inversa a la dada
import random
lista = [random.randint(0, 100) for _ in range(20)]
print("Lista original:", lista)
inversa = lista[::-1]
print("Lista invertida:", inversa)
