import pickle
class Carro:
    def __init__(self, fabricante, modelo, año, cilindrada, precio):

        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.cilindrada = cilindrada
        self.precio = precio
        
    def estado(self):
        print('Fabricante: ',self.fabricante,'\nModelo: ',self.modelo,'\nAño de Fabricación: ',self.año, '\nCilindrada (litros): ',self.cilindrada,'\nPrecio ($): ',self.precio)


#carro1 = Carro('Honda', 'Civic', 1998, 1.8, 5000)
#carro1.estado()

"""
#serializar el fichero
f = open('datoscarro1.bin', 'wb')

#Guardar usando dump
pickle.dump(carro1, f)
f.close()

"""
#Recuperar fichero para solo lectura
f2 = open('datoscarro1.bin', 'rb')
carro1 = pickle.load(f2)
f2.close()

print(type(carro1))
print(carro1.estado())

