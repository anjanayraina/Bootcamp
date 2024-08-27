import matplotlib.pyplot as plt
import numpy as np

x = np.array(range(0 , 4 ))
y = np.array(range(3 , 7))
plt.subplot(1,2,1)
plt.title("Income")
plt.plot(x,y)

plt.subplot(1,2,2)
plt.title("Sales")
plt.plot(x,y)
plt.suptitle("Finances")
plt.savefig("Plots")

