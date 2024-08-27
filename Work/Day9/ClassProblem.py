import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import xlabel

x = np.array([80 , 90 , 100 , 110 , 120])
y = np.array([87 , 88 , 91 , 100 , 103])

plt.xlabel("Calories Burned Out")
plt.ylabel("Average Pulse")
plt.title("Smart Watch Data")
plt.plot(x , y , 'o',color = 'r' , linestyle = 'dashed' , ms =10 , mfc ='g' )
plt.grid()
plt.savefig("Smart Watch Data")