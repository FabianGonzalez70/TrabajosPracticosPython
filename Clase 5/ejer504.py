import matplotlib.pyplot as plt
print( "\033[H\033[J")
tempchi=[5,4,4,6,8,8,8,10,12,15,15,17,17,17,18,20,16,15,15,12,11,8,8,6]
tempbari=[-10,-8,-7,-5,-1,0,3,3,3,5,5,5,3,3,0,0,0,0,-2,-2,-5,-6,-8,-8]
x=range(24)
ref1=["Chilecito"]
ref2=["Bariloche"]
plt.plot(x,tempchi, 'r^--',label="Chilecito")
plt.legend(loc="upper left")
plt.plot(x,tempbari, 'go--',label="Bariloche")
plt.legend(loc="upper left")
plt.title("CHILECITO - Variación de temperaturas por hora")
plt.xlabel("Horas")
plt.ylabel("Grados")
plt.show()

