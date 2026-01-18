import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots()
# 创建一个正方形
rec = mpatches.Rectangle((0.2,0.2), 0.6, 0.6, facecolor='blue', edgecolor='black')
ax.add_patch(rec)

ax.plot(0.2,0.2,color = 'red', marker = 'o', markersize=10)

ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_title('正方形示例')
# x轴和y轴一样长
ax.set_aspect('equal')
# 保持图形
plt.savefig('figures/section2/2.1.png')
plt.show()