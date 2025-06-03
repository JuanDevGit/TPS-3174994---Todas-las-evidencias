# Ejercicio 13: Menú con opciones de los ejercicios 6 al 12
import random
lista = [random.randint(0, 100) for _ in range(20)]
while True:
    print("\nMenú:")
    print("1. Buscar número")
    print("2. Contar repeticiones")
    print("3. Mayor y repeticiones")
    print("4. Ver si número aparece más que el mayor")
    print("5. Media total")
    print("6. Media entre mayor y menor")
    print("7. Invertir lista")
    print("8. Salir")
    op = input("Opción: ")

    if op == "1":
        n = int(input("Número: "))
        if n in lista:
            print("Posición:", lista.index(n))
        else:
            print("No encontrado")
    elif op == "2":
        n = int(input("Número: "))
        print("Aparece", lista.count(n), "veces")
    elif op == "3":
        m = max(lista)
        print("Mayor:", m, "- Aparece", lista.count(m), "veces")
    elif op == "4":
        n = int(input("Número: "))
        print(lista.count(n) > lista.count(max(lista)))
    elif op == "5":
        print("Media:", sum(lista) / len(lista))
    elif op == "6":
        print("Media entre mayor y menor:", (max(lista) + min(lista)) / 2)
    elif op == "7":
        print("Lista invertida:", lista[::-1])
    elif op == "8":
        break
