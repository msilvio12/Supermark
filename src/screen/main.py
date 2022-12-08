from tkinter import *
from tkinter import ttk
from tkinter import messagebox as Messagebox
from usuario import Usuario
#from PIL import Image, ImageTk


# VARIABLE GLOBAL
root = Tk()
root.iconbitmap('src/assets/logo.jpg')
root.resizable(False, False)  # Error "no module named PIL"


nombre_usuario = StringVar()
contraseña_usuario = StringVar()
usuarios = []


# VENTANA PRINCIPAL
def createGUI():
    root.title("Login Usuario")
    root.geometry("800x200")
    root.config(bg="#F49739")

    #CONTENEDOR (FRAME)
    mainFrame = Frame(root)
    mainFrame.pack()
    mainFrame.config(width=400, height=300, background="#F49739")

    # ETIQUETAS DE TEXTO(LABEL)
    titulo = Label(mainFrame, text="BIENVENIDO A SUPERMARK",
                   font=("arial black", 30), background="#F49739")
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
    nombrelabel = Label(mainFrame, text="Nombre: ", font=(
        "impact", 16), background="#F49739")
    nombrelabel.grid(column=0, row=1)
    passlabel = Label(mainFrame, text="Contraseña: ",
                      font=("impact", 16), background="#F49739")
    passlabel.grid(column=0, row=2)

    # ENTRADAS DE TEXTO
    #nombre_usuario= StringVar()
    nombre_usuario.set("")
    nombreEntry = Entry(mainFrame, textvariable=nombre_usuario)
    nombreEntry.grid(column=1, row=1)

    # contraseña_usuario=StringVar()
    contraseña_usuario.set("")
    contraseñaEntry = Entry(
        mainFrame, textvariable=contraseña_usuario, show="*")
    contraseñaEntry.grid(column=1, row=2)

    # BOTONES
    iniciarSesionButton = ttk.Style()
    iniciarSesionButton.configure("TButton", font=(
        "arial black", 10), foreground="#0068DD")

    iniciarSesionButton = ttk.Button(
        mainFrame, text="Iniciar Sesion", command=iniciarSesion)
    iniciarSesionButton.grid(column=1, row=3, ipadx=5,
                             ipady=5, padx=10, pady=10)

    registrarButton = ttk.Button(
        mainFrame, text="Registrar", command=registrarUsuario)
    registrarButton.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)

    root.mainloop()


# INICIO DE SESION
def iniciarSesion():
    for user in usuarios:
        if user.nombre == nombre_usuario.get():
            test = user.conectar(contraseña_usuario.get())
            if test:
                Messagebox.showinfo(
                    "Conectado!", f"Se inicio sesión con [{user.nombre}] exito!!!")
            else:
                Messagebox.showerror("Error", "Contraseña incorrecta!!!")

            break
    else:
        Messagebox.showerror("Error", "No existen usuarios con ese nombre!!!")


# REGISTRO DE USUARIOS

def registrarUsuario():
    nom = nombre_usuario.get()
    contra = contraseña_usuario.get()
    nuevo_usuario = Usuario(nom, contra)  # en esta linea me marca error
    usuarios.append(nuevo_usuario)
    Messagebox.showinfo("Registro exitoso",
                        f"Se registró el usuario [{nom}] !!!")
    nombre_usuario.set("")
    # error list object is not callable/ no me registra el usuario
    contraseña_usuario.set("")


# INICIALIZACION DE INTERFAZ

if __name__ == "__main__":
    #user1= Usuario(input("Ingrese un nombre"), input("Ingrese su contraseña"))
    user1 = Usuario("silvio", "1212")
    usuarios.append(user1)
    createGUI()
