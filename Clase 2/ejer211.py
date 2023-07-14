cap=float(input("ingrese el capital inicial: "))
d1=cap*(1+50)*5
d2=cap*(1+3.5)*60
if d1>d2:
    print("Es falso, no conviene invertir en el nuevo banco")
else:
    print("es cierto, conviene optar por el nuevo banco")
print("Beneficios que obtendrías con la propuesta original: ",d1)
print("Beneficios que obtendrías con la propuesta nueva: ",d2)