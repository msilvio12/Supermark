from tkinter import (Button, Canvas, Frame, PhotoImage, Tk,
                     Toplevel, messagebox)

from sql.query import Consulta


class Inicio(Toplevel):
    def __init__(self, master: Tk, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.wait_visibility()  # <- Espera a que la ventana se crea
        self.grab_set()  # <- No interactuar con la ventana raiz hasta cerrar
        self.title("Supermark - Inicio")  # <- Titulo de la ventana
        self.geometry("1200x620")  # <- Dimension de la ventana
        self.iconbitmap("src/assets/icon_logo.ico")  # <- Icono
        self.resizable(False, False)  # <- Evitar agrandar ventana
        self._sql = Consulta()  # <- Realizar consultas SQLite
        self._frame = Frame(self)  # <- Frame principal del programa
        self.configure(bg="#f49739")  # <- Color de fondo de la ventana
        self.ventana_centrada()  # <- Centrar ventana en la pantalla
        self.ventana_inicio()  # <- Instanciar metodo
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
    def ventana_inicio(self):
        canvas = Canvas(self._frame,
                        bg="#f49739",
                        height=620,
                        width=1200,
                        bd=0,
                        highlightthickness=0,
                        relief="ridge")

        background_img = PhotoImage(
            file="src/assets/home_assets/background.png")
        canvas.create_image(590.0, 310.0,
                            image=background_img)

        img0 = PhotoImage(file="src/assets/home_assets/button_profile.png")
        b0 = Button(canvas,
                    image=img0,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.btn_clicked,
                    relief="flat")

        b0.place(x=25, y=340,
                 width=200,
                 height=38)

        img1 = PhotoImage(file="src/assets/home_assets/button_log.png")
        b1 = Button(canvas,
                    image=img1,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.btn_clicked,
                    relief="flat")

        b1.place(x=25, y=395,
                 width=200,
                 height=38)

        img2 = PhotoImage(file="src/assets/home_assets/button_discount.png")
        b2 = Button(canvas,
                    image=img2,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.btn_clicked,
                    relief="flat")

        b2.place(x=25, y=450,
                 width=200,
                 height=38)

        img3 = PhotoImage(file="src/assets/home_assets/button_signoff.png")
        b3 = Button(canvas,
                    image=img3,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.cerrar_sesion,
                    relief="flat")

        b3.place(x=25, y=560,
                 width=200,
                 height=38)

        img4 = PhotoImage(file="src/assets/home_assets/button_cart.png")
        b4 = Button(canvas,
                    image=img4,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.btn_clicked,
                    relief="flat")

        b4.place(x=930, y=12,
                 width=250,
                 height=70)

        img5 = PhotoImage(file="src/assets/home_assets/button_add.png")
        b5 = Button(canvas,
                    image=img5,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.btn_clicked,
                    relief="flat")

        b5.place(x=855, y=560,
                 width=200,
                 height=38)

        canvas.create_text(125.0, 227.0,
                           text="Cliente",
                           fill="#ffffff",
                           font=("Inter-ExtraBold", int(20.0)))

        canvas.create_text(125.5, 287.0,
                           text="Usuario",
                           fill="#ffffff",
                           font=("Inter-Regular", int(15.0)))

        canvas.create_text(489.0, 116.0,
                           text="Promociones",
                           fill="#000000",
                           font=("Inter-ExtraBold", int(25.0)))

        img6 = PhotoImage(file="src/assets/home_assets/img6.png")
        b6 = Button(canvas,
                    image=img6,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.btn_clicked,
                    relief="flat")

        b6.place(x=313, y=174,
                 width=130,
                 height=130)

        canvas.create_text(954.5, 116.0,
                           text="Lista de Productos",
                           fill="#000000",
                           font=("Inter-ExtraBold", int(25.0)))

        canvas.create_text(489.0, 348.0,
                           text="Articulo Destacado",
                           fill="#000000",
                           font=("Inter-ExtraBold", int(25.0)))

        img7 = PhotoImage(file="src/assets/home_assets/img7.png")
        b7 = Button(canvas,
                    image=img7,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.btn_clicked,
                    relief="flat")

        b7.place(x=515, y=395,
                 width=130,
                 height=130)

        canvas.place(x=0, y=0)  # <- Ubicacion del canvas
        self._frame.pack()  # <- Ubicacion del frame dentro del frame principal
        canvas.pack()  # <- Ubicacion del canvas dentro del frame principal
        canvas.mainloop()  # <- Iniciar el loop del canvas

    def btn_clicked(self):
        print("Oprimio botón")
        return messagebox.showinfo("Información",
                                   "En proceso...")

    def cerrar_sesion(self):
        print("Cerrar sesión")
        if messagebox.askyesno("Cerrar Sesión",
                               "¿Está seguro que desea cerrar sesión?"):

            self.wm_deiconify()  # <- Mostrar el frame principal
            return self.destroy()
