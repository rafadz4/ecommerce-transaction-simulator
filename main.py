from catalog import show_catalog
from cart import add_product_to_cart , remove_cart , empty_cart, show_cart
from checkout import check_out

def show_menu() -> None:

    print("""
        Bienvenido a la Tienda Virtual 
        ¿Que deseas hacer?
        
        1. Ver catálogo
        2. Agregar producto al carrito
        3. Eliminar producto del carrito
        4. Vaciar carrito
        5. Mostrar carrito
        6. Finalizar compra
        7. Salir
        """)

def main()->None:
    
    while True:

        show_menu()
        option = input("Eliga una opcion:")
        
        try :
            if option == "1":
                show_catalog()
            elif option == "2":
                add_product = input("Ingrese código de producto :")
                add_product_to_cart(add_product)
            elif option =="3":
                remove_product = input("Ingrese el producto a eliminar:")
                remove_cart(remove_product)
            elif option =="4":
                empty_cart()
            elif option == "5":
                show_cart()
            elif option == "6":
                check_out()
            elif option == "7":
                break
                

        except ValueError : 
            print("Ingrese un número válido para la opcion")

            
main()