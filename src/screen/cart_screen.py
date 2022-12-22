from tkinter import END, Button, Frame, Listbox, Toplevel, messagebox, ttk


class ShoppingCart(Toplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.wait_visibility()  # <- Espera a que la ventana se crea
        self.grab_set()  # <- No interactuar con la ventana raiz hasta cerrar
        self.title("Supermark - Carrito")
        self.geometry("400x400")  # <- Dimension de la ventana
        self.iconbitmap("src/assets/icon_logo.ico")  # <- Icono
        self.resizable(False, False)  # <- Evitar agrandar ventana
        self.frame = Frame(self)  # <- Frame principal del programa
        self.configure(bg="#f49739")  # <- Color de fondo de la ventana
        self.ventana_centrada()  # <- Centrar ventana en la pantalla
        self.ventana_carrito()

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

    # Contiene Label,Text,Image,Entry,Button de la ventana usando Frame
    def ventana_carrito(self):
        self.frame.pack(fill="both", expand=True)
        self.frame.columnconfigure(0, weight=1)  # <- Ancho del frame
        self.frame.rowconfigure(0, weight=1)  # <- Alto del frame

        # Lista de productos a comprar
        self.lista_productos = Listbox(self.frame)
        self.lista_productos.grid(row=0, column=0, sticky="nsew")

        # Boton de agregar producto a la lista de compra
        self.agregar = Button(self.frame,
                              text="Agregar",
                              command=self.agregar_producto)
        self.agregar.grid(row=1, column=0, sticky="nsew")

        # Boton de eliminar producto de la lista de compra
        self.eliminar = Button(self.frame,
                               text="Eliminar",
                               command=self.eliminar_producto)
        self.eliminar.grid(row=2, column=0, sticky="nsew")

        # Boton de finalizar compra del carrito de compras
        self.finalizar = Button(self.frame,
                                text="Finalizar",
                                command=self.finalizar_compra)
        self.finalizar.grid(row=3, column=0, sticky="nsew")

    # Treeview dentro de Canvas
    def treeview(self, contenedor: Frame) -> ttk.Treeview:
        treeview = ttk.Treeview(contenedor,
                                columns=("#1", "#2", "#3", "#4", "#5", "#6"),
                                show="headings",
                                height=5,
                                selectmode="browse")

        treeview.place(x=620, y=150,
                       width=560,
                       height=390)

        return self.treeview_config(treeview)

    # Treeview config
    def treeview_config(self, treeview: ttk.Treeview) -> ttk.Treeview:

        treeview.column("#1", width=50, anchor="center", stretch=False)
        treeview.column("#2", width=150, anchor="w", stretch=False)
        treeview.column("#3", width=80, anchor="center", stretch=False)
        treeview.column("#4", width=80, anchor="center", stretch=False)
        treeview.column("#5", width=50, anchor="center", stretch=False)
        treeview.column("#6", width=120, anchor="w", stretch=False)

        treeview.heading("#1", text="ID")
        treeview.heading("#2", text="Nombre")
        treeview.heading("#3", text="Categoria")
        treeview.heading("#4", text="Precio")
        treeview.heading("#5", text="Stock")
        treeview.heading("#6", text="Descripcion")
        return treeview

    # Agregar producto a la lista de compra
    def agregar_producto(self):
        self.lista_productos.insert(END, "Producto")

    # Eliminar producto de la lista de compra
    def eliminar_producto(self):
        self.lista_productos.delete(END)

    # Finalizar compra del carrito de compras
    def finalizar_compra(self):
        messagebox.showinfo("Información",
                            "Se a realizado la compra")
        return self.destroy()
