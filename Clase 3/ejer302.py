print( "\033[H\033[J")
an=int(input("Ingrese su año de nacimiento: "))
e=2023-an
if e>=18:
    print("Es mayor de edad")
else:
    print("es menor de edad")