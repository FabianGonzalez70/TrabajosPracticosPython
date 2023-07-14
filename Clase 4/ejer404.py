print( "\033[H\033[J")
def tot(fac,iva):
    final=fac+fac*iva/100
    return(final)
a=float(input("Ingrese el importe de la factura: "))
b=float(input("Ingrese el porcentaje de IVA que desea aplicar: "))
fap=tot(a,b)
print(fap)