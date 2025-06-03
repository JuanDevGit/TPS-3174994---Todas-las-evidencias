# Ejercicio 17: Insertar aprendiz en lista ordenada
aprendices = ["Arias", "Benítez", "Cardona", "Díaz", "Espinosa", "Gómez", "López", "Martínez", "Ramírez", "Zapata"]
print("Antes:", aprendices)
nuevo = input("Apellido del nuevo aprendiz: ")
aprendices.append(nuevo)
aprendices.sort()
print("Después:", aprendices)
