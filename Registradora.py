producto=[]
almacenamiento={"productos": producto, "presio_unitario": ""}

while True:
    for i in range(6):
        nomprod = input("ingresa tu producto")
        producto.append(nomprod)
    res=input("ingresa  aisi desas otra compra")
    if(res.lower != "si"):
        break

for productos in almacenamiento["productos"]:
    print(productos)