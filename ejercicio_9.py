a=int(input(print("ingresa un numero")))
b=int(input(print("ingresa otro numero")))
print("MENU PRINCIPAL")
print("(+) suma a + b")
print("(-) resta a - b")
print("(*) muntiplicacion de a * b")
print("(/) divicion de a/b")
simbolo=input("ingresa la operacion que desea realizar")
match simbolo:
    case "+":
        print("el resultado es  ", (a+b))
    case "-":
        print("el resultado es  ",  (a-b))
    case "*":
        print("el resultado es  ",  (a*b))
    case "/":
        if b !=0:
            print("el resultado es  ",  (a/b))
        else:
            print("no se puede dividir entre 0")
    case _:
        print("operacion invalida")
        
    