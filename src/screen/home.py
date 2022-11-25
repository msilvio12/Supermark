from tkinter import Frame, Label, Button


class Inicio(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=380, height=520, bg='#14213d')
        self.frame = master
        self.pack()
        self.create_frame()

    def create_frame(self):
        frame1 = Frame(self, width=380, height=60, bg='#fca311')
        frame1.place(x=0, y=0)
        Label(frame1, text='INICIO DE SESIÓN').pack(side='bottom')
