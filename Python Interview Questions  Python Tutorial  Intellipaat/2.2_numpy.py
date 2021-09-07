import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])


print('a+b:',a+b)

c = [1,2,3]
d = [4,5,6]

print('c+d:',c+d)

e = np.sum((a,b), axis=0)
f = np.sum((a,b), axis=1)
print('e:', e)
print('f:', f)