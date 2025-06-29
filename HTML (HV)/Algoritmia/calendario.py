import calendar

# Función para ingresar mes y año
def ingresarMesAnio():
    while True:
        txtFecha = input("Ingrese mes y año mm/aaaa: ")
        listafecha = txtFecha.split("/")
        try:
            mes = int(listafecha[0])
            anio = int(listafecha[1])
            if mes > 0 and mes < 13 and anio > 1600:
                break
            else:
                print("Fecha fuera de rango")
        except:
            print("Error en formato de fecha")
    return mes, anio

# ************** PROGRAMA PRINCIPAL *******************
mes, anio = ingresarMesAnio()

# Crear calendario del mes y año ingresado
cal = calendar.TextCalendar(calendar.SUNDAY)  # Calendario que inicia en domingo
calendario_mes = cal.formatmonth(anio, mes)

# Mostrar calendario
print("\nCALENDARIO DEL MES:")
print(calendario_mes)





















































