import numpy as np
import matplotlib.pyplot as plt
x = np.random.rand(1000)
print(x)
plt.hist(x , bins = 30 , color = 'skyblue' , edgecolor = 'black')
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.savefig("Histogram")