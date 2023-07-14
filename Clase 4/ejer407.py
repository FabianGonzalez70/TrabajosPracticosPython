print( "\033[H\033[J")
def cuadra(j):
        listacua=[]
        for v in range(0,len(j)):
            if j[v]%2==0:
                 listacua.append(j[v])
        return(listacua)

print( "\033[H\033[J")
lnum=[]
cn=int(input("Ingrese la cantidad de números que desea cargar a la lista:"))
for a in range(0,cn):
    n=int(input("Ingrese un número: "))
    lnum.append(n)
print("La siguiente es la lista de los números pares de los números ingresados: ")
print(cuadra(lnum))
