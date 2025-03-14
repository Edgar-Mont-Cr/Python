n1=int(input("dame un numero"))
n=2
x=1
v = 0 
while x<=n1:
    v += x**n
    x+=1
    n+=1
c=v/n1
print("el resultado es ", c ) 