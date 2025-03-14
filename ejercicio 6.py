acu=0
while True: #al menos una vez se ejecutara
    n1=(input("teclea un numero: o presione S para salir del programa"))
    if (n1=="S"):
        break #rompe el ciclo
    else:
        acu=acu+int(n1) #toma n1 como entero
#esta fuera del ciclo lo siguente
if (acu>0):
    print("el resultado final del acumulador es------->" ,acu)
else:
    print("se pulsa S para salir")