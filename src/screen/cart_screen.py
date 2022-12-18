from tkinter import (END, Button, Label, Listbox, Tk, messagebox, simpledialog)


class ShoppingCart:
    def __init__(self, master):
        self.master = master
        master.title("Carrito de compras")

        self.total = 0
        self.items = []

        self.label = Label(master, text="Carrito de compras",
                           font=("Helvetica", 18))
        self.label.pack()

        self.shopping_list = Listbox(master, font=("Helvetica", 14))
        self.shopping_list.pack()

        self.total_label = Label(
            master, text="Total: $0", font=("Helvetica", 14))
        self.total_label.pack()

        self.add_button = Button(master, text="Agregar", font=(
            "Helvetica", 14), command=self.add_item)
        self.add_button.pack()

        self.remove_button = Button(master, text="Quitar", font=(
            "Helvetica", 14), command=self.remove_item)
        self.remove_button.pack()

        self.checkout_button = Button(master, text="Finalizar compra", font=(
            "Helvetica", 14), command=self.checkout)
        self.checkout_button.pack()

    def add_item(self):
        item = simpledialog.askstring(
            "Carrito de compras", "Desea agregar?")
        price = simpledialog.askfloat(
            "Carrito de compras", "cueal es el precio?")

        if item is not None and price is not None:
            self.items.append(item)
            self.shopping_list.insert(END, f"{item} (${price})")
            self.total += price
            self.total_label["text"] = f"Total: ${self.total}"

    def remove_item(self):
        index = self.shopping_list.curselection()
        item = self.shopping_list.get(index)
        price = float(item[item.find("$") + 1:])

        self.total -= price
        self.total_label["text"] = f"Total: ${self.total}"

        self.shopping_list.delete(index)
        self.items.remove(item[:item.find("$") - 1])

    def checkout(self):
        if len(self.items) > 0:
            messagebox.showinfo(
                "Carrito de compras", f"""Tu compra {', '.join(self.items)}
                con un total de ${self.total}.""")
            self.total = 0
            self.total_label["text"] = f"Total: ${self.total}"
            self.items = []
            self.shopping_list.delete(0, END)
        else:
            messagebox.showinfo(
                "Carrito de compras", "No tiene ningun producto para comprar!")


root = Tk()
my_gui = ShoppingCart(root)
root.mainloop()
