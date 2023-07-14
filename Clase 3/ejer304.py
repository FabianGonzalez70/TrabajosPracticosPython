print( "\033[H\033[J")
h=int(input("Ingrese kilos de harina disponibles: "))
a=int(input("Ingrese kilos de azúcar disponibles: "))
m=int(input("Ingrese kilos de manteca disponibles: "))
if h>=5:
    if a>=1:
        if m>=2:
            print("Puede comenzar la preparación")
        else:
            print("No cuenta con los ingredientes suficientes")
    else:
        print("No cuenta con los ingredientes suficientes")
else:
    print("No cuenta con los ingredientes suficientes")