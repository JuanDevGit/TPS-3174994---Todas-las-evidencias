# Ejercicio 14: Contar palabras y tamaño de la más larga
texto = input("Ingrese un texto: ")
palabras = texto.split()
mayor = 0
for palabra in palabras:
    if len(palabra) > mayor:
        mayor = len(palabra)
print("Palabras:", len(palabras))
print("Tamaño de la palabra más larga:", mayor)
