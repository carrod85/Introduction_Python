import pandas as pd

data = pd.read_excel('pruebapandas.xlsx')
group = data.groupby("Price")
print(group.get_group(1))

