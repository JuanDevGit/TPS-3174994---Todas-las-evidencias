# Ejercicio 21: Juego rojo-amarillo-verde
import random
secreto = random.sample(range(10), 3)
intentos = 0
while True:
    intento = []
    for i in range(1, 4):
        intento.append(int(input(f"Dígito {i}: ")))
    pista = []
    for i in range(3):
        if intento[i] == secreto[i]:
            pista.append("verde")
        elif intento[i] in secreto:
            pista.append("amarillo")
        else:
            pista.append("rojo")
    print("Pista:", pista)
    intentos += 1
    if pista == ["verde", "verde", "verde"]:
        print("¡Ganaste en", intentos, "intento(s)!")
        break
