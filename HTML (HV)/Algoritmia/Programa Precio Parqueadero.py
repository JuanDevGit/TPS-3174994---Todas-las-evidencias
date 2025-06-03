#PROGRAMA PARQUEADERO
def ingresarHora(tipo):
    hora = int(input(f"Ingrese la hora de {tipo} (hhmm):"))
    hh = hora // 100
    mm = hora % 100
    mm += hh * 60
   
    return mm 

#Ingresar horas de entrada y salida
he = ingresarHora("entrada")
hs = ingresarHora("salida")


# Calcular minutos
if hs < he:
    tm = 1440 - he + hs
else:
    tm = hs - he


th = tm // 60 
resto = tm % 60
if resto > 0:
    th += 1 

#Calcular valor a pagar
th -= 1
valor = 2000 + th * 800

#Mostrar valor
print(f"El valor a pagar es ${valor}")