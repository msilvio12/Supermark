from tkinter import*
from tkinter import messagebox

#creando la clase

class App():
    #metodo constructor
    def __init__(self):
#objeto tkinter
     ventana=Tk()
     ventana.title("SUPERMARK-USUARIOS")
     ventana.geometry("400x300")
     ventana.configure(bg="#A93226")
     #widgets
     self.label1=Label(ventana, text="NOMBRE")
     self.label1.place(x=40, y=30)

     self.boton=Button(ventana, text="REGISTRARSE", command=self.mensaje)
     self.boton.place(x=60, y=80)


     
     
     self.text1=Entry(ventana)
     self.text1.place(x=100, y=30)


     
     ventana.mainloop()
    def mensaje(self):
        print("BIENVENIDO AL SISTEMA")
        messagebox.showinfo(message="BIENVENIDO AL SISTEMA "+self.text1.get(), title="CLIENTE")

#objeto principal
Objeto_ventana=App()

        
