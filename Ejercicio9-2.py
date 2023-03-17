from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]

#Filtro la lista por numeros impares
numerosI = list(filter(lambda x: x % 2 != 0, numeros))

#Sumo los numeros de la lista filtrada de numeros impares
sumaI = reduce(lambda x,y : x + y, numerosI)

print('La lista de los números filtrados impares es: ',numerosI,'\nLa suma de los números impares es: ',sumaI)



