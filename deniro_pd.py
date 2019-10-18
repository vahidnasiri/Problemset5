import pandas as pd

df = pd.read_csv("deniro.csv", skipinitialspace=True)

print(df.loc[df['Title'] == 'Heat'])
print(df.loc[df['Year'] == 1992])