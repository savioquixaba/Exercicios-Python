import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 15, 20])


plt.xlabel("Produtos") # a linha X mostra o titulo abaixo das barras
plt.ylabel("Valores") # mostra o titulo ao lado esquerdo das barras
plt.title("Grafico de barras") # titulo do projeto
plt.bar(x, y) # aqui cria as barras x, y
plt.show() # como se fosse um print para mostrar o grafico