from tkinter import Tk, ttk, Frame, Toplevel, Canvas, PhotoImage, StringVar, Entry, Button, messagebox
from sql.query import Consulta


class Registro(Toplevel):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.wait_visibility()  # <-- Espera a que la ventana se crea para enfocarla
        self.grab_set()  # <-- Permite no interactuar con la ventana raiz hasta cerrarla
        self.title("Registro")  # <-- Titulo de la ventana
        self.geometry("650x350")  # <-- Dimension de la ventana
        self.iconbitmap("src/assets/logosupermark.ico")  # <-- Icono a venta
        self.configure(bg="#f49739")  # <-- Color de fondo de la ventana
        self.nombre = StringVar()  # <-- Retener datos para registrar a SQLite
        self.apellido = StringVar()
        self.direccion = StringVar()
        self.usuario = StringVar()
        self.clave = StringVar()
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
        self.ventana_registro()  # <-- Instanciar metodo
        self.mainloop()  # <-- Mantener la ventana ejecutansose hasta destruirla

    def ventana_registro(self):
        background_img = PhotoImage(file=f"src/assets/singup/background.png")

        background = self.canvas.create_image(325.0, 235.0,
                                              image=background_img)

        entry0_img = PhotoImage(file=f"src/assets/singup/img_textBox0.png")
        entry0_bg = self.canvas.create_image(225.0, 39.0,
                                             image=entry0_img)

        entry0 = Entry(self,
                       bd=0,
                       bg="#ffffff",
                       highlightthickness=0)

        entry0.place(x=140.0, y=24,
                     width=170.0,
                     height=28)

        self.canvas.create_text(88.5, 39.0,
                                text="Nombre",
                                fill="#000000",
                                font=("Inter-Regular", int(15.0)))

        entry1_img = PhotoImage(file=f"src/assets/singup/img_textBox1.png")
        entry1_bg = self.canvas.create_image(225.0, 95.0,
                                             image=entry1_img)

        entry1 = Entry(self,
                       bd=0,
                       bg="#ffffff",
                       highlightthickness=0)

        entry1.place(x=140.0, y=80,
                     width=170.0,
                     height=28)

        self.canvas.create_text(88.5, 94.0,
                                text="Apellido",
                                fill="#000000",
                                font=("Inter-Regular", int(15.0)))

        entry2_img = PhotoImage(file=f"src/assets/singup/img_textBox2.png")
        entry2_bg = self.canvas.create_image(513.0, 39.0,
                                             image=entry2_img)

        entry2 = Entry(self,
                       bd=0,
                       bg="#ffffff",
                       highlightthickness=0)

        entry2.place(x=428.0, y=24,
                     width=170.0,
                     height=28)

        self.canvas.create_text(377.5, 39.0,
                                text="Usuario",
                                fill="#000000",
                                font=("Inter-Regular", int(15.0)))

        entry3_img = PhotoImage(file=f"src/assets/singup/img_textBox3.png")
        entry3_bg = self.canvas.create_image(513.0, 95.0,
                                             image=entry3_img)

        entry3 = Entry(self,
                       bd=0,
                       bg="#ffffff",
                       highlightthickness=0)

        entry3.place(x=428.0, y=80,
                     width=170.0,
                     height=28)

        self.canvas.create_text(385.0, 94.0,
                                text="Clave",
                                fill="#000000",
                                font=("Inter-Regular", int(15.0)))

        entry4_img = PhotoImage(file=f"src/assets/singup/img_textBox4.png")
        entry4_bg = self.canvas.create_image(225.0, 150.0,
                                             image=entry4_img)

        entry4 = Entry(self,
                       bd=0,
                       bg="#ffffff",
                       highlightthickness=0)

        entry4.place(x=140.0, y=135,
                     width=170.0,
                     height=28)

        self.canvas.create_text(83.5, 149.0,
                                text="Dirección",
                                fill="#000000",
                                font=("Inter-Regular", int(15.0)))

        img0 = PhotoImage(file=f"src/assets/singup/img0.png")
        b0 = Button(self,
                    image=img0,
                    borderwidth=0,
                    highlightthickness=0,
                    command=self.confirmar_registro,
                    relief="flat")

        b0.place(x=225, y=250,
                 width=200,
                 height=38)

        self.mainloop()

    def confirmar_registro(self):
        if self.nombre.get() and self.apellido.get() and self.direccion.get() and self.usuario.get() and self.clave.get() != None:
            if self.comprobar_repetido():
                self.sql.insertar_registro('cliente', ['usuario', 'clave', 'nombre', 'apellido', 'direccion'],
                                           ["'Magia'", '1234', "'Anonimo'", "'Pepe'", "'Av. Libertad'"])
            else:
                messagebox.showerror(title="Error",
                                     message="Error al registrar los datos")
        else:
            messagebox.showwarning(title="Advertencia",
                                   message="No completo ningun campo")

    def comprobar_repetido(self):
        if not self.sql.buscar_usuario(self.usuario.get(), self.clave.get()):
            messagebox.showinfo(title="Información",
                                message="Confirmar registro")
        else:
            messagebox.showerror(title="Error",
                                 message="Ya existe un usuario con ese nombre")
