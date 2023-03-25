import tkinter

class interface:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('Opciones de Color')
        self.window.geometry('350x200')
        self.opcion_sel = tkinter.StringVar()
        self.opcion_sel.set(None)

        fuente = 'Times new roman'
        tamaño_fuente = 16

        opciones = ['Amarillo', 'Azul', 'Rojo']
        for opcion in opciones:
            tkinter.Radiobutton(self.window, text=opcion, variable=self.opcion_sel, value=opcion, font=(fuente, tamaño_fuente)).pack(anchor=tkinter.W)
        
        tkinter.Button(self.window, text='Reiniciar', command=self.reiniciar, font=(fuente, tamaño_fuente), bg='light blue', relief='raised', borderwidth=4, activebackground='white', cursor='X_cursor').pack()

        self.label=tkinter.Label(self.window, text='')
        self.label.pack()


    def reiniciar(self):
        self.opcion_sel.set(None)
        self.label.config(text='')

    def inicio(self):
        self.window.mainloop()

    def muestra_opcion_sel(self):
        self.label.config(text='La opcion seleccionada es: ' + self.opcion_sel.get())


if __name__=='__main__':
    app = interface()
    app.inicio()


