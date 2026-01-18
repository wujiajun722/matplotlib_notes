import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建子图
fig, ax = plt.subplots(1, 1, figsize=(10,5))
# 知道三角形的两条边长和夹角,计算顶点坐标
a = 0.6  # 边长a
b = 0.5  # 边长b
theta = np.radians(60)  # 夹角60度转换为弧

# 计算顶点坐标
A = [0.2, 0.2]
B = [A[0] + a, A[1]]
C = [A[0] + b * np.cos(theta), A[1] + b * np.sin(theta)]
# 创建三角形
triangle = mpatches.Polygon([A, B, C], facecolor='lightcoral', edgecolor='darkred', linewidth=2, alpha=0.7)
ax.add_patch(triangle)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_title('已知两边和夹角的三角形')
# *A表示解包坐标,*解包操作符,表示将元组拆开,写字在旁边,
ax.plot(*A, 'ro', label='顶点A')  # 标记顶点A
ax.plot(*B, 'go', label='顶点B')  # 标记顶点B
ax.plot(*C, 'bo', label='顶点C')  # 标记顶点C

ax.text(*A, 'A', fontsize=12, ha='right', va='bottom')
ax.text(*B, 'B', fontsize=12, ha='left', va='bottom')
ax.text(*C, 'C', fontsize=12, ha='center', va='bottom')
ax.legend()

plt.savefig("figures/section2/2.4.png", dpi=300)
plt.show()