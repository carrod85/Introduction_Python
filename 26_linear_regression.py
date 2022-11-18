import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
df = pd.read_excel('pruebapandas.xlsx')
x=df.Number
y=df.Price
stats = linregress(x,y)
# linear equation y = mx + a
m = stats.slope
a = stats.intercept

plt.plot(x, m*x+a, 'bo-')
plt.xlabel("Number",fontsize=10)
plt.ylabel("Price", fontsize= 10)
plt.show()
plt.savefig("pythonlinearregresion.png")
