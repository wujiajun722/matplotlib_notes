import matplotlib.pyplot as plt
import numpy as np
# 添加中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 两行一列子图
fig,ax = plt.subplots(2,1)
x = np.arange(0,10,0.1)
y0 = np.cos(x)
y1 = np.sin(x)

fig.suptitle('正余弦函数图像', fontsize=16)
ax[0].set_title('余弦函数')
ax[0].plot(x,y0)
ax[1].set_title('正弦函数')
ax[1].plot(x,y1)


plt.show()