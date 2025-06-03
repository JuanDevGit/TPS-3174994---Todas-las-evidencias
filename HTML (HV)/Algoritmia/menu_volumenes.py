# Menú para calcular áreas y volúmenes
while True:
    print("\n1. Área de rectángulo")
    print("2. Volumen de cilindro")
    print("3. Volumen de cubo")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        largo = float(input("Largo: "))
        ancho = float(input("Ancho: "))
        print("Área:", largo * ancho)
    elif opcion == "2":
        radio = float(input("Radio: "))
        altura = float(input("Altura: "))
        print("Volumen:", 3.1416 * radio * radio * altura)
    elif opcion == "3":
        lado = float(input("Lado: "))
        print("Volumen:", lado ** 3)
    elif opcion == "4":
        break
