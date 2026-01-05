from data import WAREHOUSE , SHOPPING_CART
from datetime import datetime


def check_out()->None:
    
    if len(SHOPPING_CART) == 0:
        print("No realizo ninguna compra")
    else:
        print("Resumen de compra: ")
        total = 0
        for product in SHOPPING_CART.values():
            subtotal  = product["cantidad"] * product["precio"]
            total +=subtotal
            print(f"{product['nombre']} (x{product["precio"]}) -> S/.{subtotal:.2f} ")

        print(f"Total a pagar :{total:.2f} ")    
        print("Gracias por su compra ")

    SHOPPING_CART.clear()

