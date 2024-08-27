import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

x = np.array([1,2,3,4])
y = x**2
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Parabola")
plt.plot(x,y ,'o:r' , mec = 'g' ) # this is called a fmt notation for adding dashed lines and the color , o - circle and r - red
plt.grid()
plt.show()
plt.savefig("parabola.png")