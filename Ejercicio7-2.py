import time

hora_salida = 19
hora_actual = input("Ingresa la hora actual en formato 0-23: ")

while True:

    #Obtener Horas y minutos de la hora local
    hora_actual = time.localtime().tm_hour
    minutos_actual = time.localtime().tm_min

    if hora_actual >= hora_salida:
        print("¡Es hora de irte a descansar!")
        break
    else:
        hora_r = hora_salida - hora_actual -1
        minutos_r = 60 - minutos_actual

        tiempo_restante = f"{hora_r:02}:{minutos_r:02}"
        print(f"Aún falta {tiempo_restante} horas para irte a descansar")
        time.sleep(60)


