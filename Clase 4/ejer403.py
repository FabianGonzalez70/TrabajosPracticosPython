print( "\033[H\033[J")
def facto(a):
    v=1
    for b in range(1,a+1):
        v=v*b
    return v
z=int(input("Ingrese un número: "))
print("El factrial de",z,"es:",facto(z))