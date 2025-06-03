# Ejercicio 18: Letra de control del NIT
tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
nit = int(input("Ingrese el NIT: "))
resto = nit % 23
print("Letra de control:", tabla[resto])
