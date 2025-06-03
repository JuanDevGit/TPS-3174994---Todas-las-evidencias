# Convertir texto a ASCII y ASCII a texto
print("1. Texto a ASCII")
print("2. ASCII a texto")
op = input("Elija una opción: ")

if op == "1":
    texto = input("Ingrese texto: ")
    for letra in texto:
        print(ord(letra), end=" ")
elif op == "2":
    numeros = input("Ingrese códigos ASCII separados por espacios: ")
    partes = numeros.split()
    for codigo in partes:
        print(chr(int(codigo)), end="")
print()
