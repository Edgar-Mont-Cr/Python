mon=float(input(print("Ingresa el saldo total que poses ahora  ")))
while (mon>0):
    print("ingresa el nombre y valor de cada producto que desea comprar")
    nom=input(print("ingresa el nombre del producto"))
    i=float(input(print("ingresa el costo del producto")))
    if (i<mon):
        print("El producto es :", nom)
        print("El costo es :",  i )
        x=(mon-i)
        print("tu saldo es ---->",  x,"\n\n")
    else:
        print("El producto es :", nom)
        print("El costo es :",  i )
        print("el producto es demaciado caro para el sado disponible \n cuentas con---->", mon , "\n")
    if (x==mon):
        break
    mon=x

print("gracias por comprar con nosotros")