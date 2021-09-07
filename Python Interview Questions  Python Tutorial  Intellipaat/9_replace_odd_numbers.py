import numpy as np

x= np.arange(0,10,1)

# x = [0,1,2,3,4,5,6,7,8,9]

# The first solution
# for i in x:
#     if(i%2):
#         x[i]=-1

# The second solution
x[x%2] = -1 # has to be numpy array

print(x)