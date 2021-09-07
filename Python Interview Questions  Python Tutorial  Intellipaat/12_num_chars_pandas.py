import pandas as pd

x = "mary had a little lamb".split()

df = pd.Series(x)

df = df.map(lambda x: len(x))

print(df)
