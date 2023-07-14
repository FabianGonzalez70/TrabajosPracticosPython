def prome(j):
    acu=0
    for v in range(0,len(j)):
        acu=acu+j[v]
        pro=acu/len(j)
    return(pro)

print( "\033[H\033[J")
lnum=[]
cn=int(input("Ingrese la cantidad de números que desea promediar:"))
for a in range(0,cn):
    n=int(input("Ingrese un número: "))
    lnum.append(n)
print("El promedio de los números ingresados es: ", prome(lnum))
