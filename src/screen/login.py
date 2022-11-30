from tkinter import *
import tkinter as tk


#COLORES
fondo_entrar="#A6ACAF"
fondo_salir="#A6ACAF"
fondo_correcto="#239B56"
fondo_incorrecto="#922B21"
fondo_entrada="#922B21"


ventana=Tk()
ventana.title("SUPERMARK")
ventana.geometry("400x300+500+50")
ventana.resizable(width=False, height=False)

#fondo=tk.PhotoImage(file="logo.jpg")
#fondo1=tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1) 

#LOGIN
usuario=tk.StringVar()
contraseña=tk.StringVar()

#ENTRADAS
entrada=tk.Entry(ventana, textvariable=usuario, width=22, relief="flat", bg=fondo_entrada)
entrada.place(x=255, y=300)

#BOTONES

boton=Button(ventana, text="Ingresar", cursor="hand2", bg=fondo_entrar, width=45, relief="flat", font=("Arial Black", 12))
boton.place(x=310, y=405)







ventana.mainloop()