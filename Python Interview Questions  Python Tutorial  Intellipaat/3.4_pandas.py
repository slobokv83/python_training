import pandas as pd
import numpy as np


iris = pd.read_csv('iris.csv')



print(iris.isna().sum())