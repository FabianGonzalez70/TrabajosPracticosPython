print( "\033[H\033[J")
n=int(input("ingrese un número: "))
if n%2==0:
    print("El número ",n," es par")
else:
    print("El número ",n," es impar")