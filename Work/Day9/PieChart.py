import matplotlib.pyplot as plt
import numpy as np


y = np.array([3,7,1,10])
plt.pie(y)
plt.title("Pie Chart")
plt.savefig("Pie Chart")
