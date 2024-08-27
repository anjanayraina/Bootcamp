import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A' , 'B' , 'C' , 'D'])
y = np.array([3,7,1,10])
plt.bar(x , y  , color = "red" , width = 0.2) # you can also use barh to display horizontal bars
plt.title("Bar Graph")
plt.savefig("Bar Graph")
