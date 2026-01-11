import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()
x = np.arange(0,10,0.1)
y = np.cos(x)

ax.plot(x,y)
plt.show()
