class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    #Metodo Imprimir Datos
    def datos(self):
        print('Nombre: ',self.nombre)
        print('Nota: ',self.nota)

    #Metodo Resultado
    def resultado(self):
        if self.nota >= 3:
            print('El estudiante', self.nombre, 'aprobó el curso.')
        else:
            print('El estudiante', self.nombre, 'no aprobó el curso.')

estudiante1 = Estudiante('Jhonathan', 4.5)
estudiante1.datos()
estudiante1.resultado()