a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
suma = 0
# Empezamos desde el siguiente número después de 'a' y terminamos antes de 'b'
for i in range(min(a, b) + 1, max(a, b)):  # Sin incluir a y b
    if i % 2 == 0:
        suma += i
print("La suma de los pares entre", a, "y", b, "es:", suma)
