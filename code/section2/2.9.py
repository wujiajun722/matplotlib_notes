import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig,ax = plt.subplots()

ellipse = mpatches.Ellipse((0,0),1.,0.6,fc = 'red',ec = 'blue')
circle = mpatches.Circle((0,0),0.5,fc = 'yellow',alpha = 0.5,ec = 'red')
regularPolygon = mpatches.RegularPolygon((0,0),numVertices=5,radius=0.5,alpha = 0.5)
ax.add_patch(ellipse)
ax.add_patch(circle)
ax.add_patch(regularPolygon)
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_aspect('equal')
# 文件保存
script_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig("figures/section2/" + script_name + '.png')
plt.show()