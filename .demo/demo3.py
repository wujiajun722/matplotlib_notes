import matplotlib.pyplot as plt
import numpy as np
# 添加中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig,ax = plt.subplots()
x = np.arange(0,10,0.1)
y = np.cos(x)
ax.set_title('余弦函数')

ax.plot(x,y)
plt.show()
