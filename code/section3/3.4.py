import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig,ax = plt.subplots()

x = np.linspace(-6,6.0001,100)
y = np.linspace(-6,6,100)
X,Y = np.meshgrid(x,y)

# 斜率k1 = y/(x+3),斜率k2 = y/(x-3)
# k1 * k2 = 4/9

Z = Y/(X + 3) * Y/(X-3) 
ax.contour(X, Y, Z, levels=[-4/9,4/9], colors='black')

# 文件保存
script_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig("figures/section3/" + script_name + '.png')
plt.show()