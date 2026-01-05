def input_int(mensaje:str) -> int : 
    while True: 
        try : 
            valor = int(input(mensaje))
            if valor <=0 : 
                print("Ingrese un numero mayor a  0 :")
                continue 
            return valor
        except ValueError :
            print("Debe ingresar un numero válido")

