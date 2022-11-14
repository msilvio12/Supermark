import src.package.customer
import src.package.product
import src.package.shopping_cart
import src.package.card


item = [src.package.product.Producto('Arroz', 'Dia', 'Perecedero', 80, 90.70),
        src.package.product.Producto('Fideo', 'Sol', 'Perecedero', 30, 50.30),
        src.package.product.Producto('Lenteja', 'Noche', 'Perecedero', 120, 80.10)]

carrito1 = src.package.shopping_cart.Carrito.agregar(item, cantidad)

print(carrito1)