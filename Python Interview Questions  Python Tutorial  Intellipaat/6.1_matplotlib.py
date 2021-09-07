from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0,10,1)
y = np.arange(0,10,1)

plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('X vs Y')
plt.show()

