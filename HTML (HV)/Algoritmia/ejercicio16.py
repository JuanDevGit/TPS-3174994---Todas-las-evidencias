# Ejercicio 16: Devolver cambio en monedas
cobrar = int(input("Valor a cobrar: "))
entregado = int(input("Valor entregado: "))
cambio = entregado - cobrar
for moneda in [1000, 500, 200, 100, 50]:
    cantidad = cambio // moneda
    cambio %= moneda
    if cantidad > 0:
        print(f"{cantidad} moneda(s) de {moneda}")
