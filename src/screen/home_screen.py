from tkinter import (Button, Canvas, Frame, PhotoImage, Tk, ttk,
                     Toplevel, messagebox)

from screen.cart_screen import ShoppingCart
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
        canvas.create_image(125.0, 310.0,
                            image=background_img)

        img0 = PhotoImage(file="src/assets/home_assets/button_profile.png")
        b0 = Button(canvas,
                    image=img0,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.vacio,
                    relief="flat")

        b0.place(x=25, y=340,
                 width=200,
                 height=38)

        img1 = PhotoImage(file="src/assets/home_assets/button_log.png")
        b1 = Button(canvas,
                    image=img1,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.vacio,
                    relief="flat")

        b1.place(x=25, y=395,
                 width=200,
                 height=38)

        img2 = PhotoImage(file="src/assets/home_assets/button_discount.png")
        b2 = Button(canvas,
                    image=img2,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.vacio,
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
                    command=self.iniciar_carrito,
                    relief="flat")

        b4.place(x=930, y=12,
                 width=250,
                 height=70)

        img5 = PhotoImage(file="src/assets/home_assets/button_add.png")
        b5 = Button(canvas,
                    image=img5,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.vacio,
                    relief="flat")

        b5.place(x=825, y=560,
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

        canvas.create_text(427.0, 116.0,
                           text="Promociones",
                           fill="#000000",
                           font=("Inter-ExtraBold", int(25.0)))

        img6 = PhotoImage(file="src/assets/home_assets/img6.png")
        b6 = Button(canvas,
                    image=img6,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.vacio,
                    relief="flat")

        b6.place(x=280, y=170,
                 width=130,
                 height=130)

        img7 = PhotoImage(file="src/assets/home_assets/img7.png")
        b7 = Button(canvas,
                    image=img7,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.vacio,
                    relief="flat")

        b7.place(x=440, y=170,
                 width=130,
                 height=130)

        canvas.create_text(925.5, 116.0,
                           text="Lista de Productos",
                           fill="#000000",
                           font=("Inter-ExtraBold", int(25.0)))

        canvas.create_text(427.0, 348.0,
                           text="Articulo Destacado",
                           fill="#000000",
                           font=("Inter-ExtraBold", int(25.0)))

        img8 = PhotoImage(file="src/assets/home_assets/img8.png")
        b8 = Button(canvas,
                    image=img8,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.vacio,
                    relief="flat")

        b8.place(x=440, y=395,
                 width=130,
                 height=130)

        img9 = PhotoImage(file="src/assets/home_assets/img9.png")
        b9 = Button(canvas,
                    image=img9,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.vacio,
                    relief="flat")

        b9.place(x=280, y=395,
                 width=130,
                 height=130)

        img10 = PhotoImage(file="src/assets/home_assets/button_reload.png")
        b10 = Button(canvas,
                     image=img10,
                     borderwidth=0,
                     highlightthickness=0,
                     command=self.vacio,
                     relief="flat")

        b10.place(x=1038, y=560,
                  width=38,
                  height=38)

        self.treeview(canvas)  # <-

        canvas.place(x=0, y=0)  # <- Ubicacion del canvas
        self._frame.pack()  # <- Ubicacion del frame dentro del frame principal
        canvas.pack()  # <- Ubicacion del canvas dentro del frame principal
        canvas.mainloop()  # <- Iniciar el loop del canvas

    # Treeview dentro de Canvas
    def treeview(self, contenedor: Canvas) -> ttk.Treeview:
        treeview = ttk.Treeview(contenedor,
                                columns=("#1", "#2", "#3", "#4"),
                                show="headings",
                                height=5,
                                selectmode="browse")

        treeview.place(x=620, y=150,
                       width=560,
                       height=390)

        return self.treeview_config(treeview)

    # Treeview config
    def treeview_config(self, treeview: ttk.Treeview) -> ttk.Treeview:

        treeview.column("#1", width=80, anchor="center", stretch=False)
        treeview.column("#2", width=250, anchor="center", stretch=False)
        treeview.column("#3", width=100, anchor="center", stretch=False)
        treeview.column("#4", width=90, anchor="center", stretch=False)

        treeview.heading("#1", text="ID")
        treeview.heading("#2", text="Nombre")
        treeview.heading("#3", text="Precio")
        treeview.heading("#4", text="Cantidad")
        return treeview

    # Boton clicked
    def vacio(self):
        print("Oprimio botón")
        return messagebox.showinfo("Información",
                                   "En proceso...")

    def iniciar_carrito(self):
        return ShoppingCart(self)

    def cerrar_sesion(self):
        print("Cerrar sesión")
        if messagebox.askyesno("Cerrar Sesión",
                               "¿Está seguro que desea cerrar sesión?"):

            self.wm_deiconify()  # <- Mostrar el frame principal
            return self.master.destroy()  # <- Cerrar el frame actual
