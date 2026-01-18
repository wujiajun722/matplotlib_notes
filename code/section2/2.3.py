import matplotlib.pyplot as plt
import matplotlib.patches as mpathes
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建子图
fig, ax = plt.subplots(1, 2, figsize=(10,5))
# 创建一个等边三角形,中心在(0.5,0.5),边长为0.8,RegularPolygon表示正多边形,numVertices=3表示三边形,radius表示外接圆半径,orientation表示旋转角度 pi/2表示旋转90度
triangle = mpathes.RegularPolygon((0.5, 0.5), numVertices=3, radius=0.4, orientation=np.pi / 2,
                                  facecolor='lightcoral', edgecolor='darkred', linewidth=2, alpha=0.7)
ax[0].add_patch(triangle)
ax[0].set_xlim(0, 1)
ax[0].set_ylim(0, 1)
ax[0].set_aspect('equal')
ax[0].set_title('等边三角形')

# 创建一个直角三角形,顶点坐标为(0.2,0.2),(0.8,0.2),(0.8,0.8)
right_triangle = mpathes.Polygon([(0.2, 0.2), (0.8, 0.2), (0.8, 0.8)], facecolor='lightblue', edgecolor='darkblue', linewidth=2, alpha=0.7)
ax[1].add_patch(right_triangle)
ax[1].set_xlim(0, 1)
ax[1].set_ylim(0, 1)
ax[1].set_aspect('equal')
ax[1].set_title('直角三角形')

plt.savefig("figures/section2/2.3.png", dpi=300)
plt.show()