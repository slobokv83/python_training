import numpy as np

x = np.array([0,1,2,3,2,3,4,5,5,6])
y = np.array([7,2,10,2,7,4,9,4,9,8])

a = np.intersect1d(x,y)
print(a)