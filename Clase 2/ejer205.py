cc=int(input("Ingrese cantidad de comensales: "))
dp=int(input("Ingrese dinero por persona: "))
vp=int(input("Ingrese el valor del plato: "))
vaquita=cc*dp
cp=vaquita//vp
print("Se podrán consumir ",cp, " platos.")
print("Sobran: ",vaquita%vp," pesos")
