from tkinter import Tk, ttk, Frame, Toplevel, Canvas, PhotoImage, StringVar, Entry, Button, messagebox
from sql.query import Consulta
from screen.singup import Registro


class Inicio(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Supermark")  # <-- Titulo de la ventana
        self.geometry("650x350")  # <-- Dimension de la ventana
        self.iconbitmap("src/assets/logosupermark.ico")  # <-- Icono a venta
        self.configure(bg="#f49739")  # <-- Color de fondo de la ventana
        self.usuario = StringVar()  # <-- Retener el usuario para pasarlo a SQLite
        self.clave = StringVar()  # <-- Retener la clave para pasarla a SQLite
        self.sql = Consulta()  # <-- Instanciar el objeto para realizar consultas SQLite
        self.canvas = Canvas(self,
                             bg="#f49739",
                             height=350,
                             width=650,
                             bd=0,
                             highlightthickness=0,
                             relief="ridge")
        self.canvas.place(x=0, y=0)
        self.resizable(False, False)  # <-- Evitar agrandar ventana
        self.ventana_inicio()  # <-- Instanciar metodo
        self.mainloop()  # <-- Mantener la ventana ejecutansose hasta destruirla

    # Metodo contiene Label,Text,Image,Entry de la ventana usando Canvas
    def ventana_inicio(self):

        background_img = PhotoImage(file=f"src/assets/login/background.png")
        self.canvas.create_image(197.5, 175.0,
                                 image=background_img)

        # Label, Asset y Entry de usuario
        self.canvas.create_text(437.5, 34.0,
                                text="Usuario",
                                fill="#000000",
                                font=("Inter-Regular", int(15.0)))

        entry0_img = PhotoImage(file=f"src/assets/login/img_textBox0.png")
        self.canvas.create_image(500.0, 65.0,
                                 image=entry0_img)

        entry0 = Entry(self,
                       bd=0,
                       bg="#ffffff",
                       highlightthickness=0,
                       textvariable=self.usuario)

        entry0.place(x=415.0, y=50,
                     width=170.0,
                     height=28)

        # Label, Asset y Entry de clave
        self.canvas.create_text(430.0, 99.0,
                                text="Clave",
                                fill="#000000",
                                font=("Inter-Regular", int(15.0)))

        entry1_img = PhotoImage(file=f"src/assets/login/img_textBox1.png")
        self.canvas.create_image(500.0, 125.0,
                                 image=entry1_img)

        entry1 = Entry(self,
                       bd=0,
                       bg="#ffffff",
                       show="*",
                       highlightthickness=0)

        entry1.place(x=415.0, y=110,
                     width=170.0,
                     height=28)

        # Asset boton recuperar usuario o clave
        img0 = PhotoImage(file=f"src/assets/login/img0.png")
        b0 = Button(self,
                    image=img0,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.recuperar_clave,
                    relief="flat")

        b0.place(x=520, y=150,
                 width=80,
                 height=15)

        self.canvas.create_text(442.5, 156.0,
                                text="Olvido su clave o usuario?",
                                fill="#000000",
                                font=("Inter-Medium", int(10.0)))

        # Asset boton registrar
        img1 = PhotoImage(file=f"src/assets/login/img1.png")
        b1 = Button(self,
                    image=img1,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.registrar,
                    relief="flat")

        b1.place(x=521, y=210,
                 width=89,
                 height=19)

        self.canvas.create_text(431.0, 219.0,
                                text="No tiene cuenta?",
                                fill="#000000",
                                font=("Inter-Medium", int(15.0)))

        # Asset boton iniciar sesion
        img2 = PhotoImage(file=f"src/assets/login/img2.png")
        b2 = Button(self,
                    image=img2,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.iniciar_sesion,
                    relief="flat")

        b2.place(x=400, y=290,
                 width=200,
                 height=38)

        self.mainloop()

    def recuperar_clave(self):
        print("Botón opción en desarollo")
        messagebox.showinfo(message="En desarollo...", title="Supermark")

    # Metodo para instanciar objeto Registro
    def registrar(self):
        Registro(self)

    def iniciar_sesion(self):
        if self.usuario.get() and self.clave.get() != None:
            if self.sql.buscar_usuario(self.usuario.get(), self.clave.get()):
                messagebox.showinfo(title="Información",
                                    message=f"Se inicio sesión con {self.usuario.get()}.")
            else:
                messagebox.showerror(title="Error",
                                     message="Usuario o Contraseña incorrecto.")
        else:
            messagebox.showwarning(title="Advertencia",
                                   message="No ingreso ningun usuario o clave.")
