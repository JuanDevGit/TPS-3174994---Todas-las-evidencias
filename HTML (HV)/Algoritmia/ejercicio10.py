# Ejercicio 10: Calcular la media de todos los números de la lista
import random
lista = [random.randint(0, 100) for _ in range(20)]
print("Lista:", lista)
media = sum(lista) / len(lista)
print("Media:", media)
