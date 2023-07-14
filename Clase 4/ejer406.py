print( "\033[H\033[J")
def cuadra(j):
        listacua=[]
        for v in range(0,len(j)):
            cu=j[v]**2
            listacua.append(cu)
        return(listacua)

print( "\033[H\033[J")
lnum=[]
cn=int(input("Ingrese la cantidad de números que desea cargar a la lista:"))
for a in range(0,cn):
    n=int(input("Ingrese un número: "))
    lnum.append(n)
print("La siguiente es la lista de los cuadrados de los números ingresados: ")
print(cuadra(lnum))
