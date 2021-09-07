import pandas as pd

iris = pd.read_csv('iris.csv')
iris = iris.rename(columns={'Sepal.Length': 'S_Length'})
print(iris)