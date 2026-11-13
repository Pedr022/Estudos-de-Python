import pandas as pd
import matplotlib.pyplot as plt

Y1 = []

x = -2
for e in range(97):
    eq1 = (1-(round(abs(x), 2)-1)**2)**0.5
    Y1.append(eq1)
    x += 1/24

Y2 = []
x = -2
for e in range(97):
    eq2 = (-2.5)*(1-(round(abs(x),2)/2)**0.5)**0.5
    Y2.append(eq2)
    x += 1/24

X = []
x = -2
for e in range(97):
    X.append(x)
    x = float(f'{x+(1/24):.2f}')

tabela = {'X': X,
          'Y1': Y1,
          'Y2': Y2}

grafico = pd.DataFrame(tabela)
print(grafico.info())

grafico.plot.line(x='X', alpha=1)
print(plt.show())
