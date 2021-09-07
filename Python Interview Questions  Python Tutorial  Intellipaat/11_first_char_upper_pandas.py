import pandas as pd

x= "mary had a little lamb".split()

df = pd.Series(x)

df = df.map(lambda x: x.title())
print(df)