import numpy as np
from matplotlib import pyplot as plt

data = {"apple": 50,"banana": 20, "orange":30}

names = list(data.keys())
values = list(data.values())

plt.bar(names, values)
plt.title('fruit cost')
plt.xlabel('fruit')
plt.ylabel('cost')
plt.show()