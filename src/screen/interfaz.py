from tkinter import*

root=Tk()
root.geometry("400x400")
root.title("SUPERMARK")
root.configure(background="#030303")
#root.iconbitmap("supermark_logo.ico")
titulo=Label(root, text="LISTA DE PRODUCTOS",font=("arial black", 15),
             bd=5, relief=FLAT, foreground="#050505", background="#F7DC6F")
titulo.place(x=20, y=90)

#VENTANA PRODUCTOS
productos=Label(root, text="SUPERMARK", font=("arial black", 40), 
                relief=FLAT, foreground="#922B21", background="#050505")
productos.pack()


def agregar():
    
    lista_productos.insert(END, entrada.get())

lista_productos=Listbox(root, width=50, font=("arial black", 10), foreground="#17202A", background="#A93226")
lista_productos.insert(0, "AZUCAR")
lista_productos.insert(1, "YERBA")
lista_productos.insert(2, "ACEITE")
lista_productos.insert(3, "DULCE DE LECHE")
lista_productos.insert(4, "MANTECA")
lista_productos.insert(5, "QUESO")
#lista_productos.insert(6, "JAMON")
#lista_productos.insert(7, "SAL")
#lista_productos.insert(8, "ARROZ")
#lista_productos.insert(9, "FIDEO")
lista_productos.pack()
lista_productos.place(x=20, y=150)

#ELIMINAR PRODUCTOS
def eliminar():
    posicion=lista_productos.curselection()[0]
    lista_productos.delete(posicion)
lista_productos.delete





#ENTRADA DE PRODUCTOS

entrada=Entry(root)
entrada.pack()
entrada.place(x=20, y=380, width=165)

#BOTONES
boton= Button(root, text="AGREGAR PRODUCTO", font=("arial black",10),
              foreground="#F7F9F9", background="#A93226",command=agregar)
boton.pack(side=LEFT, padx=15, pady=20)
boton.place(x=20, y=420)


boton=Button(root, text="ELIMINAR PRODUCTO", font=("arial black", 10),
             foreground="#F7F9F9",background="#A93226",command=eliminar)
boton.pack(side=RIGHT, padx=15,pady=20)
boton.place(x=20, y=460)


root.mainloop()