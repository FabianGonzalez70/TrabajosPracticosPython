print( "\033[H\033[J")
p=input("ingrese una palabra (salir para finalizar): ")
while p!="salir":
    print("Ud. escribió: ",p)
    pausa=input("presione ENTER paa continuar")
    print( "\033[H\033[J")
    p=input("ingrese una palabra: ")
print("Fin del programa")