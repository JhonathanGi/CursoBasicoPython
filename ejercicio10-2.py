import tkinter

class interface2:
    def __init__(self, window):
        self.window = window
        self.window.title('Lista de selección')
        self.window.geometry('300x300')

        #contenedor de los elementos
        self.contenedor = tkinter.Frame(self.window)
        self.contenedor.config(width=300, height=300)
        self.contenedor.pack()

        #lista 
        self.frutas = ['Aguacate', 'Banano', 'Coco', 'Mango', 'Maracuyá', 'Mora', 'Uva']
        self.seleccionadas = []

        for fruta in self.frutas:
            var = tkinter.BooleanVar()
            checkb = tkinter.Checkbutton(self.contenedor, text=fruta, variable=var, onvalue=True, offvalue=False, command=self.mostrar_seleccionadas)

            checkb.pack(anchor='w')
            self.seleccionadas.append((fruta, var))

        #label
        self.label = tkinter.Label(self.contenedor, text='')
        self.label.pack(anchor='center')
    
    def mostrar_seleccionadas(self):
        select = [seleccion[0] for seleccion in self.seleccionadas if seleccion[1].get()]
        texto = ', '.join(select)
        self.label.config(text=texto)

#ventana
window = tkinter.Tk()
interfaz = interface2(window)

#inicio del bucle
window.mainloop()

        
