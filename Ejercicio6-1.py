class Vehiculo:
    def __init__(self, color, ruedas, puertas):

        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas

class Coche(Vehiculo):

    #Para sobreescribir y agregar los atributos a la clase Coche
    def __init__(self, color, ruedas, puertas, velocidad,cilindrada):

        #Para inicializar los atributos heredados de la super clase Vehiculo
        super().__init__(color, ruedas, puertas)

        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def estado(self):

        print('Color: ', self.color, '\nNumero de Ruedas: ', self.ruedas, '\nPuertas: ', self.puertas, '\nVelocidad Máxima: ', self.velocidad, 'Km/h' '\nCilindrada: ', self.cilindrada, 'Litros')

miCoche = Coche('Rojo', 4, 2, 200, 1.6)
miCoche.estado()