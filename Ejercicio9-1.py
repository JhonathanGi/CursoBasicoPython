
paises = []
n = int(input('Cuantos paises deseas agregar: '))

for i in range(n):
    pais = input('Ingresa el nombre del pais: ').upper()
    paises.append(pais)

#Ordena paises y Elimina los repetidos
paisesF = sorted(list(set(paises)))

print('Los paises ingresados a la lista son: ', paisesF)

