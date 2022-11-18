import pandas as pd

df = pd.read_excel('pruebapandas.xlsx')
df['New_col']=df['Number']* df['Price']
print(df.New_col)
