from tkinter import (Button, Canvas, Entry, PhotoImage,
                     StringVar, Tk, Toplevel, messagebox)

from sql.query import Consulta


class Registro(Toplevel):
    def __init__(self, master: Tk, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.wait_visibility()  # <- Espera a que la ventana se crea
        self.grab_set()  # <- No interactuar con la ventana raiz hasta cerrar
        self.title("Supermark - Registro")  # <- Titulo de la ventana
        self.geometry("650x350")  # <- Dimension de la ventana
        self.iconbitmap("src/assets/icon_logo.ico")  # <-- Icono a venta
        self.resizable(False, False)  # <- Evitar agrandar ventana
        self._sql = Consulta()  # <- Realizar consultas SQLite
        self._nombre = StringVar(self)  # <- Datos para registrar a SQLite
        self._apellido = StringVar(self)
        self._direccion = StringVar(self)
        self._usuario = StringVar(self)
        self._clave = StringVar(self)
        self.configure(bg="#f49739")  # <- Color de fondo de la ventana
        self.ventana_centrada()  # <- Centrar ventana en la pantalla
        self.ventana_registro()  # <- Instanciar metodo
        self.mainloop()  # <- Mantener la ventana ejecutansose hasta destruirla

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

    def ventana_registro(self):
        self._canvas = Canvas(self,
                              bg="#f49739",
                              height=350,
                              width=650,
                              bd=0,
                              highlightthickness=0,
                              relief="ridge")
        self._canvas.place(x=0, y=0)

        background_img = PhotoImage(
            file="src/assets/signup_assets/background.png")

        self._canvas.create_image(325.0, 235.0,
                                  image=background_img)

        entry0_img = PhotoImage(
            file="src/assets/signup_assets/blanck_textBox.png")
        self._canvas.create_image(225.0, 39.0,
                                  image=entry0_img)

        entry0 = Entry(self,
                       bd=0,
                       bg="#ffffff",
                       highlightthickness=0,
                       textvariable=self._nombre)

        entry0.place(x=140.0, y=24,
                     width=170.0,
                     height=28)

        self._canvas.create_text(88.5, 39.0,
                                 text="Nombre",
                                 fill="#000000",
                                 font=("Inter-Regular", int(15.0)))

        entry1_img = PhotoImage(
            file="src/assets/signup_assets/blanck_textBox.png")
        self._canvas.create_image(225.0, 95.0,
                                  image=entry1_img)

        entry1 = Entry(self,
                       bd=0,
                       bg="#ffffff",
                       highlightthickness=0,
                       textvariable=self._apellido)

        entry1.place(x=140.0, y=80,
                     width=170.0,
                     height=28)

        self._canvas.create_text(88.5, 94.0,
                                 text="Apellido",
                                 fill="#000000",
                                 font=("Inter-Regular", int(15.0)))

        entry2_img = PhotoImage(
            file="src/assets/signup_assets/blanck_textBox.png")
        self._canvas.create_image(513.0, 39.0,
                                  image=entry2_img)

        entry2 = Entry(self,
                       bd=0,
                       bg="#ffffff",
                       highlightthickness=0,
                       textvariable=self._usuario)

        entry2.place(x=428.0, y=24,
                     width=170.0,
                     height=28)

        self._canvas.create_text(377.5, 39.0,
                                 text="Usuario",
                                 fill="#000000",
                                 font=("Inter-Regular", int(15.0)))

        entry3_img = PhotoImage(
            file="src/assets/signup_assets/blanck_textBox.png")
        self._canvas.create_image(513.0, 95.0,
                                  image=entry3_img)

        entry3 = Entry(self,
                       bd=0,
                       bg="#ffffff",
                       highlightthickness=0,
                       textvariable=self._clave)

        entry3.place(x=428.0, y=80,
                     width=170.0,
                     height=28)

        self._canvas.create_text(385.0, 94.0,
                                 text="Clave",
                                 fill="#000000",
                                 font=("Inter-Regular", int(15.0)))

        entry4_img = PhotoImage(
            file="src/assets/signup_assets/blanck_textBox.png")
        self._canvas.create_image(225.0, 150.0,
                                  image=entry4_img)

        entry4 = Entry(self,
                       bd=0,
                       bg="#ffffff",
                       highlightthickness=0,
                       textvariable=self._direccion)

        entry4.place(x=140.0, y=135,
                     width=170.0,
                     height=28)

        self._canvas.create_text(83.5, 149.0,
                                 text="Dirección",
                                 fill="#000000",
                                 font=("Inter-Regular", int(15.0)))

        img0 = PhotoImage(file="src/assets/signup_assets/button_signup.png")
        b0 = Button(self,
                    image=img0,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.comprobar_campos,
                    relief="flat")

        b0.place(x=225, y=250,
                 width=200,
                 height=38)

        self.mainloop()

    # Llamar a la base de datos para verificar si el usuario existe
    def comprobar_repetido(self):
        if self._sql.buscar_cliente(self._usuario.get()):
            return messagebox.showinfo("Advertencia",
                                       "Ya existe un usuario con ese nombre")
        return self.registrar()

    # Metodo para verificar si los EntryBox estan vacios
    def comprobar_campos(self):
        if (self._nombre.get() and
                self._apellido.get() and
                self._direccion.get() and
                self._usuario.get() and
                self._clave.get()):

            return self.comprobar_repetido()

        return messagebox.showerror("Error",
                                    "Debe completar todos los campos")

    # Metodo para registar los datos a la base
    def registrar(self):
        if self._sql.insertar_cliente('cliente',
                                      ['usuario',
                                       'clave',
                                       'nombre',
                                       'apellido',
                                       'direccion'],
                                      [(self._usuario.get()),
                                       (self._clave.get()),
                                       (self._nombre.get()),
                                       (self._apellido.get()),
                                       (self._direccion.get())]):

            messagebox.showinfo("Información",
                                "Se a registrado exitosamente")
            return self.destroy()

        return messagebox.showerror("Error",
                                    "Error al registrar los datos")
