import matplotlib.pyplot as plt
print( "\033[H\033[J")
tempchi=[5,4,4,6,8,8,8,10,12,15,15,17,17,17,18,20,16,15,15,12,11,8,8,6]
x=range(24)
plt.fill_between(x,tempchi)
plt.title("CHILECITO - Variación de temperaturas por hora")
plt.xlabel("Horas")
plt.ylabel("Grados")
plt.show()
