
from tkinter import *




Admin = Tk()
Admin.title("SUPERMARK")
Admin.geometry("700x300")
Admin.config(bg="#A93226")
Titulo = Label(Admin, text="SUPERMARK", bd=5, relief=FLAT, font=("Arial black",30), bg="#424949", fg="#F4D03F").pack(fill=X)


#VENTANA PARA REGISTRO DE USUARIOS
'''
def enviar_boton():
    ventana_usuario = Toplevel()
    ventana_usuario.title("REGISTRO DE USUARIO")
    ventana_usuario.geometry("400x250")
    ventana_usuario.config(bg="#A93226")
    valor_entrada=entrada.get()
    etiqueta=Label(ventana_usuario, text="Bienvenido al registro de usuarios!!!" + valor_entrada).grid(row=0)
    cerrar_ventana= Button(Admin, text="Cerrar la ventana", command=ventana_usuario.destroy).grid(row=2)
entrada= Entry(Admin, width=20)
entrada.grid(row=0)
registro=Button(Admin, text="Registrarse", command=enviar_boton).grid(row=1)
cerrar_admin=Button(Admin, text="Cerrar ventana principal", command=Admin.destroy).grid(row=3)
'''
#VENTANA PRINCIPAL
 
datos_cliente = LabelFrame(Admin, text="Informacion del cliente", font=("Arial black",15), bg="#1B2631", fg="#D0D3D4", bd=10)
datos_cliente.place(x=0, y=80, relwidth=1)

nombre =Label(datos_cliente, text="Nombre",font=("Arial black",12), bg="#1B2631", fg="#F4F6F7").grid(row=0, column=0, padx=8)
nombre_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=1, padx=8)

apellido =Label(datos_cliente, text="Apellido",font=("Arial black",12), bg="#1B2631", fg="#F4F6F7").grid(row=0, column=2, padx=8)
apellido_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=3, padx=8)

direccion =Label(datos_cliente, text="Direccion",font=("Arial black",12), bg="#1B2631", fg="#F4F6F7").grid(row=0, column=4, padx=8)
direccion_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=5, padx=8)

correo =Label(datos_cliente, text="Correo",font=("Arial black",12), bg="#1B2631", fg="#F4F6F7").grid(row=0, column=6, padx=8)
correo_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=7, padx=8)

historial_compra=Label(datos_cliente, text="Historial de Compra",font=("Arial black",12), bg="#1B2631", fg="#F4F6F7").grid(row=0, column=8, padx=8)
historial_compra_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=9, padx=8)

#SEPARADORES POR SECCIONES
productos= Label(Admin, text="Productos", font=("Arial black",20),bg="#1B2631",fg="#F4F6F7", relief=FLAT, borderwidth=10)
productos.place(x=12, y=180, width=1327)

productos_disponibles = LabelFrame(Admin, text="LISTA DE PRODUCTOS", font=("Arial black", 15), bg="#1B2631", fg="#F7DC6F", relief=FLAT, borderwidth=10)
productos_disponibles.place(x=5, y=250, height=380, width=325)

carrito = LabelFrame(Admin, text="CARRITO", font=("Arial black", 15), bg="#1B2631", fg="#F7DC6F", relief=FLAT, borderwidth=10)
carrito.place(x=500, y=250, height=380, width=325)

#TOTAL DE LA COMPRA CON SCROLL

frame = Frame(Admin, bd=10, relief=FLAT, bg="#1B2631")
frame.place(x=1012, y=250, width=330, height=380) 

detalle=Label(frame, text="DETALLE DE COMPRA",font=("Arial black", 15), bg="#1B2631", fg="#F7DC6F", relief=FLAT, borderwidth=10).pack(fill=X) 

#SCROLL
scroll=Scrollbar(frame, orient=VERTICAL)
textarea=Text(frame, yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=textarea.yview)
textarea.pack(fill=BOTH, expand=1)

#LISTA DE PRODUCTOS POR DENTRO
#1
arroz=Label(productos_disponibles,text="ARROZ",font=("Arial black",12), bg="#1B2631", fg="#F7DC6F").grid(row=0, column=6, padx=8)
arroz_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=7, padx=8) 
#2
fideos=Label(productos_disponibles,text="FIDEOS",font=("Arial black",12), bg="#1B2631", fg="#F7DC6F").grid(row=2, column=6, padx=8)
fideos_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=7, padx=8) 
#3
aceite=Label(productos_disponibles,text="ACEITE",font=("Arial black",12), bg="#1B2631", fg="#F7DC6F").grid(row=4, column=6, padx=8)
aceite_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=7, padx=8) 
#4
yerba=Label(productos_disponibles,text="YERBA",font=("Arial black",12), bg="#1B2631", fg="#F7DC6F").grid(row=6, column=6, padx=8)
yerba_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=7, padx=8) 
#5
azucar=Label(productos_disponibles,text="AZUCAR",font=("Arial black",12), bg="#1B2631", fg="#F7DC6F").grid(row=8, column=6, padx=8)
azucar_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=7, padx=8) 
#6
dulce_de_leche=Label(productos_disponibles,text="DULCE DE LECHE",font=("Arial black",12), bg="#1B2631", fg="#F7DC6F").grid(row=10, column=6, padx=8)
dulce_de_leche_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=7, padx=8) 
#7
mermelada=Label(productos_disponibles,text="MERMELADA",font=("Arial black",12), bg="#1B2631", fg="#F7DC6F").grid(row=12, column=6, padx=8)
mermelada_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=7, padx=8) 
#8
manteca=Label(productos_disponibles,text="MANTECA",font=("Arial black",12), bg="#1B2631", fg="#F7DC6F").grid(row=14, column=6, padx=8)
manteca_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=7, padx=8) 
#9
sal=Label(productos_disponibles,text="SAL",font=("Arial black",12), bg="#1B2631", fg="#F7DC6F").grid(row=16, column=6, padx=8)
sal_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=7, padx=8) 
#10
cafe=Label(productos_disponibles,text="CAFE",font=("Arial black",12), bg="#1B2631", fg="#F7DC6F").grid(row=18, column=6, padx=8)
cafe_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=7, padx=8) 

queso=Label(productos_disponibles,text="QUESO",font=("Arial black",12), bg="#1B2631", fg="#F7DC6F").grid(row=18, column=6, padx=8)
queso_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=7, padx=8) 


jamon=Label(productos_disponibles,text="JAMON",font=("Arial black",12), bg="#1B2631", fg="#F7DC6F").grid(row=18, column=6, padx=8)
jamon_entry = Entry(datos_cliente, borderwidth=4, width=21).grid(row=0, column=7, padx=8)




#TOTAL DE LA COMPRA
gasto=LabelFrame(Admin, text="GASTO TOTAL : ",font=("Arial black",12), bg="#424949", fg="#F4F6F7",relief=FLAT, borderwidth=10)
gasto.place(x=0, y=600, relwidth=1, height=137)

#INFO DE GASTO
info_label=Label(gasto, text="DESCUENTO POR COMPRA : ",font=("Arial black",10), bg="#F7DC6F").grid(row=0, column=0)
info_label_entry= Entry(gasto, width=30, borderwidth=2).grid(row=0, column=1, padx=10, pady=15)

#CREACION DE BOTONES
button_frame = Frame(gasto, bd=7, relief= FLAT, bg="#F7DC6F")
button_frame.place(x=500, width=800, height=95)

button_factura = Button(button_frame, text="FACTURA", width=15, font=("Arial black",12), pady=10, bg="#F7DC6F").grid(row=0, column=0, padx=12, pady=12)

button_imprimir = Button(button_frame, text="IMPRIMIR", width=15, font=("Arial black",12), pady=10, bg="#F7DC6F").grid(row=0, column=1, padx=12, pady=12)

button_reclamo = Button(button_frame, text="RECLAMOS", width=15, font=("Arial black",12), pady=10, bg="#F7DC6F").grid(row=0, column=2, padx=12, pady=12)

button_salir = Button(button_frame, text="SALIR", width=15, font=("Arial black",12), pady=10, bg="#F7DC6F").grid(row=0, column=3, padx=12, pady=12)

Admin.mainloop()
