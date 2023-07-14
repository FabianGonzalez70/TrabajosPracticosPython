print( "\033[H\033[J")
e=int(input("Ingrese su edad: "))
if e<2:
    print("No paga")
elif e<=4:
    print("Ud. paga $100")
elif e<=10:
    print("Ud. paga $200")
elif e<=18:
    print("Ud. paga $400")
elif e<70:
    print("Ud. paga $1000")
else:
    print("Ud. paga $500")