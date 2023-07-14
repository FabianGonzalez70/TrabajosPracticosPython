import matplotlib.pyplot as plt
print( "\033[H\033[J")
llutucu=[180,120,95,80,50,33,25,30,44,56,72,123]
x=range(1,13)
plt.bar(x,llutucu,color="red")
plt.xticks(x)
plt.title("Tucumán - Variación de lluvias anual")
plt.xlabel("Meses")
plt.ylabel("Milímetros")
plt.show()