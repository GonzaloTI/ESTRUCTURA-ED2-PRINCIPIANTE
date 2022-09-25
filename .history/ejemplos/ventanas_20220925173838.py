# importacion de la libreria Tkinter para invocar el modo grafico
from tkinter import *
# Implementacion de la clase grafica dibujar
class Ventana(object):
# Metodo que instancia la clase dibujo e inicializa el modo grafico
    def __init__(self,master):
        self.master = master
        self.inicializar_gui()
        self.lienzo = Canvas(self.master,width=100,height=100)
 # creamos los widget dentro del canvas       
    def inicializar_gui(self):
        Button(self.master,text='Dibujar',command=lambda: self.rectangulo()).pack()

    def rectangulo(self):
        self.lienzo.pack(expand=YES,fill=BOTH)
        self.lienzo.create_rectangle(10,10,100,100,width=5,fill='red')

    def linea(self):
        self.lienzo.pack(expand=YES,fill=BOTH)
        self.lienzo.create_line(0, 200, 200, 0, width=5, fill='green')

def main():
    master = Tk()
    master.title("Mi primer ventana") 
    master.geometry('300x300') 
    
    MiVentana = Ventana(master)

    master.mainloop()     

if __name__ == "__main__":
    main()     