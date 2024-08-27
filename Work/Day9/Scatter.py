import matplotlib.pyplot as plt
import numpy as np
x =np.array([range(1 , 10)])
y = np.array([1,10,3,4,14,5,8,1,10])
plt.scatter(x,y , color = 'red')

x = np.array([2,3,1,6,14,13,19,3,4,10])
y = np.array([13,17,11,14,4,13, 6,3, 6,1])
plt.scatter(x ,y , color = 'green' , alpha = 0.5 )
plt.colorbar()
plt.savefig("Scatter Plot")