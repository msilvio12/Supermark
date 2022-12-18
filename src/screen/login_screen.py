from tkinter import (Button, Canvas, Entry, Frame, PhotoImage,
                     StringVar, Tk, messagebox)

from screen.home_screen import Inicio
from screen.signup_screen import Registro
from sql.query import Consulta


class Sesion(Tk):
    def __init__(self):
        super().__init__()
        self.title("Supermark")  # <- Titulo de la ventana
        self.geometry("650x350")  # <- Dimension de la ventana
        self.iconbitmap("src/assets/icon_logo.ico")  # <- Icono
        self.resizable(False, False)  # <- Evitar agrandar ventana
        self._sql = Consulta()  # <- Realizar consultas SQLite
        self._frame = Frame(self)  # <- Frame principal del programa
        self._usuario = StringVar(self)  # <- Usuario para pasarlo a SQLite
        self._clave = StringVar(self)  # <- Clave para pasarla a SQLite
        self.configure(bg="#f49739")  # <- Color de la ventana
        self.ventana_centrada()  # <- Centrar ventana en la pantalla
        self.ventana_sesion()  # <- Instanciar metodo
        self.mainloop()  # <- Mantener ventana ejecutansose hasta destruirla

    # Metodo para centrar la ventana en la pantalla
    def ventana_centrada(self):

        ancho = self.winfo_screenwidth()  # <- Obtener ancho
        alto = self.winfo_screenheight()  # <- Obtener altos
        x = (ancho / 2) - (self.winfo_width() / 2)  # <- Calcular posicion en x
        y = (alto / 2) - (self.winfo_height() / 2)  # <- Calcular posicion en y
        return self.geometry("%dx%d+%d+%d" %
                             (self.winfo_width(),
                              self.winfo_height(),
                              x, y))  # <- Centrar ventana

    # Contiene Label,Text,Image,Entry de la ventana usando canvas
    def ventana_sesion(self):

        canvas = Canvas(self._frame,
                        bg="#f49739",
                        height=350,
                        width=650,
                        bd=0,
                        highlightthickness=0,
                        relief="ridge")

        background_img = PhotoImage(
            file="src/assets/login_assets/background.png")
        canvas.create_image(197.5, 175.0,
                            image=background_img)

        # Label, Asset y Entry de usuario
        canvas.create_text(437.5, 34.0,
                           text="Usuario",
                           fill="#000000",
                           font=("Inter-Regular", int(15.0)))

        entry0_img = PhotoImage(
            file="src/assets/login_assets/blank_textBox.png")
        canvas.create_image(500.0, 65.0,
                            image=entry0_img)

        entry0 = Entry(canvas,
                       bd=0,
                       bg="#ffffff",
                       highlightthickness=0,
                       textvariable=self._usuario)

        entry0.place(x=415.0, y=50,
                     width=170.0,
                     height=28)

        # Label, Asset y Entry de clave
        canvas.create_text(430.0, 99.0,
                           text="Clave",
                           fill="#000000",
                           font=("Inter-Regular", int(15.0)))

        entry1_img = PhotoImage(
            file="src/assets/login_assets/blank_textBox.png")
        canvas.create_image(500.0, 125.0,
                            image=entry1_img)

        entry1 = Entry(canvas,
                       bd=0,
                       bg="#ffffff",
                       show="*",
                       highlightthickness=0,
                       textvariable=self._clave)

        entry1.place(x=415.0, y=110,
                     width=170.0,
                     height=28)

        # Asset boton recuperar usuario o clave
        img0 = PhotoImage(file="src/assets/login_assets/button_recover.png")
        b0 = Button(canvas,
                    image=img0,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.recuperar_clave,
                    relief="flat")

        b0.place(x=520, y=150,
                 width=80,
                 height=15)

        canvas.create_text(442.5, 156.0,
                           text="Olvido su clave o usuario?",
                           fill="#000000",
                           font=("Inter-Medium", int(10.0)))

        # Asset boton registrar
        img1 = PhotoImage(file="src/assets/login_assets/button_signup.png")
        b1 = Button(canvas,
                    image=img1,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.registrar,
                    relief="flat")

        b1.place(x=521, y=210,
                 width=89,
                 height=19)

        canvas.create_text(431.0, 219.0,
                           text="No tiene cuenta?",
                           fill="#000000",
                           font=("Inter-Medium", int(15.0)))

        # Asset boton iniciar sesion
        img2 = PhotoImage(file="src/assets/login_assets/button_login.png")
        b2 = Button(canvas,
                    image=img2,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.comprobar_campos,
                    relief="flat")

        b2.place(x=400, y=290,
                 width=200,
                 height=38)

        canvas.place(x=0, y=0)  # <- Ubicacion del canvas
        self._frame.pack()  # <- Ubicacion del frame dentro del frame principal
        canvas.pack()  # <- Ubicacion del canvas dentro del frame principal
        canvas.mainloop()  # <- Iniciar el loop del canvas

    def recuperar_clave(self) -> str:
        print("Botón opción en desarollo")
        return messagebox.showinfo("Supermark", "En desarollo...")

    # Instanciar objeto Registro para abrir otra ventana(TopLevel)
    def registrar(self) -> Registro:
        # self.withdraw()
        return Registro(self)

    # Comprobar Entry si estan vacios
    def comprobar_campos(self):
        if self._usuario.get() and self._clave.get() != "":
            return self.iniciar_sesion()
        return messagebox.showerror("Error", "Debe completar todos los campos")

    # Si la clave y el usuario son correctos, se inicia sesion
    def iniciar_sesion(self):
        if self._sql.iniciar_admin(self._usuario.get(), self._clave.get()):
            print(f"Se encontro administrador: {self._usuario.get()}")
            return messagebox.showinfo("Información",
                                       f"Administrador {self._usuario.get()}")

        elif self._sql.iniciar_cliente(self._usuario.get(), self._clave.get()):
            print(f"Se encontro cliente: {self._usuario.get()}")
            self.wm_withdraw()  # <- Minimizar ventana actual(login)
            return Inicio(self)

        return messagebox.showerror("Error",
                                    "Usuario o Contraseña incorrecto.")
