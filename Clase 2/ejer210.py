cap=float(input("ingrese el capital inicial: "))
d1=cap*(1+50)*5
d2=cap*(1+25)*10
print("Invirtiendo en plazo fijo obtendrías: $",d1)
print("Invirtiendo en bonos obtendrías: $",d2)
if d1>d2:
    print("Conviene el plazo fijo")
else:
    print("Conviene invertir en bonos")