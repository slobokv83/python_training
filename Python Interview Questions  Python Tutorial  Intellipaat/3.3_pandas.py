import pandas as pd
import numpy as np

iris = pd.read_csv('iris.csv')

iris1 = iris
iris1.iloc[0:10,1:3] = np.NaN

print(iris1)