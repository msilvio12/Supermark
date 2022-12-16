from tkinter import*
import tkinter as tk
import mysql.connector
from  tkinter import Toplevel
from tkinter import Toplevel
from tkinter import ttk
import os


root=Tk()
root.geometry("400x400")
root.title("SUPERMARK")
root.configure(background="#030303")
titulo=Label(root, text=("SUPERMARK"),bd=5, relief=GROOVE, 
             font=("arial black", 35), bg="#050505", fg="#D0D3D4").pack(fill=X)
subtitulo=Label(root, text=("BIENVENIDOS!!!"),bd=5, relief=FLAT, 
             font=("arial black", 20), bg="#050505", fg="#D0D3D4").pack(fill=Y)             

#ICONO DE VENTANA
root.iconbitmap("Supermark\src\screen\carrito-de-compras.ico")            

#LOGO

img=PhotoImage(file="Supermark\src\screen\logosupermark.gif")

fondo=Label(root, image=img,width=250, height=100).place(x=0, y=2)



#DATOS CLIENTES
datos_clientes=LabelFrame(root, text="CLIENTES", font=("arial black", 14),
                          bd=10, background="#F7DC6F", relief=FLAT)
datos_clientes.place(x=0, y=120, relwidth=1)

nombre=Label(datos_clientes, text="Usuario", font=("arial black", 12), 
             bg="#F7DC6F").grid(row=0, column=0, padx=8)
nombre_entry=Entry(datos_clientes, borderwidth=4, 
             width=30).grid(row=0, column=1, padx=8)

direccion=Label(datos_clientes, text="Dirección", font=("arial black", 12),
                bg="#F7DC6F").grid(row=0, column=3, padx=8)
direccion_entry=Entry(datos_clientes, borderwidth=4, 
             width=30).grid(row=0, column=4, padx=8)

carrito=Label(datos_clientes, text="Carrito $", font=("arial black", 12), 
              bg="#F7DC6F").grid(row=0, column=8, padx=8)
carrito_entry=Entry(datos_clientes, borderwidth=4, 
             width=30).grid(row=0, column=9, padx=8)  

#BOTON CIERRE DE SESION DEL USUARIO
cerrar_sesion=Button(datos_clientes,text="Cerrar Sesión", font=("arial black", 10), 
                    bg="#A93226", foreground="#F7F9F9").grid(row=0, column=12, padx=8)                         


#VENTANA PRODUCTOS
titulo_productos=Label(root, text="LISTA DE PRODUCTOS",font=("arial black", 15),
             bd=5, relief=FLAT, foreground="#050505", background="#F7DC6F")
titulo_productos.place(x=0, y=200, width=300)


#VENTANA FACTURACION

factura=Label(root, text="FACTURACION",font=("arial black", 15),
             bd=5, relief=FLAT, foreground="#050505", background="#F7DC6F")
factura.place(x=600, y=200, width=300)

def facturar():
    
    factura.insert(END, entrada.get())

factura=Listbox(root, width=50, font=("arial black", 10), foreground="#F4F6F7", background="#A93226")
factura.insert(0, "EFECTIVO")
factura.insert(1, "TARJETA")
factura.insert(2, "TRANSFERENCIA")
factura.pack()
factura.place(x=600, y=250)

boton1=Button(root, text="CONFIRMAR PAGO", font=("arial black",10),
              foreground="#F7F9F9", background="#A93226",command=facturar)
boton1.pack(side=LEFT, padx=15, pady=20)
boton1.place(x=602, y=410)


 


#FUNCION PARA AGREGAR PRODUCTOS

def agregar():
    
    lista_productos.insert(END, entrada.get())

lista_productos=Listbox(root, width=50, font=("arial black", 10), foreground="#F4F6F7", background="#A93226")
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
lista_productos.place(x=0, y=250)

# FUNCION PARA ELIMINAR PRODUCTOS
def eliminar():
    posicion=lista_productos.curselection()[0]
    lista_productos.delete(posicion)
lista_productos.delete





#ENTRADA DE PRODUCTOS

entrada=Entry(root)
entrada.pack()
entrada.place(x=20, y=480, width=165)

#BOTONES DEL CLIENTE
boton=Button(root, text="AGREGAR PRODUCTO", font=("arial black",10),
              foreground="#F7F9F9", background="#A93226",command=agregar)
boton.pack(side=LEFT, padx=15, pady=20)
boton.place(x=20, y=520)


boton=Button(root, text="ELIMINAR PRODUCTO", font=("arial black", 10),
             foreground="#F7F9F9",background="#A93226",command=eliminar)
boton.pack(side=RIGHT, padx=15,pady=20)
boton.place(x=20, y=560)

#BOTON DE DESCUENTO POR COMPRA

descuento=Label(root, text="DESCUENTO POR COMPRA",font=("arial black", 10),
             bd=5, relief=FLAT, foreground="#050505", background="#F7DC6F")
descuento.place(x=20, y=610, width=300)

entrada=Entry(root)
entrada.pack()
entrada.place(x=20, y=660, width=165)





#BOTONES DE OPERACION

boton_frame=Frame(titulo, bd=7, relief=FLAT, bg="#A93226")
boton_frame.place(x=600, y=600, width=680, height=70)

boton_factura=Button(boton_frame, text="IMPRIMIR FACTURA", width=20, font=("arial black", 10), 
                     bg="#A93226", foreground="#F7F9F9").grid(row=0, column=0,
                     padx=12, pady=12)


boton_comprar=Button(boton_frame, text="HISTORIAL DE COMPRA", width=20, font=("arial black", 10), 
                     bg="#A93226", foreground="#F7F9F9").grid(row=0, column=1,
                     padx=10, pady=6)

boton_enviar=Button(boton_frame, text="ENVIO A DOMICILIO", width=20, font=("arial black", 10), 
                     bg="#A93226", foreground="#F7F9F9").grid(row=0, column=2,
                     padx=10, pady=6)

                                         


root.mainloop()


