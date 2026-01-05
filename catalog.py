from data import WAREHOUSE

def show_catalog()-> None:

    for code, product in WAREHOUSE.items():
        print(f"Código: {code:<8}|  Producto:{product['nombre']:<7}|  Precio:{product['precio']:.2f} ")