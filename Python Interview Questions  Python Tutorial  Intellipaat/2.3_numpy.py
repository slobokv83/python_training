import numpy as np

a = np.array([12,43,2,100,54,5,68])

print(a[np.argsort(a)[-2:][::-1]])