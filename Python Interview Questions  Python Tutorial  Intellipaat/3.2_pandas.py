import pandas as pd

iris = pd.read_csv('iris.csv')

iris1 = iris[(iris['Sepal.Length']>5) & (iris['Sepal.Width']>3)]

print(iris1)
print(iris.head())