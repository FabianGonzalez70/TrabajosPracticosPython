print( "\033[H\033[J")
def saludo(h):
    if h<12:
        return "Que tengas un buen día"
    elif h<20:
        return "Que tengas una buena tarde"
    else:
        return "Que tengas una buena noche"

ha=int(input("ingrese la hora actual: "))
print(saludo(ha))