from data import WAREHOUSE , SHOPPING_CART
from utils import input_int



def add_product_to_cart(code:str)->None:

    if code not in WAREHOUSE : 
        print ("Producto no encontrado")
        return

    product = WAREHOUSE[code]
    cantidad = int(input_int("Cantidad:"))

    if code in SHOPPING_CART : 
        SHOPPING_CART[code]["cantidad"] += cantidad
    else : 
        SHOPPING_CART[code] = {
            "nombre" : product["nombre"] , 
            "precio":product["precio"],
            "cantidad" : cantidad
        }   
    print("Producto agregado al carrito")


def remove_cart(code:str) ->None: 
        
        if code in SHOPPING_CART:
            del SHOPPING_CART[code]
            print(f"✔ Producto eliminado del carrito.")
            return 

        print("El producto no esta en el carrito")

def empty_cart()-> None:
    SHOPPING_CART.clear()
    print("El carrito esta vacio")


def show_cart()-> None:

    total = 0

    if len(SHOPPING_CART)  == 0:
        print("El carrito esta vacio")
    else:
        print("Tu carrito: ")
        for product in SHOPPING_CART.values(): 
            subtotal = product["cantidad"] * product["precio"]
            total += subtotal
            print(f"Producto : {product['nombre']} (x{product['cantidad']}) -> S/.{subtotal:.2f} ")

    print(f"Total: S/.{total:.2f}")
