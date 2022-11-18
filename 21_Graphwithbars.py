import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_excel('waiting_times.xlsx')

costumer = df["costumer"]
seconds = df["waiting_time"]
ys = list()
limite_seconds = round(max(seconds))


while limite_seconds % 5 != 0:
    limite_seconds += 1



for i in range(0,limite_seconds,5):
    ys.append(i)




xs = range(len(costumer))



plt.bar(xs, seconds)
plt.xticks(xs, costumer)
plt.yticks(ys)
plt.ylabel("seconds \n waiting")
plt.xlabel("costumers")
plt.title("waiting time Costumers")
plt.show()