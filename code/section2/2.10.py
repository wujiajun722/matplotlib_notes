import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()

# 使用 patches 自定义样式
wedge0 = mpatches.Wedge((0.,0.),0.5,theta1=0,theta2=30,linewidth=2, edgecolor='purple', facecolor='plum', alpha=0.7)
wedge1 = mpatches.Wedge((0.,0.),0.5,theta1=30,theta2=60,linewidth=2, edgecolor='green', facecolor='purple', alpha=0.7)
wedge2 = mpatches.Wedge((0.,0.),0.5,theta1=60,theta2=150,linewidth=2, edgecolor='black', facecolor='green', alpha=0.7)
wedge3 = mpatches.Wedge((0.,0.),0.5,theta1=150,theta2=290,linewidth=2, edgecolor='blue', facecolor='yellow', alpha=0.7)
wedge4 = mpatches.Wedge((0.,0.),0.5,theta1=290,theta2=360,linewidth=2, edgecolor='plum', facecolor='red', alpha=0.7)

ax.add_patch(wedge0)
ax.add_patch(wedge1)
ax.add_patch(wedge2)
ax.add_patch(wedge3)
ax.add_patch(wedge4)
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_aspect('equal') 
# 文件保存
script_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig("figures/section2/" + script_name + '.png')
plt.show()