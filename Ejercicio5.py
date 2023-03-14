#Año bisiesto

def bisiesto(anio):
    
    if(anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
        return True
    else:
        return False
    
#Pedir al usuario el año
anio = input("Ingresa un año para verificar si es bisiesto: ")

#Convertir el valor a entero
anio = int(anio)

if bisiesto(anio):
    print(anio, "Es un año bisiesto")
else:
    print(anio, "No es bisiesto")
