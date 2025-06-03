# Ejercicio 11: Calcular la media entre el mayor y el menor de la lista
import random
lista = [random.randint(0, 100) for _ in range(20)]
print("Lista:", lista)
media = (max(lista) + min(lista)) / 2
print("Media entre mayor y menor:", media)
