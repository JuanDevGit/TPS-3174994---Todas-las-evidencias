# Ejercicio 8: Buscar el número mayor y cuántas veces aparece
import random
lista = [random.randint(0, 100) for _ in range(20)]
print("Lista:", lista)
mayor = max(lista)
print("Número mayor:", mayor)
print("Aparece", lista.count(mayor), "veces")
