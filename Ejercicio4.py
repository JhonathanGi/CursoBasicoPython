#Mostrar numeros de 1 a 100 en orden inverso
lista = []
for numero in range(1,101):
    lista.append(numero)

listaR = sorted(lista, reverse=True) 
print(listaR)
