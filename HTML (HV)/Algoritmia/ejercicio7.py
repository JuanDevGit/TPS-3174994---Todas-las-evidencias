# Ejercicio 7: Contar cuántas veces aparece un número en la lista
import random
lista = [random.randint(0, 100) for _ in range(20)]
print("Lista:", lista)
num = int(input("Ingrese un número a buscar: "))
print("Aparece", lista.count(num), "veces")
